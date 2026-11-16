# cl.screen()

## Syntax:
`function void cl.screen( long column, long row, long no_of_cols, long no_of_rows )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This clears a specified area of the current window. The changes become visible on screen only after you call [refresh()](refresh.md)

## Arguments
| | | |
|---|---|---|
| `long` | `column` |  The column and row co-ordinates for the top left corner of the area to be cleared.  |
| `long` | `row` |    |
| `long` | `no_of_cols` |  The number of columns to be cleared.  |
| `long` | `no_of_rows` |  The number of rows to be cleared.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

cl.screen( 1, 5, 80, 6 )
refresh()
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
