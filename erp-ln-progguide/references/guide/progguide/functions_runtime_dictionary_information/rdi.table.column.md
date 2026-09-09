# rdi.table.column()

## Syntax:
`function long rdi.table.column( string table_name(9), long column_number, ref string column_name, ref string domain_name(14), ref long offset, ref long size, ref long dept, ref long type, ref long flag, ref string default_value, [ long flag_filter ] )`

## Description
This returns information about a specified column which is identified by the table name and the column number. Note that the first columns in the table are reserved for the following columns: Refcntd, Refcntu, _compnr, _dlock, and _index<number> (one column for each index).

## Arguments
| | | |
|---|---|---|
| `string` | `table_name(9)` |  The name of the table in which the column occurs (omit the leading 't').  |
| `long` | `column_number` |  The column number.  |
| `ref string` | `column_name` |  This returns the name of the column.  |
| `ref string` | `domain_name(14)` |  This returns the name of the column's domain.  |
| `ref long` | `offset` |  This returns the position of the column in the row.  |
| `ref long` | `size` |  This returns the size of the column, in bytes. See this [list of database types and related byte lengths](../functions_database_handling/overview.md#types).  |
| `ref long` | `dept` |  This returns the depth of the column (array columns only).  |
| `ref long` | `type` |  This returns the database type of the column. For example, DB.LONG, DB.FLOAT, and so on. See this [list of database types](../functions_database_handling/overview.md#types).  |
| `ref long` | `flag` |  This returns a bit pattern that represents one or more of the following values: DB.ARRAY DB.CDF DB.CHILD DB.FILLED DB.MLF  |
| `ref string` | `default_value` |  This returns the default value of the column.  |
| `[ long` | `flag_filter ]` |  This optional argument can be used to get a filtered list of columns that have the specified flag set. For example, the 2nd CDF column from a table can be retrieved by calling this function with column_name = 2 and flag_filter = DB.CDF  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)

- [Database types and related byte lengths](../functions_database_handling/overview.md#types)
