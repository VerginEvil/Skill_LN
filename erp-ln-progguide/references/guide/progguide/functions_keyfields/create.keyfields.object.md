# create.keyfields.object()

## Syntax:
`function long create.keyfields.object( const string tablename, [ long collection ] )`

## Description
Create an object which can hold the key fields and the corresponding values referring to one record of the passed database table. The key fields of index 1 are used.

## Arguments
| | | |
|---|---|---|
| `const string` | `tablename` |  the name of the table for which the key fields will be stored  |
| `[ long` | `collection ]` |  optional id of a key fields collection to which this key field object will be added. A key fields collection must be created with the function: [create.keyfields.collection()](create.keyfields.collection.md)  |

## Return values
| | |
|---|---|
| <> 0 | The id of the created key fields object |
| 0 | When this function fails |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Key fields Object overview](overview.md)

- [Key fields object synopsis](synopsis.md)
