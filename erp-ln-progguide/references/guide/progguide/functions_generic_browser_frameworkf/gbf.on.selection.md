# gbf.on.selection()

## Syntax:
`#include <bic_gbf>`
`function void gbf.on.selection( long obj.id, long obj.type, long transition )`

## Description
This function will be called when the user clicks on an object. It has been made to create an extra possibility for the user to manipulate the state of the standard buttons through the function [gbf.set.buttonstate()](gbf.set.buttonstate.md). It is recommended to use this function only for these purposes. The obj.id gives the id of the selected object and obj.type contains the type of the object, for example, GBF.LEAF, GBF.INTERIOR or GBF.HEADER. When an end user selects an object, the programmer wants to know to which state the object is moving. For example, when an object is selected and the end user clicks on the object again, then its transition state is that the object is moving from the selected state to the deselected state, thus the transition is GBF.DESELECT. When an object is not yet selected and the end user clicks on it, the transition state is from the unselected state to the selected state, thus the transition is GBF.SELECT.
If option GBF.OPT.MUTI.ONSELECT, see function [gbf.init()](gbf.init.md),is used, this function will called with obj.id and obj.type set to zero on a multi select.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The obj.id of the selected object or zero(0) if called because multiple objects are selected.  |
| `long` | `obj.type` |  The type of object, GBF.LEAF, GBF.INTERIOR, GBF.HEADER, or zero(0) if called because multiple objects are selected  |
| `long` | `transition` |  The new state, GBF.SELECT or GBF.DESELECT  |

## Return values
None.

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
