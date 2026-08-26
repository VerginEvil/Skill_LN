# cmf.setCategories()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setcategories( long mid, string categories )`

## Description
Sets the categories of the message identified by *mid* to the value *categories.* Categories are supplied in a comma delimited list. Mail clients such as Microsoft Outlook make use of categories and all categories used in Outlook can be used here.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `string` | `categories` |  Message category.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error (most likely invalid object id). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
