# iso.to.utc()

## Syntax:
`function domain ttutc iso.to.utc( const string iso.string )`

## Description
This converts a string, representing a time in ISO 8601 format into a UTC long value.
The following formats are supported:
- yyyy-mm-ddThh:mm:ssZ (GMT)
- yyyy-mm-ddThh:mm:ss+hh:mm
- yyyy-mm-ddThh:mm:ss-hh:mm
- yyyy-mm-ddThh:mm:ss (interpreted as local date/time)

## Arguments
| | | |
|---|---|---|
| `const string` | `iso.string` |  |

## Return values
| | |
|---|---|
| > 0 | The UTC long format value. |
| 0 | An empty string was specified. |
| < 0 | Error. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
