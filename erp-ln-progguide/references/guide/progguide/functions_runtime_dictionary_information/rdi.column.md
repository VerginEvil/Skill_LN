# rdi.column()

## Syntax:
`function long rdi.column( string column_name(18), ref string domain_name(14), ref long offset, ref long size, ref long dept, ref long type, ref long flag, ref string default_value(.) )`

## Description
This returns information about a specified table column.

## Arguments
| | | |
|---|---|---|
| `string` | `column_name(18)` |  The name of the column about which you want to retrieve information.  |
| `ref string` | `domain_name(14)` |  This returns the name of the column's domain.  |
| `ref long` | `offset` |  This returns the position of the column in the row.  |
| `ref long` | `size` |  This returns the size of the column, in bytes. See this list of database types and related byte counts.  |
| `ref long` | `dept` |  This returns the depth of the column (array columns only).  |
| `ref long` | `type` |  This returns the database type of the column. For example, DB.LONG, DB.FLOAT, and so on. See this list of database types.  |
| `ref long` | `flag` |  This returns a bit pattern that represents one or more of the following values: DB.ARRAY DB.CDF DB.CHILD DB.FILLED  |
| `ref string` | `default_value(.)` |  This returns the default value of the column.  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
- Database types and related byte counts
