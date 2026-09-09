# brp.open.language()

## Syntax:
`function long brp.open.language( string rep_name(16), string lang, string device(14), long mode )`

## Description
This is the same as [brp.open()](brp.open.md) in most respects, except that it includes a language argument. This enables you to specify a language for the report other than the default user language.

## Arguments
| | | |
|---|---|---|
| `string` | `rep_name(16)` |    |
| `string` | `lang` |    |
| `string` | `device(14)` |    |
| `long` | `mode` |    |

## Return values
> 0 an ID for the activated report
0 report could not be activated
-1 spooler could not be opened

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2120 and The report should be a tx report

## Example
See [brp.open()](brp.open.md).

## Related topics
- [Reports overview and synopsis](overview_and_synopsis.md)

- [Spooling overview and synopsis](../functions_spooling/overview_and_synopsis.md)
