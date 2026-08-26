# zoom.to$()

## Syntax:
`function string zoom.to$( string process, long zoomcode, string zoomname, string returnfld, long formpos )`

## Description
Use this to zoom to another session or menu.

## Arguments
| | | |
|---|---|---|
| `string` | `process` |  Specifies the name of the session or menu that must be started.  |
| `long` | `zoomcode` |  This can be either Z.MENU or Z.SESSION, depending on whether it is a menu or session that is being started.  |
| `string` | `zoomname` |  The name of the calling process. This is used in the [4GL zoom.from sections](../4gl_features/4gl_zoomfrom_sections.md) sections in the called process. If no name is provided here, *zoom.from* sections in the child session are not executed.  |
| `string` | `returnfld` |  Indicates the name of the variable to be returned by the function. It must be the name of a variable in the called process. If an empty string is specified here, the function returns the exit value of the zoom process. If the argument is not filled, the function returns nothing.  |
| `long` | `formpos` |  Specifies the form position for displaying the window. The default is 0  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and Value of argument process starts with "tx" or "otx"

## Return value
The variable specified in the *returnfld* argument.
Note  This function is supported for backward compatibility only. In new applications, use [start.session()](start.session.md) instead.

## Related topics
- [Starting and stopping programs: overview and synopsis](overview_and_synopsis.md)
