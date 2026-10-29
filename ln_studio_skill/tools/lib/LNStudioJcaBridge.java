import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Locale;
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
import com.infor.erpln.jca.bdeclient.JcaBdeManager;

/**
 * LNStudioJcaBridge
 * Headless Infor LN JCA 1.6 Bridge for automated BDE execution, explorers, and SCM.
 *
 * Protocol-Level Safety Guarantee (ADR 0007 / ADR 0008):
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

    public static void main(String[] args) {
        String mode = "";
        String backend = "";
        String tenant = "";
        String token = "";
        String bdeName = "";
        String methodName = "";
        String connectionPoint = "ProjectServer";
        String contextXml = "";

        for (int i = 0; i < args.length; i++) {
            if ("--ping".equals(args[i])) {
                mode = "ping";
            } else if ("--backend".equals(args[i]) && i + 1 < args.length) {
                backend = args[++i];
            } else if ("--tenant".equals(args[i]) && i + 1 < args.length) {
                tenant = args[++i];
            } else if ("--token".equals(args[i]) && i + 1 < args.length) {
                token = args[++i];
            } else if ("--bde".equals(args[i]) && i + 1 < args.length) {
                bdeName = args[++i];
                mode = "bde";
            } else if ("--method".equals(args[i]) && i + 1 < args.length) {
                methodName = args[++i];
            } else if ("--cp".equals(args[i]) && i + 1 < args.length) {
                connectionPoint = args[++i];
            } else if (("--context".equals(args[i]) || "--context-xml".equals(args[i])) && i + 1 < args.length) {
                contextXml = args[++i];
            }
        }

        try {
            // Read stdin early in BDE mode so we can inspect both methodName and XML payload BEFORE connecting
            String reqXml = "";
            if ("bde".equals(mode)) {
                if (isProhibitedOperation(bdeName, methodName, "")) {
                    System.err.println(
                        "[SECURITY_BLOCK] Protocol-level guardrail (ADR 0008): Operation '" +
                        bdeName + "." + methodName + "' (EndActivity/CloseTask) is physically removed from LNStudioJcaBridge. " +
                        "Use 'prepare-end-activity' for read-only verification and close the activity manually in LN Studio."
                    );
                    System.exit(3);
                }

                if (System.in.available() > 0 || !"ping".equals(mode)) {
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

            if ("ping".equals(mode)) {
                bdeMgr.ping();
                System.out.println("PING_OK");
                conn.close();
                System.exit(0);
            } else if ("bde".equals(mode)) {
                Element reqElement = null;
                if (!reqXml.isEmpty()) {
                    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                    dbf.setNamespaceAware(true);
                    DocumentBuilder db = dbf.newDocumentBuilder();
                    Document doc = db.parse(new InputSource(new StringReader(reqXml)));
                    reqElement = doc.getDocumentElement();
                }

                Element respElement = null;
                if (reqElement != null) {
                    respElement = bdeMgr.executeMethod(reqElement, methodName);
                } else {
                    respElement = bdeMgr.doBdeCall(bdeName, methodName, null);
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

                if (respElement != null) {
                    TransformerFactory tf = TransformerFactory.newInstance();
                    Transformer transformer = tf.newTransformer();
                    transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
                    transformer.setOutputProperty(OutputKeys.INDENT, "yes");
                    StringWriter writer = new StringWriter();
                    transformer.transform(new DOMSource(respElement), new StreamResult(writer));
                    System.out.print(writer.toString());
                } else {
                    System.out.print("<Success/>");
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
