# iso.to.date()

## Syntax:
`function long iso.to.date( const string iso.date )`

## Description
This converts an ISO 8601 date string to a local date.
The following formats are supported:
- yyyy (returns a date representing January 1 of the specified year)
- yyyy-mm (returns a date representing the first day of the specified month in the specified year)
- yyyy-mm-dd (returns the specified local date)

## Arguments
| | | |
|---|---|---|
| `const string` | `iso.date` |  |

## Return values
| | |
|---|---|
| > 0 | The local date value. |
| 0 | An empty string was specified. |
| < 0 | Error. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2320.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2460 and process is a non trusted process

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
