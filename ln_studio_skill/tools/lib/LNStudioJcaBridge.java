import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
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
 * Supports 5 BdeManager execution modes:
 * - LIST (0): executeList wrapped in <DataArea>
 * - SHOW (1): executeShow
 * - BDE (2): executeMethod / doBdeCall
 * - SPECIALLIST (3): executeSpecialList wrapped in <DataArea>
 * - BROWSELIST (4): executeList with controlling attributes wrapped in <DataArea>
 *
 * Protocol-Level Safety Guarantee (ADR 0007 / ADR 0008 / ADR 0012):
 * Execution of EndActivity, CloseTask, FinalizeActivity, or Deliver is physically blocked
 * at the Java bridge layer before any JCA connection or BDE call can occur.
 * Only read-only verification (ValidateDevelopmentActivity / executeVSC) is permitted
 * for prepare-end-activity.
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

    /**
     * Enforces protocol-level removal of EndActivity / CloseTask / FinalizeActivity.
     */
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

    private static void printXml(Element elem) throws Exception {
        TransformerFactory tf = TransformerFactory.newInstance();
        Transformer transformer = tf.newTransformer();
        transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        StringWriter writer = new StringWriter();
        transformer.transform(new DOMSource(elem), new StreamResult(writer));
        System.out.print(writer.toString());
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

    public static void main(String[] args) {
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
            if ("--ping".equals(args[i])) {
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
                try {
                    maxObjects = Integer.parseInt(args[++i]);
                } catch (NumberFormatException e) {
                    maxObjects = 0;
                }
            }
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
            if (!host.endsWith("/LN/webservice")) {
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
                    // Mode 0 (LIST) and Mode 4 (BROWSELIST)
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
                    // Mode 1 (SHOW)
                    Element respElement = bdeMgr.executeShow(reqElement, methodName, bdeSelection, bdeFilter);
                    if (respElement != null) {
                        printXml(respElement);
                    } else {
                        System.out.print("<Success/>");
                    }
                } else if ("SPECIALLIST".equals(execMode)) {
                    // Mode 3 (SPECIALLIST)
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
                    // Default Mode 2 (BDE)
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

                if (bdeMgr.hasInformation()) {
                    try {
                        com.infor.erpln.jca.bdeclient.BdeMessageIterator iter = bdeMgr.getInformation();
                        StringBuilder infoSb = new StringBuilder();
                        while (iter.hasMoreElements()) {
                            com.infor.erpln.jca.bdeclient.BdeMessage msg = iter.nextElement();
                            infoSb.append(msg.getMessageText()).append("\n");
                        }
                        if (infoSb.length() > 0) {
                            System.err.println("[BDE_INFORMATION] " + infoSb.toString().trim());
                        }
                    } catch (Exception e) {
                        // ignore information logging failure
                    }
                }

                conn.close();
                System.exit(0);
            } else {
                System.err.println("Unknown mode. Specify --ping or --bde <name> --method <method>");
                System.exit(1);
            }
        } catch (Exception e) {
            System.err.println("[ERROR] JCA Bridge exception: " + e.getMessage());
            e.printStackTrace(System.err);
            System.exit(2);
        }
    }
}
