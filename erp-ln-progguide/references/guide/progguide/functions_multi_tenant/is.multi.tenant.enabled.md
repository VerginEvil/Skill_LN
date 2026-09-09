# is.multi.tenant.enabled()

## Syntax:
`function boolean is.multi.tenant.enabled( )`

## Description
*Deprecated.* This function is deprecated as the name is confusing and it is actually the same as function [is.landlord.bse()](is.landlord.bse.md).
Returns TRUE if the current BSE is multi-tenant enabled; FALSE otherwise.
Note: if the current BSE runs in a tenant, the function returns FALSE.

## Return values
| | |
|---|---|
| TRUE | The BSE is multi tenant enabled. |
| FALSE | The BSE is not multi tenant enabled. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Multi Tenant functions overview](overview.md)

- [Multi Tenant functions synopsis](synopsis.md)
