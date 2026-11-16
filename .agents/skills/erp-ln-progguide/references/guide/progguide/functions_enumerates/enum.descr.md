# enum.descr$()

## Syntax:
`function string enum.descr$( string domain_code(12), enum_expr, [ string language_code ] )`

## Description
This returns the description associated with a specific value in an enumerated domain.

## Arguments
| | | |
|---|---|---|
| `string` | `domain_code(12)` |  The name of the domain. The domain must be of type enumerated.  |
|  | `enum_expr` | One of the possible values of the enumerated domain. |
| `[ string` | `language_code ]` |  To retrieve the description in a language other than the user language, specify the relevant language code in this argument. This is an optional argument. The default language is the language of the user. Note that the language code of the user is available in the predefined, read-only variable *language$*.  |

## Return values
The description of the specified enumerate value, either in the current user language or in another specified language.
The function returns an empty string, and displays an error message, if an unknown domain is specified or if no description exists in the data dictionary for the specified language.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
This example assumes an enumerated domain 'tcyesno' with two possible constants: 'tcyesno.yes' and 'tcyesno.no'. It also assumes that 1 is the language code for Dutch, 2 is the language code for English, and 3 is the language code for German. English is the current user language.
```

domain    tcyesno active     | enumerated domain
string    descr(25)

active = tcyesno.no
descr = enum.descr$("tcyesno", active, "1")  | descr contains "nee"
descr = enum.descr$("tcyesno", active)       | descr contains "no"
descr = enum.descr$("tcyesno", active, "3")  | descr contains
"nein"
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)

- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
