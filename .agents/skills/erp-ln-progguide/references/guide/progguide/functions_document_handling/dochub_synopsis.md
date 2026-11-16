# Document handling via Document Hub synopsis
| | | |
|---|---|---|
| `long` | [dms.dochub.create.application.attribute.list](dms.dochub.create.application.attribute.list.md) | `()` |
| `[long]` | [dms.dochub.list.add.application.attribute](dms.dochub.list.add.application.attribute.md) | `(long i.attr.list, string i.attr.name, string i.attr.value)` |
| `long` | [dms.dochub.create.filter](dms.dochub.create.filter.md) | `()` |
| `[long]` | [dms.dochub.filter.set.mimetype](dms.dochub.filter.set.mimetype.md) | `(long i.filter, string i.mimetype)` |
| `[long]` | [dms.dochub.filter.set.filenamee](dms.dochub.filter.set.filename.md) | `(long i.filter, string i.filename)` |
| `long` | [dms.dochub.query.documents](dms.dochub.query.documents.md) | `(string i.ln.table, string i.document.type, long i.attr.list, long i.filter, ref long o.nr.documents, ref long o.documents, ref string error.mesg)` |
| `long` | [dms.dochub.query.response.get.first.document](dms.dochub.query.response.get.first.document.md) | `(long i.documents)` |
| `long` | [dms.dochub.query.response.get.next.document](dms.dochub.query.response.get.next.document.md) | `(long i.document)` |
| `string` | [dms.dochub.document.get.filename](dms.dochub.document.get.filename.md) | `(long i.document)` |
| `string` | [dms.dochub.document.get.mimetype](dms.dochub.document.get.mimetype.md) | `(long i.document)` |
| `string` | [dms.dochub.document.get.created.timestamp](dms.dochub.document.get.created.timestamp.md) | `(long i.document)` |
| `string` | [dms.dochub.document.get.last.changed.timestamp](dms.dochub.document.get.last.changed.timestamp.md) | `(long i.document)` |
| `long` | [dms.dochub.document.get.attribute](dms.dochub.document.get.attribute.md) | `(ref string o.attr.value, long i.document, string i.attr.value, [long i.attr.element])` |
| `long` | [dms.dochub.download.document](dms.dochub.download.document.md) | `(long i.document, ref string io.document.file, ref string o.error.msg)` |
| `long` | [dms.dochub.upload.document](dms.dochub.upload.document.md) | `(string i.ln.table, string i.document.type, long i.attr.list, string i.filename, string i.display.name, string i.mimetype, boolean i.create.revision, ref long o.document, ref string error.mesg)` |
| `long` | [dms.dochub.delete.document](dms.dochub.delete.document.md) | `(long i.document, string i.reason, ref string o.error.mesg)` |

## Related topics
- [DMS Document handling API](overview.md)

- [Document Management via Document Hub examples](dochub_examples.md)
