# Get attribute length

## Syntax:
`function long xmlGetAttributeLength( long node, string attributeName )`

## Description
Get the length of an attribute.
This function may be used to determine the required size of the *data* argument supplied to [Get attribute value](get_attribute_value.md).

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is the node for which the length of an attribute is obtained.  |
| `string` | `attributeName` |  *attributeName* is the name of the attribute.  |

## Return values
| | |
|---|---|
| >= 0 | Success; Length of the attribute. |
| -1 | Error, or the indicated attribute does not exist. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)
