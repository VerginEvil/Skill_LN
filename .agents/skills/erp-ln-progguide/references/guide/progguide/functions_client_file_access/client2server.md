# client2server()

## Syntax:
`#include <bic_desktop>`
`function long client2server( string source, string dest, boolean text.mode, [ boolean rm.file, boolean progress.window ] )`

## Description
*Deprecated.* This copies a specified file from the client to the server.

## Arguments
| | | |
|---|---|---|
| `string` | `source` |  The source file name, on the client. When this is an empty string, this function will show the file open dialog, through which the user can select an existing file on the client. The function [get.local.filename()](get.local.filename.md) can be used afterwards to retrieve the actual filename on the client which was copied. The source parameter may include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |
| `string` | `dest` |  The destination file name, on the server.  |
| `boolean` | `text.mode` |  This is a boolean value that specifies whether the file is to be copied in text or binary mode: true text mode false binary mode  |
| `[ boolean` | `rm.file ]` |  Use this optional argument to specify whether the source file must be deleted after it has been copied: true source file is deleted false source file is not deleted  |
| `[ boolean` | `progress.window ]` |  Use this optional argument to specify whether a progress indicator must be displayed to indicate the progress of the copy action: true progress indicator is displayed false progress indicator is not displayed  |

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
client2server
      ("C:\Program Files\Test.txt2", bse.tmp.dir$() &
"/test1.txt",
      false, false, true)
```

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
