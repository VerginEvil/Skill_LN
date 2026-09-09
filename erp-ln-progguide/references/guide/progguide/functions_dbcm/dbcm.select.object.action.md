# dbcm.select.object.action()

## Syntax:
`function long dbcm.select.object.action( const string action.id$ )`

## Description
Selects the specified object action.
The specified action is used to determine whether any changes made to the object require auto-check-in when these changes are submitted for Workflow approval. This works as follows:
When the specified action is active according to the Object Configuration Management deployment for the current package combination, submitting any changes will cause execution of the `on.submit` hook in the DAL of the object's root table. Typically, this hook will publish a Workflow BOD which is to be processed by ION Workflow. Only after the changes have been approved, the object will be checked-in.
When it appears that the specified action is not active, submitting any changes will cause an immediate check-in of the object.
Important Note  In contrast to how [dbcm.select.object.instance()](dbcm.select.object.instance.md) works, a selected object action is *not* reset on return of a function.

## Arguments
| | | |
|---|---|---|
| `const string` | `action.id$` |  An id which identifies a specific action, as defined in the Object Configuration Management model. This is a string of max 6 characters.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 | In case of an error; variable *e* contains the error code. See [Database Change Management (DBCM) error codes](error_codes.md) for more information about the error codes and their meaning. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2490 and the root table of the selected Object Type is of package "tx".

## Related topics
- [Database Change Management (DBCM) overview](overview.md)

- [Database Change Management operations synopsis](synopsis.md)
