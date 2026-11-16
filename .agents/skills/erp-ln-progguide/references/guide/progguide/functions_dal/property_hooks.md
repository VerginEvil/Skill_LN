# Property hooks
Property hooks are hooks that relate to a specific property (that is, a table field).
The fieldname.check() property hooks replace the *check.input* event sections for fields of the main table. If there is a DAL for an object set, the property hooks are called to perform the necessary field checks. Any *check.input* sections in the UI script are ignored. So, if a UI script contains *check.input* sections for fields of the main table, you must replace these by property hooks in the DAL. In the UI script, *check.input* sections are retained for non-database form fields. Such sections are executed even if a DAL exists.
There are 3 property hooks:

- Hook [fieldname.make.valid()](fieldname.make.valid.md) is called before the field is checked. It can be used e.g. to perform rounding of data.

- Hook [fieldname.check()](fieldname.check.md) is called by the [4GL engine](../glossary/glossary.md#fourgl_engine) when inserting or updating an object

- Hook [fieldname.set.defaults()](fieldname.set.defaults.md) is called by the B3 through a BOI in case of a DAL_NEW or DAL_UPDATE

Note  The fieldname.make.valid() is *not* executed when a [dal.new()](../functions_db_operations/dal.new.md) or [dal.update()](../functions_db_operations/dal.update.md) is done! Instead use [dal.save.object()](../functions_db_operations/dal.save.object.md) in combination with [dal.new.object()](../functions_db_operations/dal.new.object.md) or [dal.change.object()](../functions_db_operations/dal.change.object.md).

## DAL 2
In case of [Extended DAL (DAL2)](dal2_overview.md) the fieldname.check() property hook is supported for backward compatibility reasons. However, a field having this property hook is *not* regarded as a DAL2 field. In order to make use of the benefits of DAL2 for such a field, you should replace these hooks by a number of [DAL2 Field hooks](dal2_field_hooks.md).
In this way you can implement the DAL2 concept incrementally.

## See also
[Property methods](property_methods.md)

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [DAL hooks](dal_hooks.md)
