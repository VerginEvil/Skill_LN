# on.drop()

## Syntax:
`function void on.drop( long from.pid, long collection, boolean copy )`

## Description
Call back function which is passed in function [enable.drop()](enable.drop.md). This function will be called when a drop event from the associated session arrives. In this function the business logic related to the drop operation must be implemented. In case database table updates are done in this function, the function must also commit the transaction.

## Arguments
| | | |
|---|---|---|
| `long` | `from.pid` |  process id of the session from which the objects are dropped  |
| `long` | `collection` |  collection of keyfield objects which are dropped on this session  |
| `boolean` | `copy` |  when true, the user indicated that a copy operation is requested (CTRL key pressed during drop operation). Otherwise a move operation is required  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Composite Sessions overview](overview.md)
- [Composite Sessions synopsis](synopsis.md)
- [Composite Sessions Code Examples](examples.md)
