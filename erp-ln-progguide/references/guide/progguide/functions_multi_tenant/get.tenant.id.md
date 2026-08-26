# get.tenant.id()

## Syntax:
`function string get.tenant.id( )`

## Description
Returns the tenant id of the tenant under which the user is logged in. If the user is not logged in under a tenant then id "infor" is returned.

## Return values
| | |
|---|---|
| String containing tenant id | The tenant id of the tenant under which the user is logged in |
| infor | The user is not logged in under a tenant |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [Multi Tenant functions overview](overview.md)
- [Multi Tenant functions synopsis](synopsis.md)
