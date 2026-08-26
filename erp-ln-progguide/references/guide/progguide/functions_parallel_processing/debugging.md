# Parallel Application Processing Debugging
By default the server processes run in a Bshell without a UI. This is a Bshell started with the –server option. For debugging the server side application, a server Bshell can be started through a new BW instance. This allows you to debug the server side application in the classic Bshell debugger. To enable this mode, take the following steps:
- Set environment variable DS_AS to value "bw" (-set DS_AS=bw) for the client Bshell
- In BECS on the client system, mark the correct .bwc file as the "default"  From Enterprise Server 8.7 onwards, debugging of Parallel Processing Applications is also supported by the Application Studio. See the application studio documentation for a description of this feature.

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
