# Images on Forms synopsis
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
boolean
```
```
void
```
```
boolean
```
```
boolean
```
```
string
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
| | | |
|---|---|---|
|  | [bind.image](bind.image.md) | `(string fieldname, string guidField, [string tablename] )` |
|  | [save.image.field](save.image.field.md) | `(string fieldname)` |
|  | [delete.image](delete.image.md) | `(string fieldname)` |
|  | [is.image.changed](is.image.changed.md) | `(string fieldname)` |
|  | [is.image.dropped](is.image.dropped.md) | `(string fieldname)` |
|  | [discard.changed.image](discard.changed.image.md) | `(string fieldname)` |
|  | [save.image.file](save.image.file.md) | `(string guid, long sequence, string pathname, [string tablename])` |
|  | [check.image.present](check.image.present.md) | `(string guid, [string tablename, long width, long height] )` |
|  | [get.image.path](get.image.path.md) | `(string guid, long sequ, [string tablename, long width, long height] )` |
|  | [copy.image](copy.image.md) | `(string source.guid, string source.tablename, string target.guid, string target.tablename, [boolean overwrite] )` |
|  | [copy.image.to.company](copy.image.to.company.md) | `(long source.company, string source.guid, string source.tablename, long target.company, string target.guid, string target.tablename, [boolean overwrite])` |
|  | [copy.image.to.file](copy.image.to.file.md) | `(long source.company, string source.guid, string source.tablename, string target.file)` |

## Related topics
- [Images on Forms Overview](overview.md)
- [Images on Forms Examples](examples.md)
