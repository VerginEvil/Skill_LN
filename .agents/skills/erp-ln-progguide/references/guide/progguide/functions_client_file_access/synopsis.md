# Client file access synopsis
```
long
```
```
void
```
```
long
```
```
string
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
```
void
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

void
```
```

long
```
```

long
```
```

string
```
```

boolean
```
| | | |
|---|---|---|
|  | [client.add.download.file](client.add.download.file.md) | `( long id, const string source, [const string mime.type, const string target] )` |
|  | [client.delete.upload.file.object](client.delete.upload.file.object.md) | `( long id )` |
|  | [client.download.file](client.download.file.md) | `( const string source, [const string mime.type, const string target] )` |
|  | [client.get.media.type](client.get.media.type.md) | `( const string source )` |
|  | [client.get.upload.file](client.get.upload.file.md) | `( long id, long index, [ref string client.filename, ref string mime.type] )` |
|  | [client.get.upload.filecount](client.get.upload.filecount.md) | `( long id )` |
|  | [client.prepare.download](client.prepare.download.md) | `( )` |
|  | [client.show.file](client.show.file.md) | `( const string source, boolean newwindow, const string title mb, [const string mime.type, const string target, boolean remove.after.download] )` |
|  | [client.show.url](client.show.url.md) | `( const string url )` |
|  | [client.start.download](client.start.download.md) | `( long id )` |
|  | [client.upload.file](client.upload.file.md) | `( const string destination, [ref string client.filename, ref string mime.type] )` |
|  | [client.upload.files](client.upload.files.md) | `( const string destination )` |
|  | [color.dialog()](color.dialog.md) | `( reference long io.color )` |
|  | [get.client.hostname()](get.client.hostname.md) | `( ref string hostname )` |
|  | [get.client.ip.address()](get.client.ip.address.md) | `( ref string ip.address )` |
|  | [get.client.timezone()](get.client.timezone.md) | `( )` |
|  | [open.url.local()](open.url.local.md) | `( const string url, long mode, [const string dialog.title, const string dialog.message, const string browser.title, const string string redir.param, ref long params.node] )` |

## Deprecated functions - Only supported in WebUI and BW
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

string
```
```

string
```
```

long
```
```

void
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
|  | [client2server()](client2server.md) | `( string source, string dest, boolean text.mode [, boolean rm.file] [, boolean progress.window] )` |
|  | [create.local.directory()](create.local.directory.md) | `( string dirent )` |
|  | [create.local.file()](create.local.file.md) | `( string filename )` |
|  | [dir.select.dialog.local()](dir.select.dialog.local.md) | `( ref string dirent )` |
|  | [get.client.directory()](get.client.directory.md) | `( const string id)` |
|  | [get.local.filename()](get.local.filename.md) | `( )` |
|  | [remove.local.directory()](remove.local.directory.md) | `( string dirent )` |
|  | [remove.local.file()](remove.local.file.md) | `( string filename )` |
|  | [seq.fstat.local()](seq.fstat.local.md) | `( string filename, ref long nr.bytes )` |
|  | [seq.open.dialog.local()](seq.open.dialog.local.md) | `( const string defaultname, const string directory, const string filter, ref string filename )` |
|  | [seq.open.dialog.next()](seq.open.dialog.next.md) | `( ref string filename )` |
|  | [seq.saveas.dialog.local()](seq.saveas.dialog.local.md) | `( const string defaultname, const string directory, const string filter, ref string filename)` |
|  | [server2client()](server2client.md) | `( string source, string dest, boolean text.mode [, boolean progress.window] [, boolean read.only] )` |
|  | [start.application.local()](start.application.local.md) | `( const string commandline, boolean waitFlag, reference long exitCode, [const string verb] )` |

## Deprecated functions - Only supported in BW
```

long
```
```

long
```
```

void
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
|  | [app_start()](app_start.md) | `( string commandline, string directory, string stdin, string stdout, string stderr )` |
|  | [app_status()](app_status.md) | `( long app.id )` |
|  | [seq.close.local()](seq.close.local.md) | `( long lfn )` |
|  | [seq.open.local()](seq.open.local.md) | `( string filename, string mode(2) [, long remove.after.use] )` |
|  | [seq.read.local()](seq.read.local.md) | `( ref string buf, ref long size, long lfn )` |
|  | [seq.write.local()](seq.write.local.md) | `( string buf, long size, long lfn )` |

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)

- [Implementing LN UI support](../webtop/htmlui_adoption.md)
