# inputstr.to.utc()

## Syntax:
`function domain ttutc inputstr.to.utc( const string date.inputstr(), string date.format(7), const string time.inputstr(), string time.format(7) )`

## Description
This converts the specified local date *and* time input strings to UTC long format.

## Arguments
| | | |
|---|---|---|
| `const string` | `date.inputstr()` |  A date string (in local time).  |
| `string` | `date.format(7)` |  Indicates the format of the date string, by using the substitution symbols %D *xxx* [, *lang*] .  |
| `const string` | `time.inputstr()` |  A time string (in local time).  |
| `string` | `time.format(7)` |  Indicates the format of the time string, by using the substitution symbols %U *xxx* [, *lang*].  |

## Return values
| | |
|---|---|
|  | The UTC long format value. |
| -1 | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
