# query.extend.fld.select()

## Syntax:
`function long query.extend.fld.select( string select_column, string select_expression )`

## Description
With the query.extend.fld… interface the metadata is stored in the 4gl engine. The query.extend.fld… information is used to build the standard query for retrieving requested data, inclusive the application fields. The result is used for the display of the field. The value of easy filter on the application field and the query.extend.fld… information is used to extend the WHERE clause of the standard query. The standard query is used to display the session.
SQL expression for the SELECT clause of a column. This expression will be added to the standard query for displaying the column as form field. ( see [query.extend.fld.from()](query.extend.fld.from.md) or [query.extend.fld.where()](query.extend.fld.where.md))
You can use this function in the section before.program.

## Example use query.extend.fld... functions
```

|****************************** program section ********************************
before.program:
	| Selection methods calculation field: form.calc1
	query.extend.fld.select("form.calc1","texxx100.int1 * texxx100.pric")
	query.extend.fld.from(  "form.calc1","texxx100")

	| Selection methods calculation field: form.calc2
	query.extend.fld.select("form.calc2","texxx110.int1 + " &
						    "texxx200.int2 + " &
						    "alias200.int2")
	query.extend.fld.from(  "form.calc2","texxx110, texxx200,texxx200 alias200"),
	query.extend.fld.where( "form.calc2","texxx110.bpid = texxx100.bpso AND ” &
				                 "texxx100.bpso REFERS TO texxx200" AND " &
					          "texxx100.bpsh REFERS TO alias200 PATH texxx170")

	| Selection methods database field: texxx110.desc
	query.extend.fld.select("texxx110.desc")
	query.extend.fld.from(  "texxx110.desc", "texxx110")
	query.extend.fld.where( "texxx110.desc" ,"texxx110.bpid = texxx100.bpsh")


	| Selection methods application field: form.desc
	query.extend.fld.select("form.desc", "texxx110.desc")
	query.extend.fld.from(  "form.desc", "texxx110")
	query.extend.fld.where( "form.desc” ,"texxx110.bpid = texxx100.bpso")
```

## Arguments
| | | |
|---|---|---|
| `string` | `select_column` |  Name of the form field in the form.  |
| `string` | `select_expression` |  SQL instruction for SELECT clause.  |

## Return values
| | |
|---|---|
| 0 | On success. |
| <> 0 | error |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## TIV
This function is available from Enterprise Server TIV level 2100 and is only usable in LN-UI.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Column filtering](column_filtering.md)
