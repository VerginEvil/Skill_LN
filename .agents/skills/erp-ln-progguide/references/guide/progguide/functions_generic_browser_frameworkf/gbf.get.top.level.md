# gbf.get.top.level()

## Syntax:
`#include <bic_gbf>`
`function long gbf.get.top.level( )`

## Description
This function will be called by the GBF after it has been started to get the top level node(s).
The application should call for all nodes the function: [gbf.add.object()](gbf.add.object.md) with the appropriate arguments.

## Return values
| | |
|---|---|
| GBF.DO.CONTINUE or 0 | Successful completion, GBF will continue working |
| GBF.DO.ABORT | Abort GBF, which will end the GBF and return with an error, see [gbf.start()](gbf.start.md) |
| GBF.DO.EXIT | Finish GBF, which will end the GBF and return with 0, see [gbf.start()](gbf.start.md) |
Any return other that these values will be treated as if GBF.DO.ABORT has been returned.

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
