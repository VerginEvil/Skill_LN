# client.show.file

## Syntax:
`#include <bic_desktop>`
`function long client.show.file( string source, boolean new.window, string title, [ string mime.type, string target, boolean remove.after.download ] )`

## Description
Show the server file passed in the source argument in the browser. The browser can show some file types natively in a browser window (like for example plain text and pdf files). For other file types, the browser will show a browser specific download dialog.
This function will return immediately (so will not wait until the browser window is closed or the file downloaded by the client). The optional parameter "remove.after.download" can be used to control automatic removal of the server file after the file has been downloaded by the client.
Conversion of CRLF characters is only done for text files (file extension .txt or mime.type "text/plain"). All other file types are copied in binary mode.
The mime.type can be used to indicate the file type such that the browser has the option to start the client application which is associated with this mime.type. When the mime.type is not specified, the mime.type will be determined based on the file extension of the file specified in the optional target argument. When the optional target argument is also not specified, the mime.type will be determined based on the file extension of the file specified in the source argument.
When this function is called more than once for a single UI event, only the last function call will be effective.
In case of a Document Viewer session this function may only be called after calling vwr.init() or from callback function vwr.bms.received(). In case of a Document Viewer session the following arguments are ignored: new.window, title.
This function is only supported in WebUI and LN UI.

## Arguments
| | | |
|---|---|---|
| `string` | `source` |  Specifies the server file which must be shown in the browser.  |
| `boolean` | `new.window` |  When this option is true, the server file is shown in a new browser window. Otherwise this file is shown in a frame embedded in the current browser window.  |
| `string` | `title` |  Specifies the title for the browser window or frame.  |
| `[ string` | `mime.type ]` |  This optional argument can be used to indicate the file type such that the browser has the option to start the plugin which is associated with this mime.type. When the mime.type is not specified, the mime.type will be determined based on the file extension of the file specified in the source argument.  |
| `[ string` | `target ]` |  optional string representing the proposed file name on the client  |
| `[ boolean` | `remove.after.download ]` |  When this optional argument is true, the file on the server is automatically removed after the file is downloaded by the client. The default value is false.  |

## Return values
| | |
|---|---|
| 0 | success |
| < 0 | when an error occurred (for instance invalid source path) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
