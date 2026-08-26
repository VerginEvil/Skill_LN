# Get attribute name length

## Syntax:
`function long xmlGetAttributeNameLength( long node, int attributeNr )`

## Description
Get the length of an attribute name.
This function may be used to determine the required size of the *argumentName* argument supplied to [Get attribute name](get_attribute_name.md).

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the length of an attribute name is obtained.  |
| `int` | `attributeNr` |  *attributeNr* is the 1 based index in the list of attributes for this node.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Length of the attribute name |
| -1 | Error, or the indicated attribute does not exist.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
