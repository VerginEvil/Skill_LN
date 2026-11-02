import java.io.*;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.resource.ResourceException;
import javax.resource.cci.Connection;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.xml.sax.InputSource;

import com.infor.erpln.jca.ConnectionFactoryImpl;
import com.infor.erpln.jca.ConnectionSpecImpl;
import com.infor.erpln.jca.OAuth2Callback;
import com.infor.erpln.jca.bdeclient.BdeElementIterator;
import com.infor.erpln.jca.bdeclient.BdeFilter;
import com.infor.erpln.jca.bdeclient.BdeSelection;
import com.infor.erpln.jca.bdeclient.JcaBdeManager;

/**
 * LNStudioJcaBridge
 * Headless Infor LN JCA 1.6 Bridge for automated BDE execution, explorers, and SCM.
 *
 * Supports:
 * 1. One-shot CLI invocation (--ping, --bde) for backward compatibility
 * 2. Persistent JCA Daemon (--daemon) over 127.0.0.1 TCP holding a single persistent
 *    JCA connection per connection point with a Sequential FIFO Command Queue,
 *    dynamic OAuth2 token hot-swap, and 30-minute idle auto-shutdown.
 * 3. All 5 BdeManager execution modes (LIST=0, SHOW=1, BDE=2, SPECIALLIST=3, BROWSELIST=4).
 *
 * Protocol-Level Safety Guarantee (ADR 0007 / ADR 0008 / ADR 0012):
 * Execution of EndActivity, CloseTask, FinalizeActivity, or Deliver is physically blocked
 * at the Java bridge layer before any JCA connection or BDE call can occur.
 */
public class LNStudioJcaBridge {

    private static final String[] PROHIBITED_METHODS = new String[] {
        "endactivity",
        "closetask",
        "finalizeactivity",
        "deliveractivity",
        "commitactivity",
        "completeactivity"
    };

    private static final String[] PROHIBITED_XML_TAGS = new String[] {
        "<endactivity",
        "<closetask",
        "<finalizeactivity",
        "<deliveractivity",
        "<end/>",
        "<end>",
        "<deliver/>",
        "<deliver>"
    };

