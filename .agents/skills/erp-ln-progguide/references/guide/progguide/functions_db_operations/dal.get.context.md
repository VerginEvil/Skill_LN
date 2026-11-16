# dal.get.context()

## Syntax:
`#include <bic_dam>`
`function long dal.get.context( )`

## Description
Returns the context the DAL Server is running in.

## Return values
| | | | |
|---|---|---|---|
| 1 | CTX_DATA_INPUT | Data Input | This context is set by the 4GL engine when an end-user is entering data on a form |
| 2 | CTX_DATA_CHECK | Data Check | This context is set by the 4GL engine when an end-user does an action, like pressing save or executing a form command. |
| 3 | CTX_PROCESS | Process | This context is the default context. It is used for process and print sessions, but also for 3GL programs. |
| 4 | CTX_INTEGRATION | Integration | This context is set when the DAL is used via the BOL. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
