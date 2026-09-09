# mb.locale.info()

## Syntax:
`function string mb.locale.info( long info_flag, [ const string locale_name ] )`

## Description
This function returns information about the current locale.

## Arguments
| | |
|---|---|
| TSS_GET_TSS_CHARACTERSET_ID | returns the character set id |
| TSS_GET_LOCALE_NAME | returns the locale name |
| TSS_GET_NLS_NAME | returns the NLS name |
| TSS_GET_TSS_NAME | returns the name of the character set |
| TSS_GET_IFACTOR | returns the internal mb factor |
| TSS_GET_EFACTOR | returns the external mb factor (also known as the database factor) |

## Return values
A string containing the requested information. Where applicable, [lval()](../functions_string_operations/lval.md) can be used to convert the string to a long.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [mb.locale.enumerate()](mb.locale.enumerate.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
