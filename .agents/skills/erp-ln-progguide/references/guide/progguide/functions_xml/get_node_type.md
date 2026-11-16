# Get Node type

## Syntax:
`function long xmlGetType( long node )`

## Description
Get the type of a node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the type is obtained.  |

## Return values
| | |
|---|---|
|  | Success; Node type being one of XML_ELEMENT, XML_DTD, XML_DATA or XML_PI. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
