# get.num.keyfields.object()

## Syntax:
`function long get.num.keyfields.object( long object )`

## Description
Get the number of key field objects in this collection.

## Arguments
| | | |
|---|---|---|
| `long` | `object` |  ID of the key fields collection which must be returned by a previous call to [create.keyfields.collection()](create.keyfields.collection.md)  |

## Return values
| | |
|---|---|
| >= 0 | the number of child nodes. |
| < 0 | when an invalid collection id is passed |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Key fields Object overview](overview.md)
- [Key fields object synopsis](synopsis.md)
