# tt.chm.chart()

## Syntax:
`function boolean tt.chm.chart( string appl(40), string chart_name(16) )`

## Description
This checks if the specified chart is present in the specified Chart Manager application.

## Arguments
| | | |
|---|---|---|
| `string` | `appl(40)` |  The name of the Chart Manager application. This takes the form: *ppmmxxxx*, where *pp* is the package code, *mmm* is the module code, and *xxx* is the name of the Chart Manager application. This argument must refer to a record in the Maintain Chart Manager Application Data session (ttchm1500m000).  |
| `string` | `chart_name(16)` |  The name of the chart.  |

## Return values
false success
true error; chart or application not found

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
