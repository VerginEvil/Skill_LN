# tt.chm.appl.desc()

## Syntax:
`function long tt.chm.appl.desc( string appl(40), ref string desc() mb )`

## Description
This retrieves the description (in the user's current language) of a specified Chart Manager application.

## Arguments
| | | |
|---|---|---|
| `string` | `appl(40)` |  The name of the Chart Manager application. This takes the form: *ppmmxxxx*, where *pp* is the package code, *mmm* is the module code, and *xxx* is the name of the Chart Manager application. This argument must refer to a record in the Maintain Chart Manager Application Data session (ttchm1500m000).  |
| `ref string` | `desc() mb` |  This returns the description of the specified Chart manager application.  |

## Return values
0 success
1 error; application not found

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
