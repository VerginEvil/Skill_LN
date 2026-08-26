# tt.cdf.label()

## Syntax:
`function long tt.cdf.label( const string cdf, ref string labelCode )`

## Description
This function returns information about the given Customer Defined Field (CDF) as defined for the current Package Combination.

## Arguments
| | | |
|---|---|---|
| `const string` | `cdf` |  The name of the CDF "<table>.cdf_..."  |
| `ref string` | `labelCode` |  This returns the found label code, if no label code present an empty string is returned.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | The CDF was not found |
| -2 | The length of the given field is incorrect |
| -3 | The given field is not a CDF |
| -4 | The table of the given CDF does not exist |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2491.
Note  If the label code is replaced by personalization than the original label code is returned. Not the personalized one.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
