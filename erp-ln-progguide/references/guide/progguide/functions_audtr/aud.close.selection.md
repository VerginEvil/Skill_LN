# aud.close.selection()

## Syntax:
`function long aud.close.selection( long selection.id )`

## Description
The opening of the audit trail is not done explicitly in comparison to the low-level audit library functions. To close the opened files again, the developer must use the aud.close.selection. During the invocation of [aud.select.transactions()](aud.select.transactions.md) and all functions beginning with aud.get.next, each file that is opened but not closed will be registered within the Infor Enterprise Server Audit Management. The function aud.close.selection() will use this information to close the files that are registered as being open. The function also closes the selection of transactions that have been created using the aud.select.transactions function.

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selection, as provided by [aud.select.transactions()](aud.select.transactions.md).  |

## Return values
| | |
|---|---|
| AUD_OK | All files are closed successfully and the dynamic SQL selection is also closed successfully  |
| AUD_INCORRECT_SELECTION_ID | *Selection.id* is invalid.  |
| AUD_FAIL | Not all files could be closed or the dynamic SQL statement is not closed successfully.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## State
The internal state on the *selection.id* is removed, so after running this function *selection.id* cannot be used anymore.

## Restrictions
The function [aud.select.transactions()](aud.select.transactions.md) has to be called prior to this function. After executing aud.close.selection, the *selection.id* cannot be used anymore in any other Infor Enterprise Server Audit Management functions.

## Related topics
- [Audit management overview](audit_management_overview.md)
- [Audit management synopsis](audit_management_synopsis.md)
- [Audit management examples](audit_management_examples.md)
