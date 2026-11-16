# dal.execute.hook()

## Syntax:
`#include <bic_dam>`
`function void dal.execute.hook( string set_id, string name, ref long retval, long mode, long elem )`

## Description
This starts a specified hook.
This function will for the hooks
is.applicable, is.derived, is.mandatory, is.readonly, is.never.applicable, is.valid, make.valid and update
execute the extension hooks before and after executing the hook.
If this is the first call to a particular class (that is, table), the [before.open.object.set()](../functions_dal/before.open.object.set.md) hook is automatically called before the hook is called.

## Arguments
| | | |
|---|---|---|
| `string` | `set_id` |  Indicates the name of the DAL that implements the hook.  |
| `string` | `name` |  The name of the hook.  |
| `ref long` | `retval` |  The return value of the hook.  |
| `long` | `mode` |  mode flag, one of { 0, DAL_NEW, DAL_UPDATE }  |
| `long` | `elem` |  element number in case the field is an element of an array (for non array fields this value is 1)  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Calling standard hooks should be avoided, as these are not atomic functions!
Minimal tools version is 10.7.3 with tools solution 2139062 installed. Otherwise the extension hooks will not be executed.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
