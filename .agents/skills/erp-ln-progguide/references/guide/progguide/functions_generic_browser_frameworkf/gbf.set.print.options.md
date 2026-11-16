# gbf.set.print.options()

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.print.options( long print.options )`

## Description
This function sets the print options.

## Arguments
| | |
|---|---|
| GBF.PRINT.NO.ICONS | Icons descriptions will not be printed |
| GBF.PRINT.ICONS | Icons descriptions will be printed in between “ <” and “>” |
Whether or not the keys of the objects must be printed:
| | |
|---|---|
| GBF.PRINT.NO.KEYS | Key of object will not be printed |
| GBF.PRINT.KEYS | Key of object will be printed in between “[“ and “ ]” |
Whether the current tree contents must be printed or whether first the whole tree should be read:
| | |
|---|---|
| GBF.PRINT.NO.READ | Print only what is already current in memory |
| GBF.PRINT.READ | Before printing, first read the whole tree |
These options come in the place of the question dialog box whether to print the selection or the entire tree.
| | |
|---|---|
| GBF.PRINT.NO.SEL | Do not ask anything, just print the current selection only |
| GBF.PRINT.SEL | Before printing ask whether to print all or only the current selection |
The default print options of GBF is GBF.PRINT.DEFAULT which is:
GBF.PRINT.NO.ICONS + GBF.PRINT.NO.KEYS + GBF.PRINT.NO.READ + GBF.PRINT.SEL
However when an icon is added which has a description, then the GBF.PRINT.ICONS is automatically turned on.

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
