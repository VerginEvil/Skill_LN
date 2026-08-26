# tt.reportgroup.exists()

## Syntax:
`function boolean tt.reportgroup.exists( string session(13), long report_group )`

## Description
This checks if a specified report group ( *report_group*) is present in the definition of the specified session ( *session*).
When more than one report is linked to a session, the reports may be grouped. Report groups are useful when specific reports must be used in specific situations. The current report group is defined in the predefined variable *reportgrp* (the default report group is 1).

## Arguments
| | | |
|---|---|---|
| `string` | `session(13)` |  |
| `long` | `report_group` |  |

## Return values
TRUE report group exists
FALSE report group does not exist

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
if tt.report group.exists("tccom0401m000", 2) then
reportgrp = 2 | else reportgrp = 1 (default)
endif

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
