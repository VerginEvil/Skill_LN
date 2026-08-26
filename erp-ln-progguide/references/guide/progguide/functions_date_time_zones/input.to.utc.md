# input.to.utc()

## Syntax:
`function domain ttutc input.to.utc( const string value(), const string format() )`

## Description
This converts a string to a local date *or* local time based on a format.

## Arguments
| | | |
|---|---|---|
| `const string` | `value()` |  A date string *or* a time string (in local time).  |
| `const string` | `format()` |  Indicates the format of the input string. For a date string, use the substitution symbols %u *xxx* [, *lang*] . For a time string, use the substitution symbols %U *xxx* [, *lang*] .  |

## Return values
| | |
|---|---|
|  | the local date as the number of days since 01-01-0001 or the local time as the number of seconds since 00:00 hour depending on the format string.  |
| -1 | Error. The exact result is negative or greater than the maximum value 2^( BitCountOfLong-1) - 1 of the signed BitCountOfLong-bit range.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Return value
The local date or local time value depending on the format string. Or -1 if an error occurs (such as when there is no valid local date or local time value possible for the given string).

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