    public static boolean isProhibitedOperation(String bdeName, String methodName, String reqXml) {
        String mLower = methodName == null ? "" : methodName.trim().toLowerCase(Locale.ROOT);
        String bLower = bdeName == null ? "" : bdeName.trim().toLowerCase(Locale.ROOT);
        for (String forbidden : PROHIBITED_METHODS) {
            if (mLower.equals(forbidden) || mLower.contains(forbidden) || bLower.contains(forbidden)) {
                return true;
            }
        }
        if (reqXml != null && !reqXml.isEmpty()) {
            String xmlLower = reqXml.toLowerCase(Locale.ROOT);
            for (String tag : PROHIBITED_XML_TAGS) {
                if (xmlLower.contains(tag)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static String xmlToString(Element elem) throws Exception {
        TransformerFactory tf = TransformerFactory.newInstance();
        Transformer transformer = tf.newTransformer();
        transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        StringWriter writer = new StringWriter();
        transformer.transform(new DOMSource(elem), new StreamResult(writer));
        return writer.toString();
    }

    private static void printXml(Element elem) throws Exception {
        System.out.print(xmlToString(elem));
    }

    private static BdeFilter.Expression parseSingleCondition(BdeFilter bdeFilter, String condition) {
        Pattern p = Pattern.compile("^([a-zA-Z0-9_.]+)\\s*(==|!=|<=|>=|<>|=|<|>|LIKE)\\s*(.*)$", Pattern.CASE_INSENSITIVE);
        Matcher m = p.matcher(condition.trim());
        if (m.matches()) {
            String field = m.group(1).trim();
            String op = m.group(2).trim().toUpperCase(Locale.ROOT);
            String val = m.group(3).trim();
            if ((val.startsWith("'") && val.endsWith("'")) || (val.startsWith("\"") && val.endsWith("\""))) {
                val = val.substring(1, val.length() - 1);
            }
            if ("==".equals(op) || "=".equals(op)) {
                return bdeFilter.createComparisonEqual(field, val);
            } else if ("!=".equals(op) || "<>".equals(op)) {
                return bdeFilter.createComparisonNotEqual(field, val);
            } else if (">=".equals(op)) {
                return bdeFilter.createComparisonGreaterOrEqual(field, val);
            } else if ("<=".equals(op)) {
                return bdeFilter.createComparisonLessOrEqual(field, val);
            } else if (">".equals(op)) {
                return bdeFilter.createComparisonGreater(field, val);
            } else if ("<".equals(op)) {
                return bdeFilter.createComparisonLess(field, val);
            } else if ("LIKE".equals(op)) {
                return bdeFilter.createComparisonLike(field, val);
            }
        }
        return null;
    }

    private static BdeFilter.Expression parseFilterExpression(BdeFilter bdeFilter, String exprStr) {
        if (exprStr == null || exprStr.trim().isEmpty()) {
            return null;
        }
        String trimmed = exprStr.trim();
        if (trimmed.toUpperCase(Locale.ROOT).contains(" AND ")) {
            String[] parts = trimmed.split("(?i)\\s+AND\\s+");
            BdeFilter.Expression combined = null;
            for (String part : parts) {
                BdeFilter.Expression sub = parseSingleCondition(bdeFilter, part);
                if (sub != null) {
                    if (combined == null) {
                        combined = sub;
                    } else {
                        combined = bdeFilter.createLogicalAnd(combined, sub);
                    }
                }
            }
            return combined;
        } else if (trimmed.toUpperCase(Locale.ROOT).contains(" OR ")) {
            String[] parts = trimmed.split("(?i)\\s+OR\\s+");
            BdeFilter.Expression combined = null;
            for (String part : parts) {
                BdeFilter.Expression sub = parseSingleCondition(bdeFilter, part);
                if (sub != null) {
                    if (combined == null) {
                        combined = sub;
                    } else {
                        combined = bdeFilter.createLogicalOr(combined, sub);
                    }
                }
            }
            return combined;
        } else {
            return parseSingleCondition(bdeFilter, trimmed);
        }
    }

    public static void applyControllingAttributes(JcaBdeManager bdeMgr, String methodName, Map<String, String> ctrlAttrs) throws Exception {
        if (ctrlAttrs == null || ctrlAttrs.isEmpty()) {
            return;
        }
        StringBuilder metaSb = new StringBuilder();
        List<String> values = new ArrayList<>();
        for (Map.Entry<String, String> entry : ctrlAttrs.entrySet()) {
            String key = entry.getKey().trim();
            String val = entry.getValue();
            if (metaSb.length() > 0) {
                metaSb.append(":;:");
            }
            if (key.contains(";")) {
                metaSb.append(key);
            } else if (key.contains(":")) {
                metaSb.append(key.replace(":", ";")).append(";false");
            } else {
                metaSb.append(methodName).append(";").append(key).append(";in;false");
            }
            values.add(val);
        }
        bdeMgr.setSpecificControlAttributeMetaData(metaSb.toString());
        for (int i = 0; i < values.size(); i++) {
            bdeMgr.setSpecificControlAttribute(i, values.get(i));
        }
    }

    // Mutable OAuth2 callback for in-memory token hot-swapping
    static class MutableOAuth2Callback implements OAuth2Callback {
        private volatile String bearerToken;

        public MutableOAuth2Callback(String initialToken) {
            this.bearerToken = initialToken;
        }

        public void setBearerToken(String token) {
            this.bearerToken = token;
        }

        @Override
        public String getBearerToken() {
            return this.bearerToken;
        }
    }

    // Managed JCA connection item
    static class ManagedConnection {
        Connection conn;
        JcaBdeManager bdeMgr;
        MutableOAuth2Callback oauthCallback;
        long lastUsedTime;

        ManagedConnection(Connection conn, JcaBdeManager bdeMgr, MutableOAuth2Callback cb) {
            this.conn = conn;
            this.bdeMgr = bdeMgr;
            this.oauthCallback = cb;
            this.lastUsedTime = System.currentTimeMillis();
        }

        void close() {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (Exception e) {
                // ignore close failure
            }
        }
    }

    // Daemon task for sequential FIFO queue
    static class DaemonTask {
        String jsonRpcRequest;
        CompletableFuture<String> futureResponse;

        DaemonTask(String req) {
            this.jsonRpcRequest = req;
            this.futureResponse = new CompletableFuture<>();
        }
    }

    // Persistent JCA Daemon Server
    public static class DaemonServer {
        private final int port;
        private final long idleTimeoutMillis;
        private final Map<String, ManagedConnection> connectionPool = new ConcurrentHashMap<>();
        private final BlockingQueue<DaemonTask> fifoQueue = new LinkedBlockingQueue<>();
        private volatile boolean running = true;
        private volatile long lastActivityTime = System.currentTimeMillis();
        private ServerSocket serverSocket;
        private Thread workerThread;
        private ScheduledExecutorService idleScheduler;

        public DaemonServer(int port, int idleTimeoutSeconds) {
            this.port = port;
            this.idleTimeoutMillis = (idleTimeoutSeconds > 0 ? idleTimeoutSeconds : 1800) * 1000L;
        }

        public void start() throws Exception {
            serverSocket = new ServerSocket(port, 50, InetAddress.getByName("127.0.0.1"));
            int boundPort = serverSocket.getLocalPort();
            long pid = ProcessHandle.current().pid();

            // Print DAEMON_READY line expected by client
            System.out.println("DAEMON_READY port=" + boundPort + " pid=" + pid);
            System.out.flush();

            // Start single-threaded sequential FIFO worker
            workerThread = new Thread(this::runWorker, "JcaDaemonWorker");
            workerThread.setDaemon(true);
            workerThread.start();

            // Start idle timeout check scheduler
            idleScheduler = Executors.newSingleThreadScheduledExecutor();
            idleScheduler.scheduleWithFixedDelay(this::checkIdleTimeout, 10, 10, TimeUnit.SECONDS);

            // Accept loop
            while (running) {
                try {
                    Socket socket = serverSocket.accept();
                    new Thread(() -> handleClientSocket(socket), "JcaClientHandler").start();
                } catch (Exception e) {
                    if (!running) {
                        break;
                    }
                }
            }
        }

        private void handleClientSocket(Socket socket) {
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
                 BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    line = line.trim();
                    if (line.isEmpty()) {
                        continue;
                    }
                    lastActivityTime = System.currentTimeMillis();
                    DaemonTask task = new DaemonTask(line);
                    fifoQueue.put(task);
                    String response = task.futureResponse.get();
                    writer.write(response);
                    writer.write("\n");
                    writer.flush();
                }
            } catch (Exception e) {
                // client disconnected
            }
        }

        private void runWorker() {
            while (running) {
                try {
                    DaemonTask task = fifoQueue.poll(1, TimeUnit.SECONDS);
                    if (task == null) {
                        continue;
                    }
                    lastActivityTime = System.currentTimeMillis();
                    String response = processJsonRpc(task.jsonRpcRequest);
                    task.futureResponse.complete(response);
                } catch (InterruptedException e) {
                    break;
                } catch (Exception e) {
                    // worker loop error
                }
            }
        }

        private String processJsonRpc(String reqStr) {
            String id = "1";
            try {
                // Minimal JSON parser for JSON-RPC 2.0 requests
                Map<String, Object> req = parseSimpleJson(reqStr);
                if (req.containsKey("id")) {
                    id = String.valueOf(req.get("id"));
                }
                String method = (String) req.get("method");
                @SuppressWarnings("unchecked")
                Map<String, Object> params = (Map<String, Object>) req.get("params");
                if (params == null) {
                    params = Collections.emptyMap();
                }

                if ("ping".equals(method)) {
                    return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"result\":{\"status\":\"ok\"}}";
                } else if ("status".equals(method)) {
                    long idleSec = (System.currentTimeMillis() - lastActivityTime) / 1000;
                    return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"result\":{" +
                        "\"status\":\"running\"," +
                        "\"active_connections\":" + connectionPool.size() + "," +
                        "\"idle_seconds\":" + idleSec + "," +
                        "\"pid\":" + ProcessHandle.current().pid() + "," +
                        "\"port\":" + serverSocket.getLocalPort() + "}}";
                } else if ("update_token".equals(method)) {
                    String newToken = (String) params.get("token");
                    if (newToken != null) {
                        for (ManagedConnection mc : connectionPool.values()) {
                            mc.oauthCallback.setBearerToken(newToken);
                        }
                    }
                    return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"result\":{\"status\":\"updated\"}}";
                } else if ("shutdown".equals(method)) {
                    new Thread(this::shutdown).start();
                    return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"result\":{\"status\":\"shutting_down\"}}";
                } else if ("execute_bde".equals(method)) {
                    return executeBdeRpc(id, params);
                } else {
                    return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"error\":{\"code\":-32601,\"message\":\"Method not found: " + method + "\"}}";
                }
            } catch (Exception e) {
                return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"error\":{\"code\":-32603,\"message\":\"" + escapeJson(e.getMessage()) + "\"}}";
            }
        }

        private String executeBdeRpc(String id, Map<String, Object> params) {
            String backend = (String) params.get("backend");
            String tenant = (String) params.get("tenant");
            String token = (String) params.get("token");
            String connectionPoint = (String) params.getOrDefault("connectionPoint", "ProjectServer");
            String bdeName = (String) params.get("bde");
            String methodName = (String) params.get("method");
            String reqXml = (String) params.getOrDefault("requestXml", "");
            String contextXml = (String) params.get("contextXml");
            String dispatchMode = (String) params.getOrDefault("mode", "BDE");
            int maxObjects = 0;
            if (params.containsKey("maxObjects")) {
                try {
                    maxObjects = Integer.parseInt(String.valueOf(params.get("maxObjects")));
                } catch (Exception ignored) {}
            }

            // Security guardrail check
            if (isProhibitedOperation(bdeName, methodName, reqXml)) {
                return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"error\":{\"code\":-32003,\"message\":\"[SECURITY_BLOCK] Prohibited operation (EndActivity/CloseTask blocked)\"}}";
            }

            try {
                ManagedConnection mc = getOrCreateConnection(backend, tenant, token, connectionPoint);
                JcaBdeManager bdeMgr = mc.bdeMgr;

                // Update token if newer token was provided
                if (token != null && !token.isEmpty()) {
                    mc.oauthCallback.setBearerToken(token);
                }

                // Set ActivityID context element in ControlArea
                if (contextXml != null && !contextXml.trim().isEmpty()) {
                    try {
                        DocumentBuilderFactory cDbf = DocumentBuilderFactory.newInstance();
                        cDbf.setNamespaceAware(true);
                        Document cDoc = cDbf.newDocumentBuilder().parse(new InputSource(new StringReader(contextXml)));
                        bdeMgr.setadditionalControlAreaElement(cDoc.getDocumentElement());
                    } catch (Exception e) {
                        System.err.println("[WARN] Failed to set ActivityID context element: " + e.getMessage());
                    }
                }

                try {
                    // Apply controlling attributes
                    @SuppressWarnings("unchecked")
                    Map<String, String> ctrlAttrs = (Map<String, String>) params.get("controllingAttributes");
                    if (ctrlAttrs != null && !ctrlAttrs.isEmpty()) {
                        applyControllingAttributes(bdeMgr, methodName, ctrlAttrs);
                    }

                    // Build selection
                    @SuppressWarnings("unchecked")
                    List<String> selectFields = (List<String>) params.get("selectionFields");
                    BdeSelection bdeSelection = null;
                    if (selectFields != null && !selectFields.isEmpty()) {
                        bdeSelection = bdeMgr.createBdeSelection();
                        for (String f : selectFields) {
                            bdeSelection.addSelection(f);
                        }
                    }

                    // Build filter
                    String filterExpr = (String) params.get("filterExpression");
                    BdeFilter bdeFilter = null;
                    if (filterExpr != null && !filterExpr.trim().isEmpty()) {
                        bdeFilter = bdeMgr.createBdeFilter();
                        BdeFilter.Expression expr = parseFilterExpression(bdeFilter, filterExpr);
                        if (expr != null) {
                            bdeFilter.setExpression(expr);
                        }
                    }

                    Element reqElement = null;
                    if (reqXml != null && !reqXml.isEmpty()) {
                        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                        dbf.setNamespaceAware(true);
                        Document doc = dbf.newDocumentBuilder().parse(new InputSource(new StringReader(reqXml)));
                        reqElement = doc.getDocumentElement();
                    }

                    String execMode = dispatchMode != null ? dispatchMode.toUpperCase(Locale.ROOT) : "BDE";
                    String xmlResp = "";

                    if ("LIST".equals(execMode) || "BROWSELIST".equals(execMode)) {
                        BdeElementIterator iter = bdeMgr.executeList(bdeName, methodName, bdeSelection, bdeFilter, maxObjects);
                        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                        dbf.setNamespaceAware(true);
                        Document outDoc = dbf.newDocumentBuilder().newDocument();
                        Element dataArea = outDoc.createElement("DataArea");
                        outDoc.appendChild(dataArea);
                        if (iter != null) {
                            while (iter.hasNext()) {
                                Element item = iter.nextElement();
                                if (item != null) {
                                    dataArea.appendChild(outDoc.importNode(item, true));
                                }
                            }
                        }
                        xmlResp = xmlToString(dataArea);
                    } else if ("SHOW".equals(execMode)) {
                        Element respElement = bdeMgr.executeShow(reqElement, methodName, bdeSelection, bdeFilter);
                        xmlResp = respElement != null ? xmlToString(respElement) : "<Success/>";
                    } else if ("SPECIALLIST".equals(execMode)) {
                        BdeElementIterator iter = bdeMgr.executeSpecialList(bdeName, methodName, bdeSelection, reqElement);
                        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                        dbf.setNamespaceAware(true);
                        Document outDoc = dbf.newDocumentBuilder().newDocument();
                        Element dataArea = outDoc.createElement("DataArea");
                        outDoc.appendChild(dataArea);
                        if (iter != null) {
                            while (iter.hasNext()) {
                                Element item = iter.nextElement();
                                if (item != null) {
                                    dataArea.appendChild(outDoc.importNode(item, true));
                                }
                            }
                        }
                        xmlResp = xmlToString(dataArea);
                    } else {
                        Element respElement = null;
                        if (reqElement != null) {
                            respElement = bdeMgr.executeMethod(reqElement, methodName);
                        } else {
                            respElement = bdeMgr.doBdeCall(bdeName, methodName, null);
                        }
                        xmlResp = respElement != null ? xmlToString(respElement) : "<Success/>";
                    }

                    return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"result\":{\"xml\":\"" + escapeJson(xmlResp) + "\"}}";
                } finally {
                    // Always clear context element in ControlArea after execution
                    try {
                        bdeMgr.setadditionalControlAreaElement(null);
                    } catch (Exception ignored) {}
                }
            } catch (Exception e) {
                return "{\"jsonrpc\":\"2.0\",\"id\":" + id + ",\"error\":{\"code\":-32000,\"message\":\"" + escapeJson(e.getMessage()) + "\"}}";
            }
        }

        private synchronized ManagedConnection getOrCreateConnection(String backend, String tenant, String token, String connectionPoint) throws Exception {
            String key = (backend != null ? backend : "") + "|" + (tenant != null ? tenant : "") + "|" + (connectionPoint != null ? connectionPoint : "ProjectServer");
            ManagedConnection mc = connectionPool.get(key);
            if (mc != null) {
                mc.lastUsedTime = System.currentTimeMillis();
                return mc;
            }

            MutableOAuth2Callback cb = new MutableOAuth2Callback(token);
            ConnectionSpecImpl spec = new ConnectionSpecImpl();
            spec.setApplication("LNStudio");
            spec.setActivationType("http_oauth2");
            spec.setTenant(tenant);

            String host = backend;
            if (host != null && !host.endsWith("/LN/webservice")) {
                if (host.endsWith("/")) {
                    host = host.substring(0, host.length() - 1);
                }
                host = host + "/" + tenant + "/LN/webservice";
            }
            spec.setBackend(host);
            spec.setApplication("LN");
            spec.setOAuth2Callback(cb);

            if (connectionPoint != null && !connectionPoint.isEmpty()) {
                try {
                    spec.setConnectionPoint(connectionPoint);
                } catch (Exception e) {
                    System.err.println("[WARN] setConnectionPoint failed: " + e.getMessage());
                }
            }

            ConnectionFactoryImpl factory = new ConnectionFactoryImpl();
            try {
                File tempCpFile = File.createTempFile("ln_connectionpoints_", ".xml");
                tempCpFile.deleteOnExit();
                String cpXml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                    + "<connectionpoints>\n"
                    + "  <connectionpoint name=\"ProjectServer\" hostname=\"" + host + "\" port=\"0\" timerdelay=\"0\" maxconnections=\"1\" maxreferences=\"-1\" maxthreads=\"0\" forcecleanup=\"true\">\n"
                    + "    <activation type=\"http_oauth2\" bse=\"\" bshell=\"\" tenant=\"" + tenant + "\"/>\n"
                    + "  </connectionpoint>\n"
                    + (connectionPoint != null && !connectionPoint.isEmpty() && !"ProjectServer".equals(connectionPoint)
                        ? "  <alias name=\"" + connectionPoint + "\" linkto=\"ProjectServer\"/>\n" : "")
                    + "</connectionpoints>\n";
                try (FileWriter fw = new FileWriter(tempCpFile)) {
                    fw.write(cpXml);
                }
                factory.setLocation(tempCpFile.getAbsolutePath());
            } catch (Exception e) {
                System.err.println("[WARN] Failed to configure connectionpoints XML: " + e.getMessage());
            }

            Connection conn = factory.getConnection(spec);
            JcaBdeManager bdeMgr = new JcaBdeManager(conn);
            mc = new ManagedConnection(conn, bdeMgr, cb);
            connectionPool.put(key, mc);
            return mc;
        }

        private void checkIdleTimeout() {
            if (System.currentTimeMillis() - lastActivityTime > idleTimeoutMillis) {
                System.err.println("[INFO] JCA Daemon idle for " + (idleTimeoutMillis / 1000) + "s. Shutting down.");
                shutdown();
            }
        }

        public void shutdown() {
            running = false;
            for (ManagedConnection mc : connectionPool.values()) {
                mc.close();
            }
            connectionPool.clear();
            if (idleScheduler != null) {
                idleScheduler.shutdownNow();
            }
            try {
                if (serverSocket != null) {
                    serverSocket.close();
                }
            } catch (Exception ignored) {}
            System.exit(0);
        }
    }

    private static String escapeJson(String s) {
        if (s == null) return "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '"') sb.append("\\\"");
            else if (c == '\\') sb.append("\\\\");
            else if (c == '\b') sb.append("\\b");
            else if (c == '\f') sb.append("\\f");
            else if (c == '\n') sb.append("\\n");
            else if (c == '\r') sb.append("\\r");
            else if (c == '\t') sb.append("\\t");
            else if (c < 0x20) sb.append(String.format("\\u%04x", (int) c));
            else sb.append(c);
        }
        return sb.toString();
    }

    private static Map<String, Object> parseSimpleJson(String jsonStr) {
        Map<String, Object> map = new HashMap<>();
        String s = jsonStr.trim();
        if (!s.startsWith("{") || !s.endsWith("}")) {
            return map;
        }
        s = s.substring(1, s.length() - 1).trim();

        // Parse key-value pairs top-level
        int len = s.length();
        int i = 0;
        while (i < len) {
            // Find key
            while (i < len && (s.charAt(i) == ' ' || s.charAt(i) == ',' || s.charAt(i) == '\n' || s.charAt(i) == '\r' || s.charAt(i) == '\t')) i++;
            if (i >= len) break;
            if (s.charAt(i) != '"') break;
            int keyStart = ++i;
            while (i < len && s.charAt(i) != '"') {
                if (s.charAt(i) == '\\') i++;
                i++;
            }
            String key = s.substring(keyStart, i);
            i++; // skip closing quote
            while (i < len && s.charAt(i) != ':') i++;
            i++; // skip colon
            while (i < len && (s.charAt(i) == ' ' || s.charAt(i) == '\t')) i++;
            if (i >= len) break;

            char valChar = s.charAt(i);
            if (valChar == '"') {
                int valStart = ++i;
                StringBuilder valSb = new StringBuilder();
                while (i < len && s.charAt(i) != '"') {
                    if (s.charAt(i) == '\\' && i + 1 < len) {
                        i++;
                        char esc = s.charAt(i);
                        if (esc == 'n') valSb.append('\n');
                        else if (esc == 'r') valSb.append('\r');
                        else if (esc == 't') valSb.append('\t');
                        else if (esc == '"') valSb.append('"');
                        else if (esc == '\\') valSb.append('\\');
                        else valSb.append(esc);
                    } else {
                        valSb.append(s.charAt(i));
                    }
                    i++;
                }
                i++; // skip quote
                map.put(key, valSb.toString());
            } else if (valChar == '{') {
                int objStart = i;
                int depth = 0;
                while (i < len) {
                    if (s.charAt(i) == '{') depth++;
                    else if (s.charAt(i) == '}') {
                        depth--;
                        if (depth == 0) { i++; break; }
                    } else if (s.charAt(i) == '"') {
                        i++;
                        while (i < len && s.charAt(i) != '"') {
                            if (s.charAt(i) == '\\') i++;
                            i++;
                        }
                    }
                    i++;
                }
                String subJson = s.substring(objStart, i);
                map.put(key, parseSimpleJson(subJson));
            } else if (valChar == '[') {
                int arrStart = i;
                int depth = 0;
                while (i < len) {
                    if (s.charAt(i) == '[') depth++;
                    else if (s.charAt(i) == ']') {
                        depth--;
                        if (depth == 0) { i++; break; }
                    } else if (s.charAt(i) == '"') {
                        i++;
                        while (i < len && s.charAt(i) != '"') {
                            if (s.charAt(i) == '\\') i++;
                            i++;
                        }
                    }
                    i++;
                }
                String subArr = s.substring(arrStart, i);
                List<String> list = new ArrayList<>();
                String inner = subArr.substring(1, subArr.length() - 1).trim();
                if (!inner.isEmpty()) {
                    String[] tokens = inner.split(",");
                    for (String t : tokens) {
                        String clean = t.trim();
                        if (clean.startsWith("\"") && clean.endsWith("\"") && clean.length() >= 2) {
                            clean = clean.substring(1, clean.length() - 1);
                        }
                        list.add(clean);
                    }
                }
                map.put(key, list);
            } else {
                int valStart = i;
                while (i < len && s.charAt(i) != ',' && s.charAt(i) != '}') i++;
                String rawVal = s.substring(valStart, i).trim();
                map.put(key, rawVal);
            }
        }
        return map;
    }

    public static void main(String[] args) {
        boolean isDaemon = false;
        int daemonPort = 0;
        int idleTimeout = 1800;

        String cliAction = "";
        String dispatchMode = "BDE";
        String backend = "";
        String tenant = "";
        String token = "";
        String bdeName = "";
        String methodName = "";
        String connectionPoint = "ProjectServer";
        String contextXml = "";
        String filterExpr = null;
        int maxObjects = 0;
        List<String> selectionFields = new ArrayList<>();
        Map<String, String> controllingAttrs = new LinkedHashMap<>();

        for (int i = 0; i < args.length; i++) {
            if ("--daemon".equals(args[i])) {
                isDaemon = true;
            } else if ("--port".equals(args[i]) && i + 1 < args.length) {
                try { daemonPort = Integer.parseInt(args[++i]); } catch (Exception ignored) {}
            } else if ("--idle-timeout".equals(args[i]) && i + 1 < args.length) {
                try { idleTimeout = Integer.parseInt(args[++i]); } catch (Exception ignored) {}
            } else if ("--ping".equals(args[i])) {
                cliAction = "ping";
            } else if ("--backend".equals(args[i]) && i + 1 < args.length) {
                backend = args[++i];
            } else if ("--tenant".equals(args[i]) && i + 1 < args.length) {
                tenant = args[++i];
            } else if ("--token".equals(args[i]) && i + 1 < args.length) {
                token = args[++i];
            } else if ("--bde".equals(args[i]) && i + 1 < args.length) {
                bdeName = args[++i];
                cliAction = "bde";
            } else if ("--method".equals(args[i]) && i + 1 < args.length) {
                methodName = args[++i];
            } else if ("--cp".equals(args[i]) && i + 1 < args.length) {
                connectionPoint = args[++i];
            } else if (("--context".equals(args[i]) || "--context-xml".equals(args[i])) && i + 1 < args.length) {
                contextXml = args[++i];
            } else if ("--mode".equals(args[i]) && i + 1 < args.length) {
                dispatchMode = args[++i].toUpperCase(Locale.ROOT);
            } else if ("--ctrl-attr".equals(args[i]) && i + 1 < args.length) {
                String pair = args[++i];
                int eq = pair.indexOf('=');
                if (eq > 0) {
                    controllingAttrs.put(pair.substring(0, eq).trim(), pair.substring(eq + 1).trim());
                }
            } else if ("--select".equals(args[i]) && i + 1 < args.length) {
                String[] fields = args[++i].split(",");
                for (String f : fields) {
                    if (!f.trim().isEmpty()) {
                        selectionFields.add(f.trim());
                    }
                }
            } else if ("--filter".equals(args[i]) && i + 1 < args.length) {
                filterExpr = args[++i];
            } else if ("--max-objects".equals(args[i]) && i + 1 < args.length) {
                try { maxObjects = Integer.parseInt(args[++i]); } catch (NumberFormatException e) { maxObjects = 0; }
            }
        }

        if (isDaemon) {
            try {
                DaemonServer daemon = new DaemonServer(daemonPort, idleTimeout);
                daemon.start();
            } catch (Exception e) {
                System.err.println("[ERROR] Failed to start JCA daemon: " + e.getMessage());
                e.printStackTrace(System.err);
                System.exit(1);
            }
            return;
        }

        try {
            // Read stdin early in BDE mode so we can inspect both methodName and XML payload BEFORE connecting
            String reqXml = "";
            if ("bde".equals(cliAction)) {
                if (isProhibitedOperation(bdeName, methodName, "")) {
                    System.err.println(
                        "[SECURITY_BLOCK] Protocol-level guardrail (ADR 0008): Operation '" +
                        bdeName + "." + methodName + "' (EndActivity/CloseTask) is physically removed from LNStudioJcaBridge. " +
                        "Use 'prepare-end-activity' for read-only verification and close the activity manually in LN Studio."
                    );
                    System.exit(3);
                }

                if (System.in.available() > 0 || !"ping".equals(cliAction)) {
                    StringBuilder sb = new StringBuilder();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
                    String line;
                    while ((line = reader.readLine()) != null) {
                        sb.append(line).append("\n");
                    }
                    reqXml = sb.toString().trim();
                }

                if (isProhibitedOperation(bdeName, methodName, reqXml)) {
                    System.err.println(
                        "[SECURITY_BLOCK] Protocol-level guardrail (ADR 0008): XML payload attempting EndActivity/CloseTask/Deliver " +
                        "is physically blocked by LNStudioJcaBridge."
                    );
                    System.exit(3);
                }
            }

            final String bearerToken = token;
            ConnectionSpecImpl spec = new ConnectionSpecImpl();
            spec.setApplication("LNStudio");
            spec.setActivationType("http_oauth2");
            spec.setTenant(tenant);

            String host = backend;
            if (host != null && !host.endsWith("/LN/webservice")) {
                if (host.endsWith("/")) {
                    host = host.substring(0, host.length() - 1);
                }
                host = host + "/" + tenant + "/LN/webservice";
            }
            spec.setBackend(host);
            spec.setApplication("LN");

            spec.setOAuth2Callback(new OAuth2Callback() {
                @Override
                public String getBearerToken() {
                    return bearerToken;
                }
            });

            if (connectionPoint != null && !connectionPoint.isEmpty()) {
                try {
                    spec.setConnectionPoint(connectionPoint);
                } catch (Exception e) {
                    System.err.println("[WARN] setConnectionPoint failed: " + e.getMessage());
                }
            }

            ConnectionFactoryImpl factory = new ConnectionFactoryImpl();
            try {
                File tempCpFile = File.createTempFile("ln_connectionpoints_", ".xml");
                tempCpFile.deleteOnExit();
                String cpXml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                    + "<connectionpoints>\n"
                    + "  <connectionpoint name=\"ProjectServer\" hostname=\"" + host + "\" port=\"0\" timerdelay=\"0\" maxconnections=\"1\" maxreferences=\"-1\" maxthreads=\"0\" forcecleanup=\"true\">\n"
                    + "    <activation type=\"http_oauth2\" bse=\"\" bshell=\"\" tenant=\"" + tenant + "\"/>\n"
                    + "  </connectionpoint>\n"
                    + (connectionPoint != null && !connectionPoint.isEmpty() && !"ProjectServer".equals(connectionPoint)
                        ? "  <alias name=\"" + connectionPoint + "\" linkto=\"ProjectServer\"/>\n" : "")
                    + "</connectionpoints>\n";
                try (FileWriter fw = new FileWriter(tempCpFile)) {
                    fw.write(cpXml);
                }
                factory.setLocation(tempCpFile.getAbsolutePath());
            } catch (Exception e) {
                System.err.println("[WARN] Failed to configure connectionpoints XML: " + e.getMessage());
            }

            Connection conn = factory.getConnection(spec);
            JcaBdeManager bdeMgr = new JcaBdeManager(conn);

            if (contextXml != null && !contextXml.trim().isEmpty()) {
                try {
                    DocumentBuilderFactory cDbf = DocumentBuilderFactory.newInstance();
                    cDbf.setNamespaceAware(true);
                    Document cDoc = cDbf.newDocumentBuilder().parse(new InputSource(new StringReader(contextXml)));
                    bdeMgr.setadditionalControlAreaElement(cDoc.getDocumentElement());
                } catch (Exception e) {
                    System.err.println("[WARN] Failed to set ActivityID context element: " + e.getMessage());
                }
            }

            if ("ping".equals(cliAction)) {
                bdeMgr.ping();
                System.out.println("PING_OK");
                conn.close();
                System.exit(0);
            } else if ("bde".equals(cliAction)) {
                // Apply controlling attributes if provided
                if (!controllingAttrs.isEmpty()) {
                    applyControllingAttributes(bdeMgr, methodName, controllingAttrs);
                }

                // Build BdeSelection if fields provided
                BdeSelection bdeSelection = null;
                if (!selectionFields.isEmpty()) {
                    bdeSelection = bdeMgr.createBdeSelection();
                    for (String f : selectionFields) {
                        bdeSelection.addSelection(f);
                    }
                }

                // Build BdeFilter if expression provided
                BdeFilter bdeFilter = null;
                if (filterExpr != null && !filterExpr.trim().isEmpty()) {
                    bdeFilter = bdeMgr.createBdeFilter();
                    BdeFilter.Expression expr = parseFilterExpression(bdeFilter, filterExpr);
                    if (expr != null) {
                        bdeFilter.setExpression(expr);
                    }
                }

                Element reqElement = null;
                if (!reqXml.isEmpty()) {
                    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                    dbf.setNamespaceAware(true);
                    DocumentBuilder db = dbf.newDocumentBuilder();
                    Document doc = db.parse(new InputSource(new StringReader(reqXml)));
                    reqElement = doc.getDocumentElement();
                }

                String execMode = dispatchMode.toUpperCase(Locale.ROOT);
                if ("LIST".equals(execMode) || "BROWSELIST".equals(execMode)) {
                    BdeElementIterator iter = bdeMgr.executeList(bdeName, methodName, bdeSelection, bdeFilter, maxObjects);
                    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                    dbf.setNamespaceAware(true);
                    Document outDoc = dbf.newDocumentBuilder().newDocument();
                    Element dataArea = outDoc.createElement("DataArea");
                    outDoc.appendChild(dataArea);
                    if (iter != null) {
                        while (iter.hasNext()) {
                            Element item = iter.nextElement();
                            if (item != null) {
                                dataArea.appendChild(outDoc.importNode(item, true));
                            }
                        }
                    }
                    printXml(dataArea);
                } else if ("SHOW".equals(execMode)) {
                    Element respElement = bdeMgr.executeShow(reqElement, methodName, bdeSelection, bdeFilter);
                    if (respElement != null) {
                        printXml(respElement);
                    } else {
                        System.out.print("<Success/>");
                    }
                } else if ("SPECIALLIST".equals(execMode)) {
                    BdeElementIterator iter = bdeMgr.executeSpecialList(bdeName, methodName, bdeSelection, reqElement);
                    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                    dbf.setNamespaceAware(true);
                    Document outDoc = dbf.newDocumentBuilder().newDocument();
                    Element dataArea = outDoc.createElement("DataArea");
                    outDoc.appendChild(dataArea);
                    if (iter != null) {
                        while (iter.hasNext()) {
                            Element item = iter.nextElement();
                            if (item != null) {
                                dataArea.appendChild(outDoc.importNode(item, true));
                            }
                        }
                    }
                    printXml(dataArea);
                } else {
                    Element respElement = null;
                    if (reqElement != null) {
                        respElement = bdeMgr.executeMethod(reqElement, methodName);
                    } else {
                        respElement = bdeMgr.doBdeCall(bdeName, methodName, null);
                    }
                    if (respElement != null) {
                        printXml(respElement);
                    } else {
                        System.out.print("<Success/>");
                    }
                }

                conn.close();
                System.exit(0);
            } else {
                System.err.println("Unknown mode. Specify --daemon, --ping, or --bde <name> --method <method>");
                System.exit(1);
            }
        } catch (Exception e) {
            System.err.println("[ERROR] JCA Bridge exception: " + e.getMessage());
            e.printStackTrace(System.err);
            System.exit(2);
        }
    }
}
