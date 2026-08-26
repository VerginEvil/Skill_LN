# ml_one_lang()

## Syntax:
`function string ml_one_lang( const string mlv, [ const string language ] )`

## Description
This function retrieves the value in a specific data language from a string variable.

## Arguments
| | | |
|---|---|---|
| `const string` | `mlv` |  a multi language value (string)  |
| `[ const string` | `language ]` |  a valid Data Language code  |

## Return values
The value in the specified data language'. If the optional argument 'language' is not specified: the value in the 'current data language'
This function can be used in SQL as well, to select values in just one language from the database.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Multi Language Data overview](overview.md)
- [Multi Language Data synopsis](synopsis.md)
- [Multi Language Data support code examples](examples.md)
- [ml_one_lang function](../functions_database_handling/ml_one_lang_function.md)
