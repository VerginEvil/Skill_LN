# rdi.report.sensitivity()

## Syntax:
`function long rdi.report.sensitivity( const string reportname )`

## Description
Returns sensitivity of current report if no reportname was specified, otherwise the given reportname is used.

## Arguments
| | | |
|---|---|---|
| `const string` | `reportname` |  optional argument: the name of the report for which you need to know the sensitivity.  |

## Return values
A value of 0 means that the report is not sensitive. A value of 1 - 99 is the sensitivity level. A value of < 0 or > 99 indicates an error.

## Context
This function is implemented in the porting set and can be used in all script types.

## Remarks
If no reportname was provided and handle.report.pool function was called before, all table fields (if any) on the current report are also part of the sensitivity level calculation. In case of a reportname was provided, the sensitivity level as specified in $BSE/lib/sensitivity_reports was returned, and no table fields on the report are part of the sensitivity calculation.
This function is available with portingsets starting at TIV level 1200.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
- [Tools Interface Version (TIV)](../tiv/tiv_overview.md)
