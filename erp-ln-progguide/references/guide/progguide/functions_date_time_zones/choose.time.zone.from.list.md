# choose.time.zone.from.list()

## Syntax:
`function long choose.time.zone.from.list( ref string new.timezone )`

## Description
This starts a session where the user can choose a time zone from a list. The function then calls *set.timezone()* with the time zone selected by the user.

## Arguments
| | | |
|---|---|---|
| `ref string` | `new.timezone` |  This argument is used to return the set timezone to the caller.  |

## Return values
| | |
|---|---|
| 0 | New time zone set. |
| -1 | User aborted operation; time zone not set . |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
