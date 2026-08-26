# Property methods

## Setting properties
In order to notify the DAL about a change in the value of a property, you must use the [dal.set.property()](../functions_db_operations/dal.set.property.md) function to change the value. Using this function ensures that the relevant property hooks are executed when the value is changed. If you use an assignment or the [Database operations overview](../functions_db_operations/overview.md) functions to change a property value, the DAL is not notified of the change. Consequently, the property checks in the DAL are not executed.
You can call this function from both UI and DAL scripts.

## Retrieving properties
You can retrieve the value of the flag (see [Property hooks](property_hooks.md)) for any property by calling [dal.get.property.flag()](../functions_db_operations/dal.get.property.flag.md). The property must have been changed by the *dal.set.property()* function.
You can call this function from both UI and DAL scripts.

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [DAL hooks](dal_hooks.md)
- [Transition issues (BAAN IV to Infor Enterprise Server)](transition_issues_baan_iv_to_baanerp.md)
