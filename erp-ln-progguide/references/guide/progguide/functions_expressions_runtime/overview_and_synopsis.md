# Runtime expressions: overview and synopsis

## Overview
Use these functions to compile and evaluate expressions at runtime. This is particularly useful when expressions or formulas are stored in a database or can be entered by a user.
Use of these functions increases system load and should be avoided, where possible.

## Synopsis
| | | |
|---|---|---|
| `double` | [d.expr()](d.expr.md) | `( long expr_id [, arg] )` |
| `long` | [expr.compile()](expr.compile.md) | `( "expression" )` |
| `void` | [expr.free()](expr.free.md) | `( long expr_id )` |
| `long` | [l.expr()](l.expr.md) | `( long expr_id [, arg] )` |
| `string` | [s.expr$()](s.expr.md) | `( long expr_id [, arg] )` |
