# dal.set.cdf.fields()

## Syntax:
`#include <bic_dam>`
`function long dal.set.cdf.fields( string tbl.name )`

## Description
This function can be used to copy Customer Defined Fields from a source record to a target record of the same table, see also [dal.store.cdf.fields()](dal.store.cdf.fields.md).
It sets all previously stored Custom Defined Fields of the given table on the current table record and informs the DAL that these fields are changed.
For each CDF of type Text, the text is copied as well.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  the table name of the DAL.  |

## Return values
| | |
|---|---|
| 0 | OK (CDF fields are set) |
| -1 | CDF fields were not stored for the table |
| -2 | CDF text cannot be copied |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2460.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Preconditions
Function [dal.store.cdf.fields()](dal.store.cdf.fields.md) must have been called before for the same table.
Note  This function does not update any dependent fields itself, nor does it check the field's value! These actions are done during a save.

## Example
```

function long tdsls400.create.copy()
{
	long	result

	|* Store the current values of the CDFs from the source record
	result = dal.store.cdf.fields("tdsls400")
	RETIFNOK(result)

	|* Start insert, sets object defaults
	dal.new.object("tdsls400")

	|* Set table fields
	dal.set.field("tdsls400.hdst", status)
	dal.set.field("tdsls400.corg", origin)
	...

	|* Set the stored values of the CDFs for the copy record
	result = dal.set.cdf.fields("tdsls400")
	RETIFNOK(result)

	|* Save the record. This will make sure that all fields will get a
	|* correct value, based on the field dependencies defined for the DAL.
	result = dal.save.object("tdsls400")

	return(result)
}
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)

- [CDF (Customer Defined Fields) handling overview](../functions_cdf/overview.md)

- [CDF (Customer Defined Fields) handling synopsis](../functions_cdf/synopsis.md)
