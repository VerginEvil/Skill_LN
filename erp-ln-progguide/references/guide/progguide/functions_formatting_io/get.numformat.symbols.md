# get.numformat.symbols()

## Syntax:
`function long get.numformat.symbols( ref string decimal$, ref string grouping$ )`

## Description
Determine which decimal sign and thousand separator are currently being used.

## Arguments
| | | |
|---|---|---|
| `ref string` | `decimal$` |  The current decimal sign will be returned in this string.  |
| `ref string` | `grouping$` |  The current thousand separator will be returned in this string.  |

## Return values
| | |
|---|---|
| 0 | The returned decimal sign and thousand separator have the original, user defined, values. |
| 1 | The returned decimal sign and thousand separator have been set with the function set.numformat.symbols() |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Formatting input and output - overview and synopsis](overview_and_synopsis.md)
