import java.io.*;
import java.nio.charset.StandardCharsets;
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
 */
public class LNStudioJcaBridge {

    public static void main(String[] args) {
        String mode = "";
        String backend = "";
        String tenant = "";
        String token = "";
        String bdeName = "";
        String methodName = "";
        String connectionPoint = "ProjectServer";

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
            }
        }

        try {
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

            spec.setOAuth2Callback(new OAuth2Callback() {
                @Override
                public String getBearerToken() {
                    return bearerToken;
                }
            });

            ConnectionFactoryImpl factory = new ConnectionFactoryImpl();
            Connection conn = factory.getConnection(spec);
            JcaBdeManager bdeMgr = new JcaBdeManager(conn);

            if ("ping".equals(mode)) {
                bdeMgr.ping();
                System.out.println("PING_OK");
                conn.close();
                System.exit(0);
            } else if ("bde".equals(mode)) {
                // Read request XML from stdin
                StringBuilder sb = new StringBuilder();
                BufferedReader reader = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
                String line;
                while ((line = reader.readLine()) != null) {
                    sb.append(line).append("\n");
                }
                String reqXml = sb.toString().trim();

                Element reqElement = null;
                if (!reqXml.isEmpty()) {
                    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                    dbf.setNamespaceAware(true);
                    DocumentBuilder db = dbf.newDocumentBuilder();
                    Document doc = db.parse(new InputSource(new StringReader(reqXml)));
                    reqElement = doc.getDocumentElement();
                }

                Element respElement = bdeMgr.doBdeCall(bdeName, methodName, reqElement);

                // Serialize response element to stdout
                TransformerFactory tf = TransformerFactory.newInstance();
                Transformer transformer = tf.newTransformer();
                transformer.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
                transformer.setOutputProperty(OutputKeys.INDENT, "yes");
                StringWriter writer = new StringWriter();
                transformer.transform(new DOMSource(respElement), new StreamResult(writer));

                System.out.print(writer.toString());
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
