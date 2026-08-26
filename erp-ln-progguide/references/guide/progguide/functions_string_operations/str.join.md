# str.join$()

## Syntax:
`function string str.join$( const string separator$, void ... )`

## Description
Joins the specified arguments to a single string. Non-string arguments are first converted to strings. The strings are separated with the specified separator.
Contrary to [concat$()](concat.md), the separator may be a string of more than one character.

## Arguments
| | | |
|---|---|---|
| `const string` | `separator$` |  a separator string, may be an empty string  |
| `void` | `...` |  the values to join into one string  |

## Return values
A single string containing all specified values separated by the specified separator

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.

## Example
```

string	result$(100)

result$ = str.join$(", ", "a", "comma", "separated", "string", "with", 7, "words")
| result$ now contains "a, comma, separated, string, with, 7, words"

result$ = str.join$(" OR ",
        "tdsls400.corg = tdsls.corg.contracts",
        "tdsls400.corg = tdsls.corg.quotations",
        "tdsls400.corg = tdsls.corg.service")
| result$ now contains "tdsls400.corg = tdsls.corg.contracts OR tdsls400.corg = tdsls.corg.quotations OR tdsls400.corg = tdsls.corg.service"
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
