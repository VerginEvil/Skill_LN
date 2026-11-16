# dbcm.select.checked.in.mode()

## Syntax:
`function long dbcm.select.checked.in.mode( boolean value )`

## Description
Sets or unsets the checked in mode.
Use the checked in mode to ignore checked-out objects when querying and manipulating tables for which DBCM is active.
Important Note  This function is only meant for SPT libraries used by the Data Upgrade Engine.
When the *value* argument is true, the empty Object instance and the empty Object Type override any earlier selected instance and type. The (set or unset) value of the checked in mode and the (either or not modified) selected Object instance and Object Type remain in effect until the end of the current 3GL function. After return from the current 3GL function, the checked in mode and the instance and type selection are set back to the values that they had in the calling 3GL function. When the program jumps back to a [retry point](../functions_database_handling/retry_points.md), the checked in mode and the instance and type selection are set back to the values that they had at the moment that the retry point was set.

## Arguments
| | | |
|---|---|---|
| `boolean` | `value` |  specify 'true' to select the checked in mode; this also deselects any selected Object instance and Object Type. specify 'false' to deselect the checked in mode; this does not influence any selected Object instance and Object Type.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 | In case of an error; variable *e* contains the error code. See [Database Change Management (DBCM) error codes](error_codes.md) for more information about the error codes and their meaning. |

## Context
This function is implemented in the 4GL Engine and can be used in SPT DLL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
