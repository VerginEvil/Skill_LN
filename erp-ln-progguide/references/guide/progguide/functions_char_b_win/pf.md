# pf$()

## Syntax:
`function string pf$( long num_expr )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to change the printer font settings. The following settings are available:
| | |
|---|---|
| 1 | large |
| 2 | small |
| 3 | middle |
| 4 | dblwide |
| 5 | nlq |
| 6 | italic |
| 7 | superscript |
| 8 | subscript |
| 9 | .font1 |
| 10 | font2 |
| ... | ... |
| 24 | font16 |
You define settings 9 to 24 in the printer information file of the particular printer (for example, $BSE/lib/printinf/m/m290).

## Arguments
| | | |
|---|---|---|
| `long` | `num_expr` |  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

spool.pr.line = pf$(2)
spool.line() | Set printer to small font
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
