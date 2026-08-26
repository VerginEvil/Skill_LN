# tt.currency()

## Syntax:
`function boolean tt.currency( string cur(3), ref string cur_desc() mb, ref string thous_sign, ref string dec_sign, ref string symbol() )`

## Description
This returns information about a specified currency.

## Arguments
| | | |
|---|---|---|
| `string` | `cur(3)` |  The currency code.  |
| `ref string` | `cur_desc() mb` |  This returns the currency description.  |
| `ref string` | `thous_sign` |  This returns the thousands sign for the specified currency.  |
| `ref string` | `dec_sign` |  This returns the decimal sign for the specified currency.  |
| `ref string` | `symbol()` |  This returns the currency symbol.  |

## Return values
false error; currency not found
true success

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
