# Electronic Signature synopsis
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
boolean
```
| | | |
|---|---|---|
|  | [signature.start.request](signature.start.request.md) | `(domain ttesg.docm i.docm, const string key_field1, key_value1, [ key_field2, key_value2, ... ])` |
|  | [signature.finish.request](signature.finish.request.md) | `(boolean i.succeeded)` |
|  | [signed.document.add.record](signed.document.add.record.md) | `(long i.document.xml, const string i.table.name, const string | long | double i.key.reference)` |
|  | [signed.document.add.extra.field](signed.document.add.extra.field.md) | `(long i.document.xml, const string i.table.name, const string i.key.reference, const string i.label, const string i.value)` |
|  | [signed.document.add.field.desc](signed.document.add.field.desc.md) | `(long i.document.xml, const string i.table.field.name, const string i.key.reference, const string i.label, const string i.desc, [long i.element])` |
|  | [signature.is.required](signature.is.required.md) | `(domain ttesg.docm i.docm, long i.compnr)` |

## Related topics
- [Electronic Signature overview](overview.md)
