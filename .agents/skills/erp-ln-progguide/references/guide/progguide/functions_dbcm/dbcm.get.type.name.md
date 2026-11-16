# dbcm.get.type.name()

## Syntax:
`function long dbcm.get.type.name( const string tbl.name$, ref string obj.type$ )`

## Description
Returns the object type for the given table, as defined in the Object Configuration Management model for the current package combination.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name$` |  A table code, e.g. "tdsls400".  |
| `ref string` | `obj.type$` |  The returned object type as defined in the Object Configuration Management model. This is a string of max 6 characters. In case no object type is defined for the given table, an empty string is returned. In case multiple object types are defined for the given table, this value is undefined.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| -1 | In case of an error; variable *e* contains the error code. See [Database Change Management (DBCM) error codes](error_codes.md) for more information about the error codes and their meaning. |
| 1 | The given table occurs in more than one object type (ie. the table is a shared table); an example of this may be table tcibd420. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
