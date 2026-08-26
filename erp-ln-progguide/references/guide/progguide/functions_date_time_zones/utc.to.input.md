# utc.to.input()

## Syntax:
`function string utc.to.input( domain ttutc lvalue, const string format() )`

## Description
This converts a UTC long format value to an input date string *or* an input time string (in local time). The format specified determines whether the function returns a date string or a time string.

## Arguments
| | | |
|---|---|---|
| `domain ttutc` | `lvalue` |  A UTC long format value.  |
| `const string` | `format()` |  |

## Return values
| |
|---|
| The representation of lvalue in the given format. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
