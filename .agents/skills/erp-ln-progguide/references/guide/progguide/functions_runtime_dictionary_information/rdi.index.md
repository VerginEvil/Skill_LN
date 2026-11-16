# rdi.index()

## Syntax:
`function long rdi.index( string table_name(9), long index_no, ref long parts(32, 3), ref boolean duplicate, ref boolean active, [ ref string index_name ] )`

## Description
This returns information about a specified index.

## Arguments
| | | |
|---|---|---|
| `string` | `table_name(9)` |  The name of the relevant table (omit the leading 't').  |
| `long` | `index_no` |  The index ID.  |
| `ref long` | `parts(32, 3)` |  This returns the start position, length, and type of the index parts (up to a maximum of 32 parts): parts(i,1) Start position of part *i* in record parts(i,2) Length of part *i*. See this [list of database types and related byte lengths](../functions_database_handling/overview.md#types). parts(i,3) Type of part *i*. See this [list of database types](../functions_database_handling/overview.md#types).  |
| `ref boolean` | `duplicate` |  Indicates whether or not duplicate values are permitted. Possible values are: TRUE duplicates permitted FALSE duplicates not permitted  |
| `ref boolean` | `active` |  Indicates whether or not the index is active. Possible values are: TRUE index is active FALSE index is not active  |
| `[ ref string` | `index_name ]` |  If specified the name of the index (e.g. "ttadv112._index2") is returned in this parameter. This parameter is available from TIV 2520.  |

## Return values
The number of filled parts.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)

- [Database types and related byte lengths](../functions_database_handling/overview.md#types)
