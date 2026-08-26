# donut.set.innersubtitle()

## Syntax:
`function long donut.set.innersubtitle( long i.donutid, const string i.donutsubtitle, [ long i.size, const string i.style ] )`

## Description
This function sets the inner subtitle of the donut.

## Arguments
| | | |
|---|---|---|
| `long` | `i.donutid` |  The id returned by the function donut.new.  |
| `const string` | `i.donutsubtitle` |  The title that is displayed just below the donut title inside the donut. The subtitle uses default other styling, and a smaller font, then the donut title in LN UI.  |
| `[ long` | `i.size ]` |  Font size of the title. Options: DONUT.INNERTITLE.SIZE.STANDARD DONUT.INNERTITLE.SIZE.LARGE DONUT.INNERTITLE.SIZE.XLARGE Default: DONUT.INNERTITLE.SIZE.STANDARD  |
| `[ const string` | `i.style ]` |  Font style of the title. Options: DONUT.INNERTITLE.STYLE.STANDARD DONUT.INNERTITLE.STYLE.BOLD Default: DONUT.INNERTITLE.STYLE.STANDARD  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Failure, probably the i.donutid was not correct. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Donut overview and synopsis](overview_and_synopsis.md)
