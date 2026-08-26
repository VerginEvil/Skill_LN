# tt.cdf()

## Syntax:
`function long tt.cdf( const string cdf, ref boolean active, ref boolean internal )`

## Description
This function returns information about the given Customer Defined Field (CDF) as defined for the current Package Combination.

## Arguments
| | | |
|---|---|---|
| `const string` | `cdf` |  The name of the CDF "<table>.cdf_..."  |
| `ref boolean` | `active` |  This indicates whether the CDF is currently marked as active. A CDF that is not yet available is never considered active.  |
| `ref boolean` | `internal` |  This indicates whether the CDF is marked for internal use (which should not be shared with e.g. Business Partners).  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | The CDF was not found |
| -2 | The length of the given field is incorrect |
| -3 | The given field is not a CDF |
| -4 | The table of the given CDF does not exist |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2110.
Note  From TIV level 2491 the return options -2 till -4 are available and the function is trusted

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
