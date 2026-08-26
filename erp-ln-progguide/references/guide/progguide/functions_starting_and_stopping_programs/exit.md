# exit()

## Syntax:
`function void exit( [ void exitvalue ] )`

## Description
When included in a 3GL program that is not activated by a 4GL program, *exit()* has the same effect as [end()](end.md) and [end()](end.md) in a 3GL program.
When included in a 4GL script, or in a 3GL program that is activated from a 4GL program with [zoom.to$()](zoom.to.md), an exit value is returned to the calling program. The *exitvalue* argument can be of any type (except an array). It is always converted to a string. If no exit value is specified, an empty string is returned.

## Arguments
| | | |
|---|---|---|
| `[ void` | `exitvalue ]` |  Exit value to be returned to the calling program. Implicit conversion of the supplied value from its original type to the string type is performed.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and In a not trusted process

## Related topics
- [Starting and stopping programs: overview and synopsis](overview_and_synopsis.md)
