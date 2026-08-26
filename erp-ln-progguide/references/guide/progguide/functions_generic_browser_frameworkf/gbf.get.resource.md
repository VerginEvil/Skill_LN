# gbf.get.resource()

## Syntax:
`#include <bic_gbf>`
`function long gbf.get.resource( long resource.type, ref void resource.value )`

## Description
Returns the current value for the given resource types. The arguments are given in name value pairs. For the possible resources see [gbf.set.resource()](gbf.set.resource.md). In almost all cases the *<type>* will be long (or a domain of basic type int, long, enumerate, bitset and so on.), except when the resource.type is DsNtitle, since in this case the *<type>* must be multibyte string.
This function may be used after the GBF run has finished to get the setting for this specific user, and restore them at the next run.
Note
When the Tree Control is used, it may very well be that the actual requested resources are NOT supported by this Tree Control. Nevertheless in these cases no error will be returned.

## Arguments
| | | |
|---|---|---|
| `long` | `resource.type` |  The resource type that is used to get the value. For a list of resource types see [gbf.set.resource()](gbf.set.resource.md).  |
| `ref void` | `resource.value` |  Returns the current value of the resource type.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ARG.ERROR | One or more of the given resource.value references is wrong  |
|  GBF.ILL.RESOURCE. TYPE  | Unknown resource type specified |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [gbf.set.resource()](gbf.set.resource.md)
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
