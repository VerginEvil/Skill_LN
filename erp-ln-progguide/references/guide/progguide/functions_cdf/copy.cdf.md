# copy.cdf()

## Syntax:
`function long copy.cdf( long dest.table.id, long src.table.id )`

## Description
This function facilitates the application in the task of carrying forward the information in the CDFs through the business process. The function will copy CDFs from a source record buffer to a destination record buffer if the destination table has a CDF with the same name.
Example:
copy.cdf( ttdsls101, ttdsls401 )
Example:
```

	  quotation.line.table = db.bind("tdsls101", my.quot.line.buf )
	  order.line.table = db.bind("tdsls401, my.order.line.buf )
	  . . .
	  copy.cdf(quotation.line.table, order.line.table)
```

## Arguments
| | | |
|---|---|---|
| `long` | `dest.table.id` |  destination table  |
| `long` | `src.table.id` |  source table  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [CDF (Customer Defined Fields) handling overview](overview.md)
- [CDF (Customer Defined Fields) handling synopsis](synopsis.md)
