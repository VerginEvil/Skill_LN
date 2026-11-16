# dms.dochub.list.add.application.attribute

## Syntax:
`#include <bic_dms>`
`function [long] dms.dochub.list.add.application.attribute( long i.attr.list, string i.attr.name, string i.attr.value )`

## Description
Add an attribute with its value to the given attribute list.

## Arguments
| | | |
|---|---|---|
| `long` | `i.attr.list` |  The handle to the attribute list as returned by a previous call to [dms.dochub.create.application.attribute.list](dms.dochub.create.application.attribute.list.md)  |
| `string` | `i.attr.name` |  The name of the attribute.  |
| `string` | `i.attr.value` |  The value of the attribute.  |

## Return values
| | |
|---|---|
| 0 | An error occurred. |
| <>0 | A handle to the added attribute. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)

- [Document handling via Document Hub synopsis](dochub_synopsis.md)

- [Document Management via Document Hub examples](dochub_examples.md)
