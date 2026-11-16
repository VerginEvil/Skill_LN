# Document Viewer overview
Session type by which documents can be viewed
The client side browser will be used to render the content of the document. The mime-type of the document will be used by the browser to decide how to view the document. When the browser cannot render a specific mime-type, the browser will show a (browser specific) dialog typically asking the user what to do with the document. For example: save, save as or open. When the user choses open, another client side application related to the file extension will be started. This feature will only become available for Swing WebUI and LN UI and not for Worktop.
A Document viewer session must have the following characteristics:

- Related script type: 3GL (Without 4GL Engine)

- No related form must be created

- The 3GL Script must include bic_vwr and must implement the main() function. In this main function a call must be done to the functions: vwr.init() and vwr.start().

For sending an update message from a navigation session to a viewer session, the PRCM mechanism can be used.

## Related topics
- [Document Viewer synopsis](synopsis.md)

- [Document Viewer example](example.md)

- [client.show.file](../functions_client_file_access/client.show.file.md)

- [client.show.url](../functions_client_file_access/client.show.url.md)
