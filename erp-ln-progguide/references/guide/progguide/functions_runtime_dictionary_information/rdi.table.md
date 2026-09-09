# rdi.table()

## Syntax:
`function long rdi.table( string table_name(9), ref long no_keys, ref long no_columns, ref long int_length, ref long real_length, [ ref long no_cdf, ref boolean mlf_table_all_languages ] )`

## Description
This returns information about a specified table.

## Arguments
| | | |
|---|---|---|
| `string` | `table_name(9)` |  The table name (omit the leading 't').  |
| `ref long` | `no_keys` |  This returns the number of indices that have been created on the table.  |
| `ref long` | `no_columns` |  This returns the number of columns that are in the table, including the following columns: Refcntd Refcntu _compnr _dlock _index< *number* > (a column for each index)  |
| `ref long` | `int_length` |  This returns the length of the internal buffer that is needed for a row in the table and its internal data like '_compnr' and '_dlock'.  |
| `ref long` | `real_length` |  This returns the length of a row in the table without the internal data. This length is at least the sum of the byte lengths of the individual columns. See this [list of database types and related byte lengths](../functions_database_handling/overview.md#types).  |
| `[ ref long` | `no_cdf ]` |  This optional argument returns the number of CDF columns that are in the table.  |
| `[ ref boolean` | `mlf_table_all_languages ]` |  This optional argument returns whether the table is configured for selection of all languages of its multi language fields, even when the [resource](../misc/bshell_resources.md) *mle_all_data_languages* is set to the value 0 (indicating that by default only the current language must be selected). If this optional argument is used, then first the *no_cdf* argument must be supplied. This optional argument can be used as of [TIV level 2140](../tiv/tiv_2140.md).  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)

- [Database types and related byte lengths](../functions_database_handling/overview.md#types)
