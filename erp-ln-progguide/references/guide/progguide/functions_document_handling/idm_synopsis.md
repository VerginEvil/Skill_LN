# Document handling in IDM synopsis
| | | |
|---|---|---|
| `long` | [dms.idm.create.doctype.attribute.list](dms.idm.create.doctype.attribute.list.md) | `()` |
| `[long]` | [dms.idm.list.add.doctype.attribute](dms.idm.list.add.doctype.attribute.md) | `(long i.attr.list, string i.attr.name, string i.attr.value, boolean i.attr.is.ident, [boolean i.attr.is.multi])` |
| `long` | [dms.idm.create.filter](dms.idm.create.filter.md) | `()` |
| `[long]` | [dms.idm.filter.set.mimetype](dms.idm.filter.set.mimetype.md) | `(long i.filter, string i.mimetype)` |
| `[long]` | [dms.idm.filter.set.filenamee](dms.idm.filter.set.filename.md) | `(long i.filter, string i.filename)` |
| `long` | [dms.idm.query.documents](dms.idm.query.documents.md) | `(string i.document.type, long i.attr.list, long i.filter, ref long o.nr.documents, ref long o.documents, ref string error.mesg)` |
| `long` | [dms.idm.query.response.get.first.document](dms.idm.query.response.get.first.document.md) | `(long i.documents)` |
| `long` | [dms.idm.query.response.get.next.document](dms.idm.query.response.get.next.document.md) | `(long i.document)` |
| `string` | [dms.idm.document.get.filename](dms.idm.document.get.filename.md) | `(long i.document)` |
| `string` | [dms.idm.document.get.mimetype](dms.idm.document.get.mimetype.md) | `(long i.document)` |
| `string` | [dms.idm.document.get.created.by](dms.idm.document.get.created.by.md) | `(long i.document)` |
| `string` | [dms.idm.document.get.created.timestamp](dms.idm.document.get.created.timestamp.md) | `(long i.document)` |
| `string` | [dms.idm.document.get.last.changed.by](dms.idm.document.get.last.changed.by.md) | `(long i.document)` |
| `string` | [dms.idm.document.get.last.changed.timestamp](dms.idm.document.get.last.changed.timestamp.md) | `(long i.document)` |
| `long` | [dms.idm.document.get.attribute](dms.idm.document.get.attribute.md) | `(ref string o.attr.value, long i.document, string i.attr.value, [long i.attr.element])` |
| `long` | [dms.idm.download.document](dms.idm.download.document.md) | `(long i.document, ref string io.document.file, ref string o.error.msg)` |
| `long` | [dms.idm.upload.document](dms.idm.upload.document.md) | `(string i.document.type, long i.attr.list, string i.filename, string i.display.name, string i.mimetype, boolean i.create.revision, ref long o.document, ref string error.mesg)` |
| `long` | [dms.idm.delete.document](dms.idm.delete.document.md) | `(long i.document, ref string o.error.mesg)` |

## Related topics
- [DMS Document handling API](overview.md)

- [Document Management (IDM) examples](idm_examples.md)
