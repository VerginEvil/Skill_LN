# db.set.error.bypass.on()

## Syntax:
`function long db.set.error.bypass.on( [ boolean with.retry ] )`

## Description
This function flushes all buffered database actions in the current transaction before setting the error.bypass and error.bypass.with.retry flags. If any of the database actions results in a retryable error a jump is made to the db.retry.point(). If any of the actions results in a fatal error, then the process is terminated. If any error occurs then the values of error.bypass and error.bypass.with.retry are not modified. After successful flush, sets the value of error.bypass to true. The value of error.bypass.with.retry is set to the value specified by the with.retry argument, or to false if the argument is not given.
Note that not all errors can be handled by using this function. See Error Handling in [Database operations overview](overview.md).

## Arguments
| | | |
|---|---|---|
| `[ boolean` | `with.retry ]` |  The value used to set the error.bypass.with.retry flag.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2010.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
