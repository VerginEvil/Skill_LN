# dms.idm.document.get.attribute

## Syntax:
`#include <bic_dms>`
`function long dms.idm.document.get.attribute( string o.attr.value, long i.document, string i.attr.name, integer [i.attr.element] )`

## Description
Get the value of a document type attribute of a document in a query response.

## Arguments
| | | |
|---|---|---|
| `string` | `o.attr.value` |  The value of the document type attribute of the document.  |
| `long` | `i.document` |  The handle to a document in a query response as returned by an earlier call to [dms.idm.query.documents](dms.idm.query.documents.md)  |
| `string` | `i.attr.name` |  Document type attribute name.  |
| `integer` | `[i.attr.element]` |  The element to be retrieved in case of a multi-value attribute.  |

## Return values
| | |
|---|---|
| 0 | Attribute value retrieved. |
| <>0 | An error occurred. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)
- [Document handling in IDM synopsis](idm_synopsis.md)
- [Document Management (IDM) examples](idm_examples.md)
