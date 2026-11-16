# tt.chm.application()

## Syntax:
`function boolean tt.chm.application( string appl )`

## Description
This checks if the specified Chart Manager application is present in the runtime dictionary.

## Arguments
| | | |
|---|---|---|
| `string` | `appl` |  The name of the Chart Manager application. This takes the form: *ppmmxxxx*, where *pp* is the package code, *mmm* is the module code, and *xxx* is the name of the Chart Manager application. This argument must refer to a record in the Maintain Chart Manager Application Data session (ttchm1500m000).  |

## Return values
false application not found
true application found

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
