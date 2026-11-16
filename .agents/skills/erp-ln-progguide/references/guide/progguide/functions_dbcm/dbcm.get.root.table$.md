# dbcm.get.root.table$()

## Syntax:
`function string dbcm.get.root.table$( const string toid.or.obj.type$ )`

## Description
Returns the root table of an either an Object or an Object Type.
In case a Type Object Id is specified (which identifies a specific instance of a certain Object Type), first the Object Type is determined. Then, for that Object Type, the root table is returned.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid.or.obj.type$` |  A Typed Object Id, or an Object Type. A Typed Object Id is a string of 34 characters identifying a checked-out business object. An Object Type is a string of 6 characters identifying a business object type.  |

## Return values
The root table code, or an empty string in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
