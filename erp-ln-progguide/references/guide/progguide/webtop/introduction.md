# WebUI and LN UI Programming Rules
WebUI and LN UI speak a different "language" (protocol) with the 4GL Engine than BW does. The reason for this is that Web-based clients (like WebUI and LN UI) use a different network topology than fat clients (like BW). The network connection between the BW client and the Infor Enterprise Server allows the 4GL Engine to initiate requests to the BW client in order to draw things on the screen (see picture).
A Web-based network topology does not allow the server to initiate requests to the client (browser). The HTTP protocol does not allow this (see picture).
Because of this restriction WebUI and LN UI use a different protocol with the 4GL Engine.
Since not all API's (especially low-level BW API's) are suitable to fit into this protocol, some API's are deprecated.
A general rule of thumb is that 4GL Sessions, GBF Sessions and sessions based on Programmable Dialogs can (with slight modifications) be run in WebUI and LN UI. In general 3GL sessions which have a User Interface cannot be run in WebUI and LN UI. 3GL-Session which do not have a User Interface and which run in the background, should use the function [tc.ignore.process()](../functions_webtop/tc.ignore.process.md) to run correctly in WebUI and LN UI.

## The following sections describe the deprecated API's:
- [Deprecated low-level UI drawing API's](lowlevel_ui.md)
- [Baan Automation is deprecated](baan_automation.md)
- [Other deprecated predefined variables / functions](other_deprecated.md)

## The following sections describe other attention points:
- [Functions that should be used with caution](caution.md)
- [Some notes on the Generic Browser Framework (GBF)](gbf_notes.md)
- [Exiting 3gl and messages](exiting_3gl.md)
- [Using a Progress Indicator](progress_indicator.md)
