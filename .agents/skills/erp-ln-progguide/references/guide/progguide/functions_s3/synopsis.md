# S3 functions synopsis

## S3 path functions
| | | |
|---|---|---|
| `long` | [s3.path.to.location](s3.path.to.location.md) | `( const string s3.path$, ref string s3.key$ )` |
| `string` | [s3.location.to.path$](s3.location.to.path$.md) | `( long s3.location, const string s3.key$, [ long symbolize.mode ] )` |
| `string` | [s3.path.to.uri$](s3.path.to.uri$.md) | `( const string s3.path$ )` |
| `string` | [s3.uri.to.path$](s3.uri.to.path$.md) | `( const string s3.uri$ )` |
| `string` | [s3.path.bucket$](s3.path.bucket$.md) | `( const string s3.path$ )` |
| `string` | [s3.path.key$](s3.path.key$.md) | `( const string s3.path$ )` |
| `string` | [s3.path.filename$](s3.path.filename$.md) | `( const string s3.path$ )` |
| `string` | [s3.path.extension$](s3.path.extension$.md) | `( const string s3.path$ )` |
| `string` | [s3.path.folder$](s3.path.folder$.md) | `( const string s3.path$ )` |
| `string` | [s3.path.as.folder$](s3.path.as.folder$.md) | `( const string s3.path$ )` |
| `boolean` | [s3.path.is.folder](s3.path.is.folder.md) | `( const string s3.path$ )` |
| `string` | [s3.path.normalize$](s3.path.normalize$.md) | `( const string s3.path$ )` |
| `string` | [s3.path.expand$](s3.path.expand$.md) | `( const string s3.path$ )` |
| `string` | [s3.path.symbolize$](s3.path.symbolize$.md) | `( const string s3.path$, [ long symbolize.mode ] )` |
| `boolean` | [s3.path.exists](s3.path.exists.md) | `( const string s3.path$ )` |

## S3 object functions
| | | |
|---|---|---|
| `long` | [s3.object.modification.date](s3.object.modification.date.md) | `( const string s3.path$ )` |
| `long` | [s3.object.size](s3.object.size.md) | `( const string s3.path$ )` |
| `long` | [s3.object.stat](s3.object.stat.md) | `( const string s3.path$, ref long size, [ ref long modification.date ] )` |
| `long` | [s3.open.object](s3.open.object.md) | `( const string s3.path$, string mode$(1), [ long bufsz ] )` |
| `long` | [s3.put.object](s3.put.object.md) | `( const string s3.path$, const string bytes$, long num.bytes, [ long compress.method ] )` |
| `long` | [s3.get.object](s3.get.object.md) | `( const string s3.path$, ref string bytes$, long num.bytes, [ long compress.method ] )` |
| `long` | [s3.delete.object](s3.delete.object.md) | `( const string s3.path$ )` |
| `long` | [s3.copy.object](s3.copy.object.md) | `( const string source.s3.path$, const string target.s3.path$ )` |
| `long` | [s3.move.object](s3.move.object.md) | `( const string source.s3.path$, const string target.s3.path$ )` |
| `long` | [s3.upload.object](s3.upload.object.md) | `( const string s3.path$, const string file.path$, [ long compress.method ] )` |
| `long` | [s3.download.object](s3.download.object.md) | `( const string s3.path$, const string file.path$, [ long compress.method ] )` |

## S3 folder functions
| | | |
|---|---|---|
| `long` | [s3.list.object.keys](s3.list.object.keys.md) | `( const string s3.path$, long type, ref long object.keys )` |
| `long` | [s3.list.objects](s3.list.objects.md) | `( const string s3.path$, long type, ref long objects )` |
| `long` | [s3.create.folder](s3.create.folder.md) | `( const string s3.path$ )` |
| `long` | [s3.delete.folder](s3.delete.folder.md) | `( const string s3.path$, [ const string progress.callback.dll$, const string progress.callback.function$, long progress.callback.data ] )` |
| `long` | [s3.copy.folder](s3.copy.folder.md) | `( const string source.s3.path$, const string target.s3.path$, [ const string progress.callback.dll$, const string progress.callback.function$, long progress.callback.data ] )` |
| `long` | [s3.move.folder](s3.move.folder.md) | `( const string source.s3.path$, const string target.s3.path$, [ const string progress.callback.dll$, const string progress.callback.function$, long progress.callback.data ])` |
| `long` | [s3.upload.folder](s3.upload.folder.md) | `( const string s3.path$, const string file.path$, [ const string progress.callback.dll$, const string progress.callback.function$, long progress.callback.data ] )` |
| `long` | [s3.download.folder](s3.download.folder.md) | `( const string s3.path$, const string file.path$, [ const string progress.callback.dll$, const string progress.callback.function$, long progress.callback.data ] )` |

## S3 error functions
| | | |
|---|---|---|
| `string` | [s3.error.argument$](s3.error.argument$.md) | `( )` |
