# dal.skip.never.applicable.checks()

## Syntax:
`#include <bic_dal>`
`function void dal.skip.never.applicable.checks( [ boolean keep_old_data ] )`

## Description
By default, the 4GL engine will check fields that are defined as never applicable. You can skip these checks by calling this function in the [before.open.object.set()](../functions_dal/before.open.object.set.md) hook in the DAL.

## Arguments
| | | |
|---|---|---|
| `[ boolean` | `keep_old_data ]` |  if this argument is KEEP_OLD_DATA (define for true) then the data of never applicable fields will stay unchanged. This argument is only available for dal with TIV LEVEL >= 2140  |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
