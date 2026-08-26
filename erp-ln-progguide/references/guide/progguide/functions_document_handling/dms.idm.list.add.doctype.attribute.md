# dms.idm.list.add.doctype.attribute

## Syntax:
`#include <bic_dms>`
`function [long] dms.idm.list.add.doctype.attribute( long i.attr.list, string i.attr.name, string i.attr.value, boolean i.attr.is.ident, boolean i.attr.is.multi )`

## Description
Add an attribute with its value to the given attribute list.

## Arguments
| | | |
|---|---|---|
| `long` | `i.attr.list` |  The handle to the attribute list as returned by a previous call to [dms.idm.create.doctype.attribute.list](dms.idm.create.doctype.attribute.list.md)  |
| `string` | `i.attr.name` |  The name of the attribute.  |
| `string` | `i.attr.value` |  The value of the attribute.  |
| `boolean` | `i.attr.is.ident` |  Whether or not the attribute is an identifying attribute Only relevant when the attribute list is used for an upload request which should create a new revision. The identifying attributes are used to decide whether a document already exists or not.  |
| `boolean` | `i.attr.is.multi` |  This optional argument must be set to true when the attribute is a multi-value attribute. Multi-value attributes are supported from Enterprise Server 10.8 onwards.  |

## Return values
| | |
|---|---|
| 0 | An error occurred. |
| <>0 | A handle to the added attribute. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [DMS Document handling API](overview.md)
- [Document handling in IDM synopsis](idm_synopsis.md)
- [Document Management (IDM) examples](idm_examples.md)
