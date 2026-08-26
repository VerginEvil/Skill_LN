# dbcm.is.cm.active()

## Syntax:
`function boolean dbcm.is.cm.active( const string tbl.name$, [ long comp ] )`

## Description
Tests whether Change Management is active for the given table (and optionally the company number), as defined in the Object Configuration Management deployment for the current package combination.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name$` |  A table code, like "tdsls400".  |
| `[ long` | `comp ]` |  The company number in which the perform the test. If not specified, the test is done in the current company.  |

## Return values
| | |
|---|---|
| true | In case Change Management is active for the given table (and company). |
| false | In any other case. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
