# d.expr()

## Syntax:
`function double d.expr( long expr_id, [ void value, boolean suppressError ] )`

## Description
Executes (or evaluates) an expression previously compiled by [expr.compile()](expr.compile.md). The result is always converted to a double.

## Arguments
| | | |
|---|---|---|
| `long` | `expr_id` |  The ID of the compiled expression, as returned by [expr.compile()](expr.compile.md).  |
| `[ void` | `value ]` |  If the expression contains the characters '$$', the value specified by this argument is substituted for those characters. This is an optional argument.  |
| `[ boolean` | `suppressError ]` |  Suppresses errors  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Return value
The result of the expression converted to a double.
Note  You can execute compiled expressions multiple times without recompiling. The current values of the variables are used each time.

## Related topics
- [Runtime expressions: overview and synopsis](overview_and_synopsis.md)
