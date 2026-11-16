# l.expr()

## Syntax:
`function long l.expr( long expr_id, [ void value, boolean suppressError ] )`

## Description
Executes (or evaluates) an expression previously compiled by [expr.compile()](expr.compile.md). The result is always converted to a long.

## Arguments
| | | |
|---|---|---|
| `long` | `expr_id` |  The ID of the compiled expression, as returned by [expr.compile()](expr.compile.md).  |
| `[ void` | `value ]` |  If the expression contains the characters '$$', the value specified by this argument is substituted for those characters. This is an optional argument.  |
| `[ boolean` | `suppressError ]` |  Suppresses errors  |

## Return values
The result of the expression converted to an integer value.
Notice that signed 64-bit values are used for integer arithmetic in runtime expression evaluation.
In older porting sets (with [bshell TIV level](../tiv/tiv_overview.md) less than [2000](../tiv/tiv_2000.md)), signed 32-bit values are used for integer arithmetic in runtime expression evaluation.
If the resulting integer value is greater than the maximum value 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) - 1 of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range, then that maximum value is returned.
If the resulting integer value is less than the minimum value -2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range, then that minimum value is returned.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  You can execute compiled expressions multiple times without recompiling. The current values of the variables are used each time.

## Related topics
- [Runtime expressions: overview and synopsis](overview_and_synopsis.md)
