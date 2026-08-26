# format.round()

## Syntax:
`function double format.round( double value, string format, [ long mode ] )`

## Description
The rounds a value according to a specified format.

## Arguments
| | | |
|---|---|---|
| `double` | `value` |  The value to be rounded.  |
| `string` | `format` |  The format for the returned value. For example %10.5f or %5.10g. See [sprintf$()](../functions_formatting_io/sprintf.md).  |
| `[ long` | `mode ]` |  This argument is optional. If it is not included, the default mode is 1. 0: truncate (for example, both 1.5 and 1.49 are rounded down to 1) 1: normal round (for example, 1.5 is rounded up to 2; 1.49 is rounded down to 1) 2: round up (for example, both 1.5 and 1.49 are rounded up to 2)  |

## Return values
The rounded value.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Mathematical operations overview](overview.md)
- [Mathematical operations synopsis](synopsis.md)
