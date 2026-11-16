# start.angular.app()

## Syntax:
`function long start.angular.app( string application, [ string query, long options, string title ] )`

## Description
Start an angular workbench. This function will return when the angular application is closed by the user.

## Arguments
| | | |
|---|---|---|
| `string` | `application` |  This is the Web application name which implements the angular workbench client This is part of the relative path of the Web application on the Web Server. for example "planner".  |
| `[ string` | `query ]` |  Optional argument. An xml element with a number of attribute/value pairs. These attribute/value pairs will appended to the URL as query parameters. Can be set to 0, to indicate no query parameters are passed.  |
| `[ long` | `options ]` |  Optional argument to set some desk application options. Possible values: DSK.STATUSBAR Show a status bar Default value DSK.STATUSBAR  |
| `[ string` | `title ]` |  Optional argument in which a non-standard title of the Workbench session can be specified. When this argument is not present, the session description is used as the Workbench title. This argument can be useful when the same workbench application should have a different title which can only be determined at runtime  |

## Return values
| | |
|---|---|
| 0 | on success |
| -1 | when this function fails |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2496.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Workbench Sessions overview](overview.md)

- [Workbench Sessions synopsis](synopsis.md)
