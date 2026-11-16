# aud.get.field.info()

## Syntax:
`function void aud.get.field.info( long selection.id, long table.id, long field.id, ref long field.depth, ref long field.type, ref long field.length )`

## Description
Returns the format of the field at the time it was audited. The information consists of the type, the depth and the size of the field. This function will not check the input, because of performance reasons. Instead the combination *selection.id*, *table.id*, *field.id* is assumed to refer to an existing field, as returned by [aud.get.field.ids()](aud.get.field.ids.md). This means that if the input parameters are not valid, an error message will be presented to the end user

## Arguments
| | | |
|---|---|---|
| `long` | `selection.id` |  Id of the selection, as provided by [aud.select.transactions()](aud.select.transactions.md).  |
| `long` | `table.id` |  Id of the table on which the action occurred, which is used to retrieve the detailed action data using function [aud.get.field.status()](aud.get.field.status.md), [aud.put.old.field.value()](aud.put.old.field.value.md), and [aud.put.new.field.value()](aud.put.old.field.value.md). This id is also used to get the meta data information, in case it has been changed.  |
| `long` | `field.id` |  Identifier for a field, as retrieved using the functions aud.get.field.ids() or aud.get.field.list(). Precondition: field.id should not be 0: for not existing fields no field information can be retrieved.  |
| `ref long` | `field.depth` |  Depth of the field: 1 for non array fields, > for array fields  |
| `ref long` | `field.type` |  Data type of the field, for example db.long, db.double, db.string, db.multibyte and so on. See this [list of database types](../functions_database_handling/overview.md#types).  |
| `ref long` | `field.length` |  Length of the field in the action row string. The *field.length* specifies the number of characters to be extracted from the old value or the new value string. See this [list of database types and related byte lengths](../functions_database_handling/overview.md#types). The length of fields of type DB.TIME depends on the TIV level of the porting set which audited the transaction. If this TIV level is less than 2000, then DB.TIME fields have length 4 and the field contains a [UTC](../functions_date_time_zones/overview.md#utc) long format value in [Utc32](../functions_date_time_zones/overview.md#Utc32) layout. If this TIV level is at least 2000, then DB.TIME fields have length 5 and the field contains a [UTC](../functions_date_time_zones/overview.md#utc) long format value in [Utc40](../functions_date_time_zones/overview.md#Utc40) layout.  |

## Return values
None

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restrictions
It is assumed that the *field.id* is retrieved using function aud.get.field.ids and has a valid value (greater than 0). So this is not checked in the function.

## Related topics
- [Audit management overview](audit_management_overview.md)

- [Audit management synopsis](audit_management_synopsis.md)

- [Audit management examples](audit_management_examples.md)
