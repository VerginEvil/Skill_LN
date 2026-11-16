# dbcm.find.object.by.workflow.id()

## Syntax:
`function long dbcm.find.object.by.workflow.id( const string wf.id$, ref string toid$ )`

## Description
Finds a checked-out business object using the given workflow instance id. When the object is found, the Typed Object Id is returned.
This function is typically used in the communication between ION Workflow and Infor LN when processing BODs.

## Arguments
| | | |
|---|---|---|
| `const string` | `wf.id$` |  A Workflow instance id.  |
| `ref string` | `toid$` |  The returned Typed Object Id (only filled when the object was found).  |

## Return values
| | |
|---|---|
| 0 | The object was found successfully. |
| `ENOREC` (111) | The object was not found; probably the object is not checked out. |
| <> 0 | Another database error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
