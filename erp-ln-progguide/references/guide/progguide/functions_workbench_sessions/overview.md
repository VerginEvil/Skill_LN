# Workbench Sessions overview
Workbench sessions are sessions which are used to launch a Workbench application which runs outside the WebUI or LN UI. The UI of such a session is rendered as a normal session inside the WebUI or LN UI. Workbench sessions are only supported when running inside the Infor Workspace or Ming.le portal. The first generation of Workbench UI's is implemented using Silverlight. The next generation of Workbench UI's is based on the Infor Workbench SDK. The Infor Workbench SDK is used to create a HTML5 based Workbench.
For each Workbench Application one Workbench session (also known as desk session) is running on the Infor Enterprise Server server. A Workbench session must have the following characteristics:
- Related script type: 3GL (Without 4GL Engine)
- No related form must be created
- By default, the session Description will become the title in the title bar of the Workbench Application (similar to normal sessions)   The related 3GL Script must include bic_desk and must implement the main() function. In this main function a call must be done to the function: start.ext.desk().

## Related topics
- [Workbench Sessions synopsis](synopsis.md)
