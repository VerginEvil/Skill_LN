# tab$()

## Syntax:
`function string tab$( long num_expr )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to position the cursor at a specified column in the current window. If you use this function in the variable *spool.pr.line* for the function [spool.line()](../functions_spooling/spool.line.md), the printer is set to column *num_expr*.

## Arguments
| | | |
|---|---|---|
| `long` | `num_expr` |  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
