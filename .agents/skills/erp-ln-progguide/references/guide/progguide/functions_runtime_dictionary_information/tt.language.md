# tt.language()

## Syntax:
`function boolean tt.language( string lang, ref string desc() mb, ref string dec_sign, ref string thous_sign, ref string date_sep, ref string time_sep )`

## Description
This returns information about a specified language.

## Arguments
| | | |
|---|---|---|
| `string` | `lang` |  The language for which you want to retrieve information.  |
| `ref string` | `desc() mb` |  This returns the language description.  |
| `ref string` | `dec_sign` |  This returns the decimal sign defined for the language.  |
| `ref string` | `thous_sign` |  This returns the thousands sign defined for the language.  |
| `ref string` | `date_sep` |  This returns the date separator defined for the language.  |
| `ref string` | `time_sep` |  This returns the time separator defined for the language.  |

## Return values
false error; language not found
true success

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
