# utc.to.inputstr$()

## Syntax:
`function long utc.to.inputstr$( domain ttutc utc, string date.format(7), string time.format(7), ref string local.date(), ref string local.time() )`

## Description
This converts a UTC long format value to a local date string *and* a local time string.

## Arguments
| | | |
|---|---|---|
| `domain ttutc` | `utc` |  A UTC long format value.  |
| `string` | `date.format(7)` |  Indicates the format for the returned date string, by using the substitution symbols %u *xxx* [, *lang*]. The returned date string will always contain: 4 digits year, 2 digits month, 2 digits day. The order depends on the used language. No Separators are used.  |
| `string` | `time.format(7)` |  Indicates the format for the returned time string, by using the substitution symbols %U *xxx* [, *lang*]. The returned time string is always in the format HH:MM:SS  |
| `ref string` | `local.date()` |  The returned local date string.  |
| `ref string` | `local.time()` |  The returned local time string.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. For example: An illegal format is specified. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
