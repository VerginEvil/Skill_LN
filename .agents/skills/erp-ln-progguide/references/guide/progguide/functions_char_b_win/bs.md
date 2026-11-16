# bs$()

## Syntax:
`function string bs$( [ long num_expr ] )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to position the cursor *num_expr* positions to the left. If you do not specify the *num_expr* argument, the default number of positions is 1.

## Arguments
| | | |
|---|---|---|
| `[ long` | `num_expr ]` |  The number of positions to go to the left, default 1  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

			print bs$(4) | Move cursor 4 positions to the left refresh()
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
