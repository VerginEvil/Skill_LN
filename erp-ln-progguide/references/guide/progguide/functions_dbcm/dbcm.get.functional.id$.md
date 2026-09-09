# dbcm.get.functional.id$()

## Syntax:
`function string dbcm.get.functional.id$( const string toid$, [ long comp ] )`

## Description
Retrieves the functional object id for a checked-out object.
The functional id is a concatenation of the values of all primary key parts, separated with commas. E.g. "SLS000368, 10" for Line 10 of Sales Order SLS000368.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id. A Typed Object Id is a string of 34 characters identifying a checked-out business object.  |
| `[ long` | `comp ]` |  A company number to retrieve the functional id from.  |

## Return values
The functional id as string (key parts are concatenated using commas); or an empty string in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
