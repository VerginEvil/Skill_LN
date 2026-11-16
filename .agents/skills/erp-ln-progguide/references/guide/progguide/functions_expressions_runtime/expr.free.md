# expr.free()

## Syntax:
`function void expr.free( long expr_id )`

## Description
This frees the memory allocated to a compiled expression. *expr_id* is the ID of the compiled expression, as returned by [expr.compile()](expr.compile.md) It is important to call this function when you have finished with an expression.

## Arguments
| | | |
|---|---|---|
| `long` | `expr_id` |  The ID of the compiled expression.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime expressions: overview and synopsis](overview_and_synopsis.md)
