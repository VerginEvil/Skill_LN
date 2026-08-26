# SQL query extensions synopsis
| | | |
|---|---|---|
| long | [query.extend.fld.select](query.extend.fld.select.md) | `( string select_column, string extension_string )` |
| long | [query.extend.fld.from](query.extend.fld.from.md) | `( string select_column, string extension_string )` |
| long | [query.extend.fld.where](query.extend.fld.where.md) | `( string select_column, string extension_string] )` |
| long | [query.extend.fld.parm](query.extend.fld.parm.md) | `( string select_column, string parameter] )` |
| void | [clear.query.extend.in.zoom()](clear.query.extend.in.zoom.md) | `( )` |
| void | [query.extend.select](query.extend.select.md) | `( string extension_string [, long mode] )` |
| void | [query.extend.select.in.zoom](query.extend.select.in.zoom.md) | `( string extension_string )` |
| void | [query.extend.from](query.extend.from.md) | `( string extension_string [, long mode] )` |
| void | [query.extend.from.in.zoom](query.extend.from.in.zoom.md) | `( string extension_string )` |
| void | [query.extend.where](query.extend.where.md) | `( string extension_string [, long mode] )` |
| void | [query.extend.where.in.zoom](query.extend.where.in.zoom.md) | `( string extension_string )` |
| void | [query.extend.hint](query.extend.hint.md) | `( string extension_string [, long mode] )` |
| void | [query.extend.hint.in.zoom](query.extend.hint.in.zoom.md) | `( string extension_string )` |
| void | [rebuild.query()](rebuild.query.md) | `( )` |
| long | [query.define.sort.order()](query.define.sort.order.md) | `(long table.index, const string field.var, direction.var [, const string ..., ...])` |

## Related topics
- [SQL query extensions overview](overview.md)
- [Query extensions sample program](example.md)
