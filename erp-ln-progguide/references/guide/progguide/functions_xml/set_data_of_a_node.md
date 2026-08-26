# Set data of a Node

## Syntax:
`function long xmlSetData( long node, string data )`

## Description
Set the data of an XML_DATA or XML_PI node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  node is the node for which the data is set.  |
| `string` | `data` |  data contains the new data value.  |

## Return values
| | |
|---|---|
| <> 0 | Success; Value of parameter *node* when successful.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
