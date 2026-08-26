# mb.coerce.to.sb()

## Syntax:
`function long mb.coerce.to.sb( ref string string$, [ long setid ] )`

## Description
This function converts a string from the [TSS](../misc/tss.md) character set to the external, native character set, assuring that each resulting character is a *single* byte. By default, the setting of the current user locale (single-byte or multibyte environment) or the installation locale (Unicode environment) determines the character set to which the string is converted. Code features in the string are skipped.
This function may be used when a string containing multibyte characters must be assigned to a single-byte string. Note that the conversion may result in *ambiguous* high ascii characters (see [TSS Encoding](../misc/tss.md)).

## Arguments
| | | |
|---|---|---|
| `ref string` | `string$` |   |
| `[ long` | `setid ]` |  If you do not want to base the conversion on the setting of the current user locale (single-byte or multibyte environment) or the installation locale (Unicode environment), use this optional argument to specify the ID of the TSS character set to be used during the converversion.  |

## Return values
| | |
|---|---|
| >= 0 | The number of bytes in the result string. |
| -1 | The conversion failed because some character could not be converted, or some converted character is not a *single* byte.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1641.

## Related topics
- [mb.export$()](mb.export.md)
- [mb.locale.enumerate()](mb.locale.enumerate.md)
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
