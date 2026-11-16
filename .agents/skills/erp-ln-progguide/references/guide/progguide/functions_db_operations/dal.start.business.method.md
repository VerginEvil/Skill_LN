# dal.start.business.method()

## Syntax:
`#include <bic_dam>`
`function void dal.start.business.method( string set_id, string name, ref long retval, [... ] )`

## Description
This starts a specified business method.
The business method must be implemented as a function of type EXTERN LONG. If this is the first call to a particular class (that is, table), the [before.open.object.set()](../functions_dal/before.open.object.set.md) hook is automatically called before the business method is called.

## Arguments
| | | |
|---|---|---|
| `string` | `set_id` |  Indicates the name of the DAL that implements the business method.  |
| `string` | `name` |  The name of the business method.  |
| `ref long` | `retval` |  The return value of the business method. Negative values are reserved for the calling mechanism. For example: `-1 DALNOOBJSET` `-2 DALNOMETHOD` The business method may return only DALHOOKERROR, 0, or positive numbers.  |
| `[` | `... ]` |  Use these optional arguments to pass arguments to the business method.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Executing standard hooks is not allowed via this function. Extension hooks will not be executed! Calling standard hooks should be avoided, as these are not atomic functions. If needed, use [dal.execute.hook()](dal.execute.hook.md) for standard hooks.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
