# tss.uni.normalized$()

## Syntax:
`function string tss.uni.normalized$( const string source$, long tss.uni.normalization.form )`

## Description
Normalize the supplied *source$* string according to the specified normalization form and return the result.

## Arguments
| | | |
|---|---|---|
| `const string` | `source$` |  Input string (encoded in TSS) to be normalized.  |
| `long` | `tss.uni.normalization.form` |  The Unicode Normalization Form to be applied. See Unicode Standard Annex #15: Unicode Normalization Forms. The following named constants are available.  |
-
-

## Return values
| | |
|---|---|
| <> "" | Success. A multibyte string, containing a copy of the supplied *source$* string, normalized according to the specified normalization form.  |
| "" | Error. The supplied *tss.uni.normalization.form* is not one of the valid normalization form values.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2520.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
