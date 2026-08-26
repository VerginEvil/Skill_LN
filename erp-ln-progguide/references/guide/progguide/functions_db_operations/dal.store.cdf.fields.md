# dal.store.cdf.fields()

## Syntax:
`#include <bic_dam>`
`function long dal.store.cdf.fields( string tbl.name )`

## Description
This function can be used to copy Customer Defined Fields from a source record to a target record of the same table, see also [dal.set.cdf.fields()](dal.set.cdf.fields.md).
It stores the values of the current table record of all Custom Defined Fields of the given table in memory. These values are used for the [dal.set.cdf.fields()](dal.set.cdf.fields.md).
In case the values for the same table are stored before, the storage is overwritten with the current values.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  the table name of the DAL.  |

## Return values
| | |
|---|---|
| 0 | OK (CDF fields are stored) |
| -1 | Table does not exist |
| -2 | Value of CDF cannot be read |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2460.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function must be called before function [dal.new.object()](dal.new.object.md), [dal.copy.object()](dal.copy.object.md) or [dal.change.object()](dal.change.object.md) is called. Do not place a retry point in between.
See [dal.set.cdf.fields()](dal.set.cdf.fields.md) for an example.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
- [CDF (Customer Defined Fields) handling overview](../functions_cdf/overview.md)
- [CDF (Customer Defined Fields) handling synopsis](../functions_cdf/synopsis.md)
