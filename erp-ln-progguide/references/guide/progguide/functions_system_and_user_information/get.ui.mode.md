# get.ui.mode()

## Syntax:
`function long get.ui.mode( )`

## Description
This returns a long value that indicates the UI mode in which this session is running. The possible values are:
| | |
|---|---|
| NO_UI | without a User Interface |
| BW_UI | UI is bw client |
| WEBUI_CLASSIC | UI is thin-client in classic mode |
| WEBUI_COMMONUI | UI is thin-client in commonUI mode |
| HTML_UI | UI is thin-client running in HTMLUI mode (LN UI) |
| SOHO_XI | UI is thin-client running in SoHo Xi mode |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1900](../tiv/tiv_1900.md).

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
