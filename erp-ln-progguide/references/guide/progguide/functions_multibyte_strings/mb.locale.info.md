# mb.locale.info()

## Syntax:
`function string mb.locale.info( long info_flag, [ const string locale_name ] )`

## Description
This function returns information about the current locale.

## Arguments
| | | |
|---|---|---|
| `long` | `info_flag` |  Specifies the required information. The possible values are:  |
| `[ const string` | `locale_name ]` |  Specifies the locale name of the locale for which the information is requested. If this parameter is omitted the current locale is used.  |

## Return values
A string containing the requested information. Where applicable, [lval()](../functions_string_operations/lval.md) can be used to convert the string to a long.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [mb.locale.enumerate()](mb.locale.enumerate.md)
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
