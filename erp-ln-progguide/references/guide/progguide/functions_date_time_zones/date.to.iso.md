# date.to.iso()

## Syntax:
`function string date.to.iso( long local.date )`

## Description
This converts a local date to an ISO 8601 date string. This is a string with the format: yyyy-mm-dd

## Arguments
| | | |
|---|---|---|
| `long` | `local.date` |  A local date value.  |

## Return values
The string representation of the local date in ISO 8601 format. If an invalid local date is specified, the following string is returned: "0000-00-00"

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2320.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2460 and process is a non trusted process

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
