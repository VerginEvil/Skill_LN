# seq.open.dialog.local()

## Syntax:
`#include <bic_desktop>`
`function long seq.open.dialog.local( boolean mselect, string defaultname, string directory, string filter, ref string filename )`

## Description
*Deprecated.* This shows the Windows file-open dialog, to allow the user to select one or more local files.

## Arguments
| | | |
|---|---|---|
| `boolean` | `mselect` |  When true, multiple select is allowed by the user else only one file can be selected by the user.  |
| `string` | `defaultname` |  The default filename shown in the file-open dialog.  |
| `string` | `directory` |  The startup directory for this dialog. In case of an empty string the "My Documents" directory will be the default. This parameter may include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |
| `string` | `filter` |  This argument specifies all possible file extensions for the file. The string must contain pairs of strings that are separated by a "|" character. The first string in each pair is a filter name (for example: "Text Files"). The second string must be a filter patern (for example: "*.txt"). Multiple filter patters can be specified by separating the filter patterns with a semicolon. Example: "All Files(*.*)|*.*|Text Files(*.txt) Word documents(*.doc)|*.txt;*.doc"  |
| `ref string` | `filename` |  Output argument which will contain the full path of the file selected by the user. In case *mselect* is true possible other selected file names can be retrieved using function [seq.open.dialog.next()](seq.open.dialog.next.md)  |

## Return values
| | |
|---|---|
| > 0 | Number of files selected by the user. |
| 0 | File open dialog canceled by the user. |
| -1 | Error occurred |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
