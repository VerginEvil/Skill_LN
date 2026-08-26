# to.group()

## Syntax:
`function boolean to.group( long group_number )`

## Description
Use this to make the first form on which the specified group occurs the current form. This function is relevant to dynamic forms only.
In a well-designed GUI, users (and not the application) select and initiate the actions to be performed. Using *to.group()* removes control from the user. Therefore it does not conform to good GUI design principles.

## Arguments
| | | |
|---|---|---|
| `long` | `group_number` |   |

## Return values
true success
false group not found

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
