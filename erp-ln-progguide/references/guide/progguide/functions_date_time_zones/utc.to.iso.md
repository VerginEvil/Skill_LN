# utc.to.iso()

## Syntax:
`function string utc.to.iso( domain ttutc utc, [ long format ] )`

## Description
This converts a UTC into a string representation of the UTC in ISO 8601 format.

## Arguments
| | | |
|---|---|---|
| `domain ttutc` | `utc` |  A UTC long format value.  |
| `[ long` | `format ]` |  Can be one of the following constants:  |

## Return values
The string representation of the UTC in ISO 8601 format. If an invalid UTC value is specified, a string is returned with all values set to 0, e.g. 0000-00-00T00:00:00+00:00

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
