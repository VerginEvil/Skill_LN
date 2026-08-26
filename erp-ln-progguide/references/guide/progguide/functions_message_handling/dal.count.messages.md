# dal.count.messages()

## Syntax:
`function long dal.count.messages( long i.type )`

## Description
This returns the number of DAL messages of the specified type that are currently in the message buffer.

## Arguments
| | | |
|---|---|---|
| `long` | `i.type` |  A message type. Parameter i.type should be one of the following values: `MSG.ALL, MSG.ERROR, MSG.WARNING, MSG.INFO`.  |

## Return values
The number of DAL messages of the specified type.

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
