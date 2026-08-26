# db.indexinfo()

## Syntax:
`function long db.indexinfo( long table_id, long index_nr, ref long index_info(32, 3), ref long indexparts, ref boolean indexdups, ref boolean indexactive, [ ref string index_name ] )`

## Description
This returns information about the parts of a specified index.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `long` | `index_nr` |  The index number.  |
| `ref long` | `index_info(32, 3)` |  This returns the start position, length, and type of the index parts (up to a maximum of 32 parts): index_info(i,1) Start position in the logical record of part i of the index. index_info(i,2) Length of part i. index_info(i,3) Type of part i. The possible values are: DB.BYTE DB.TIME DB.INTEGER DB.TEXT DB.LONG DB.MAIL DB.FLOAT DB.ENUM DB.DOUBLE DB.BITSET DB.STRING DB.COMBINED DB.DATE DB.MULTIBYTE  |
| `ref long` | `indexparts` |  Returns the number of parts in the index.  |
| `ref boolean` | `indexdups` |  Indicates whether or not duplicate values are permitted.  |
| `ref boolean` | `indexactive` |  Indicates whether or not the index is active.  |
| `[ ref string` | `index_name ]` |  If specified the name of the index (e.g. "ttadv112._index2") is returned in this parameter. This parameter is available from TIV 2520.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
