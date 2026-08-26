# is.tenant.bse()

## Syntax:
`function boolean is.tenant.bse( )`

## Description
This function returns TRUE if the current BSE is a tenant BSE; FALSE otherwise.

## Return values
| | |
|---|---|
| TRUE | The BSE is a tenant BSE. |
| FALSE | The BSE is not multi tenant enabled or is not a tenant BSE. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Multi Tenant functions overview](overview.md)
- [Multi Tenant functions synopsis](synopsis.md)
