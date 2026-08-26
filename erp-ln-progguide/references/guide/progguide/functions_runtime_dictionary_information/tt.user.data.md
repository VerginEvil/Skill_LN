# tt.user.data()

## Syntax:
`function boolean tt.user.data( string user(12), long property, ... )`

## Description
This function retrieves one or more properties of an Infor LN user.
The arguments must meet the following conditions:
- at least 3 arguments
- an odd number of arguments
- a property must be a known property (i.e. in the list below)
- the data type of the argument following a property must be correct

## Arguments
| | | |
|---|---|---|
| `string` | `user(12)` |  |
| `long` | `property` |  After the 'user', one or more pairs follow, with property (long) and value (ref):  |
| `` | `...` |  |

## Return values
| | |
|---|---|
| false | error; user not found or invalid input |
| true | success |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
