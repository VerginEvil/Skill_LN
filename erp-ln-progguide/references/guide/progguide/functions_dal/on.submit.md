# on.submit()

## Syntax:
`function long on.submit( )`

## Description
This hook is executed in case Workflow Document Authorization is active for the Business Object of which the table of this DAL, is the root table, as defined in the OCM Workflow Model. In case any changes made to the Business Object are submitted, the DBCM layer will execute this hook. This hook must then publish a Workflow BOD to ION with a request for approval.
Note: This hook should only be implemented for root tables.

## Return values
| | |
|---|---|
| 0 |  In case of success.  |
| DALHOOKERROR |  In case of a failure.  |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Data Access Layer](overview.md)
- [Database Change Management (DBCM) overview](../functions_dbcm/overview.md)
