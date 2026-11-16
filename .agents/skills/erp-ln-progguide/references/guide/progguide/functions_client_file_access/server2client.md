# server2client()

## Syntax:
`#include <bic_desktop>`
`function long server2client( string source, string dest, boolean text.mode, [ boolean progress.window, boolean read.only ] )`

## Description
*Deprecated.* This copies a specified file from the server to the client.

## Arguments
| | | |
|---|---|---|
| `string` | `source` |  The source file name, on the server.  |
| `string` | `dest` |  The destination file name, on the client. When this is an empty string, this function will show the file save-as dialog through which the user can select an existing file or enter the name of a new file on the client. The function [get.local.filename()](get.local.filename.md) can be used afterwards to retrieve the actual filename on the client to which the file was copied. The dest parameter may include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |
| `boolean` | `text.mode` |  This argument specifies whether the file is to be copied in text or binary mode: true text mode false binary mode  |
| `[ boolean` | `progress.window ]` |  Use this optional argument to specify whether a progress indicator must be displayed to indicate the progress of the copy action: true progress indicator is displayed false progress indicator is not displayed this is the default  |
| `[ boolean` | `read.only ]` |  When creating a file on the client side, this attribute can be used to set the file attributes to readonly mode after the file has been transferred. true file is set to readonly mode false file remains in read/write mode this is the default  |

## Return values
| | |
|---|---|
| 0 | File copy success. |
| 1 | Error. File copy canceled by the user. |
| < 0 | Error. Source file not copied to the destination file. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

- In order to use a progress indicator, you must first create it with [create.progress.indicator()](../functions_progress_indicators/create.progress.indicator.md). When you want the progress indicator to start with another value then 0, you must use [change.progress.indicator()](../functions_progress_indicators/change.progress.indicator.md) to change its initial value. If you specify the PROGRESS.STOP and/or PROGRESS.CANCEL modes when creating the indicator, the user can stop or cancel the copy operation before it has completed. In both cases, the destination file is deleted.

- This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Example
```

create.progress.indicator("Title", PROGRESS.BAR + PROGRESS.STOP)
server2client(
      bse.tmp.dir$() & "/test1.txt", "C:\Program Files\Test.txt", false, true )
```

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
