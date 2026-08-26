# reactivate()

## Syntax:
`function void reactivate( long processno )`

## Description
This activates the specified sleeping process.

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and The process to reactivate should be a not trusted process

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
