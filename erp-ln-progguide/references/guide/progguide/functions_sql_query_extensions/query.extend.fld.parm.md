# query.extend.fld.parm()

## Syntax:
`function long query.extend.fld.parm( string select_column, string parameter )`

## Description
Parameter for the query.extend.fld clause of a column defined by query.extend.fld.select.
The parameter is merged to the meta data of the query.extend.fld definition. Each parameter has its own functionality.
You can use this function in the section before.program.

## Arguments
| | | |
|---|---|---|
| `string` | `select_column` |  Name of the form field in the form.  |
| `string` | `parameter` |  Predefined word NO_REFRESH_EDITABLE_GRID - the editable grid field is maintained by the script in field section before.display:. The field value is not automatic refreshed. FIELD_WITH_ELEMENT - The column contains elements. Element of form-field is used to retrieve the sequential number of table field declared by query.extend.fld.select().  |

## Return values
| | |
|---|---|
| 0 | On success. |
| <> 0 | Error |
| -1 | Column not found |
| -2 | Column can not be added to extend definition |
| -3 | Wrong sql expression for column |
| -4 | All elements of same colum-field must use the same sql expression as clause for query.extend.fld.select(), query.extend.fld.from() and query.extend.fld.where(). |
| -5 | For UPDATE or DELETE is not allowed |
| -6 | Column definition is already in use. (query.extend.select...) |
| -11 | Qrycol not supported (application version must be at least 10.4 or tiv portingset is not 2030 or higher.) |
| -12 | Unknown parameter value |
| -13 | Query.extend.fld for column-name not present |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## TIV
This function is available from Enterprise Server TIV level 2370, FIELD_WITH_ELEMENT in TIV level 2420 and is only usable in LN-UI.
Notes  Query.extend.fld.parm("column",...) must follow the other Query.extend.fld...("column",..) function(s) for the column.
You can only use FIELD_WITH_ELEMENT with a simple sql expression in QUERY.EXTEND.FLD.SELECT().
The folowing syntax is supported: "table.field" or "SELECT table.field FROM... WHERE...".
The column-field must be defined in the program as extern field with the maximum element. This is used for saving and needed for navigating throught rows of the view.

## Example
```

	| f.ttadv.tver is added multiple times to Form Definition with different Element
	extern 	domain	ttadv.vers	f.ttadv.tver(5)

before.program:
	|optional reference
	query.extend.fld.select("f.ttadv.tver", "ttadv111.tver")
	query.extend.fld.from("f.ttadv.tver", "ttadv111")
	query.extend.fld.where("f.ttadv.tver", "ttaad121.cmba REFERS TO ttadv111")
	query.extend.fld.parm("f.ttadv.tver", "FIELD_WITH_ELEMENT")
```

## Related topics
- [SQL query extensions overview](overview.md)

- [SQL query extensions synopsis](synopsis.md)
