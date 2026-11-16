# dal.set.property.with.check()

## Syntax:
`#include <bic_dam>`
`function long dal.set.property.with.check( string tbl.name, long object_set, const string proper_name, void value )`

## Description
In order to notify the DAL about a change to the value of a property, you must use this function to change the value. Using this function ensures that the relevant property hooks are executed when the value is changed. If you use an assignment or the db.* functions to change a property value, the DAL is not notified of the change. Consequently, the property checks in the DAL are not executed.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  A string containing the name of the DAL.  |
| `long` | `object_set` |  The ID of an open object set (if this ID is not known, use the table ID).  |
| `const string` | `proper_name` |  The name of the property whose value must be changed.  |
| `void` | `value` |    |

## Return values
The return value of the property check.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## DEPRECATED
This function has been deprecated. Please use [dal.set.field()](dal.set.field.md) in combination with [dal.check.field()](dal.check.field.md) instead.

## Remark
The property check is executed by calling this function, and the has_changed flag is set to DAL_UPDATE. The return value of this function is the return value of the property check.
There is another function: [dal.set.property()](dal.set.property.md) which does the same as dal.set.property.with.check, but only calls the property check during the dal.update/dal.destroy.
You can call this function from both UI and DAL scripts.

## Example
See [dal.set.property()](dal.set.property.md)

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
