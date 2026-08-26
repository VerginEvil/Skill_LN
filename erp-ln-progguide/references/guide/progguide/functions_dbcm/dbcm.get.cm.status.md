# dbcm.get.cm.status()

## Syntax:
`function enum dbcm.get.cm.status( const string toid$ )`

## Description
Retrieves the Change Management status of the Object that is identified by the given Typed Object Id.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id; this is a string of 34 characters identifying a business object.  |

## Return values
| | | |
|---|---|---|
| Constant | Value | Description |
| `DBCM_STATUS_DRAFT` | 1 | The Object is in the Draft state; it is checked-out, it can be modified and any changes can be submitted, or any changes can be undone by doing a Revert to Approved.  |
| `DBCM_STATUS_DRAFT_REV` | 2 | The Object is in the Draft state, for a second time; this state is equal to the DBCM_STATUS_DRAFT state, except that an Object can only enter this state after a Recall of any submitted changes was successful.  |
| `DBCM_STATUS_PENDING` | 3 | The Object is in the Pending state; this means any changes to the Object have been submitted and the user must wait until the changes are Approved or Rejected. The Object cannot be modified.  |
| `DBCM_STATUS_RECALL_REQ` | 4 | The Object is in the Recall Requested state; the user made a request to ignore any submitted changes, as he e.g. wants to make more changes to the Object. The Object cannot be modified.  |
| `DBCM_STATUS_REJECTED` | 5 | The Object is in the Rejected state; any submitted changes were not approved. The user must either make other changes and re-submit them, or perform a Revert to Approved. The Object can be modified.  |
| `DBCM_STATUS_APPR_RECVD` | 6 | The Object is in the Approval Received state; usually this state will not be visible to the user. It can only be visible if somehow, after receiving an Approval, the Object cannot be checked-in. In this situation an Admin must be involved in order to force a check-in, or to discard any changes and perform a Revert to Approved. The Object can be modified.  |
| `DBCM_STATUS_APPROVED` | 7 | The Object is in the Approved state; any submitted changes have been Approved, and the Object has been checked-in. The Object can be modified.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
