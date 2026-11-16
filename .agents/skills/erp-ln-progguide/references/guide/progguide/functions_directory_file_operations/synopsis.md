# Directory and file operations synopsis
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
long
```
| | | |
|---|---|---|
| General functions |  |  |
| `string` | [creat.tmp.file$](creat.tmp.file.md) | `( [string pathname] )` |
| `long` | [dir.close](dir.close.md) | `( long dfd )` |
| `string` | [dir.entry](dir.entry.md) | `( long dfd, long read_type, ref long return_type, ref long filesize, ref long mode )` |
| `long` | [dir.open](dir.open.md) | `( const string path )` |
| `long` | [dir.open.tree](dir.open.tree.md) | `( const string path [, long nlevels] )` |
| `long` | [dir.rewind](dir.rewind.md) | `( long dfd )` |
| `long` | [file.chmod](file_chmod.md) | `( const string file, long mode )` |
| `long` | [file.chown](file.chown.md) | `( string file, string user, string group )` |
| `long` | [file.cp](file.cp.md) | `( const string source, const string target )` |
| `long` | [file.mv](file.mv.md) | `( const string source, const string target )` |
| `long` | [file.mv.across.hosts](file.mv.across.hosts.md) | `( const string source, const string target )` |
| `long` | [file.rm](file.rm.md) | `( const string path )` |
| `long` | [file.stat](file.stat.md) | `( string file_name(256), ref long file_size [, ref long ctime, ref long mtime, ref long atime ] )` |
| `void` | [FileManager.show](filemanager.show.md) | `( [const string i.root.path,] const string i.start.path, const string i.mime.filter )` |
| `long` | [FileManager.selectFile](filemanager.selectfile.md) | `( [const string i.root.path,] const string i.start.path, const string i.mime.filter, ref string o.file )` |
| `long` | [FileManager.selectFolder](filemanager.selectfolder.md) | `( [const string i.root.path, ]const string i.start.path, ref string o.folder )` |
| `long` | [fstat.info](fstat.info.md) | `( long fp, ref long size, ref long mode, ref long inode, ref long dev, ref long uid, ref long gid, ref long nlink, ref long ctime, ref long mtime, ref long atime )` |
| `string` | [getcwd](getcwd.md) | `( )` |
| `long` | [mkdir](mkdir.md) | `( string path_name$, [long access_level] )` |
| `long` | [pathname](pathname.md) | `( string file_basename(16), string file_type, ref string file_path(256) )` |
| `string` | [path.change.extension](path.change.extension.md) | `( const string path, const string extension, [long os.type] )` |
| `string` | [path.combine](path.combine.md) | `( string part(1024), [[string part(1024),...], long os.type] )` |
| `string` | [path.dir.separator](path.dir.separator.md) | `( [long os.type] )` |
| `string` | [path.directory](path.directory.md) | `( const string path, [long os.type] )` |
| `boolean` | [path.exists](path.exists.md) | `( const string path, [long access_level] )` |
| `string` | [path.extension](path.extension.md) | `( const string path, [long os.type] )` |
| `string` | [path.filename.without.extension](path.filename.without.extension.md) | `( const string path, [long os.type] )` |
| `string` | [path.filename](path.filename.md) | `( const string path, [long os.type] )` |
| `boolean` | [path.has.extension](path.has.extension.md) | `( const string path, [long os.type] )` |
| `boolean` | [path.is.absolute](path.is.absolute.md) | `( string path_name )` |
| `boolean` | [path.is.accessible](path.is.accessible.md) | `( string path_name )` |
| `string` | [path.separator](path.separator.md) | `( [long os.type] )` |
| `long` | [make.path.absolute](make.path.absolute.md) | `( ref string path_name )` |
| `long` | [rmdir](rmdir.md) | `( const string path, [boolean recursive] )` |
| `long` | [seq.clearerr](seq.clearerr.md) | `( long fp )` |
| `long` | [seq.close](seq.close.md) | `( long fp )` |
| `long` | [seq.eof](seq.eof.md) | `( long fp )` |
| `long` | [seq.error](seq.error.md) | `( long fp )` |
| `long` | [seq.flush](seq.flush.md) | `( long fp )` |
| `string` | [seq.getc$](seq.getc.md) | `( long fp )` |
| `long` | [seq.gets](seq.gets.md) | `( ref string line(), long nrbytes, long fp )` |
| `long` | [seq.islocked](seq.islocked.md) | `( long mode, long offset, long size, long fp )` |
| `long` | [seq.lock](seq.lock.md) | `( long mode, long offset, long size, long fp )` |
| `long` | [seq.open](seq.open.md) | `( string file(128), string openmode(2) [, ref string pathnm()] )` |
| `long` | [seq.open.bse.file](seq.open.bse.file.md) | `( string file(128), string openmode(2) [, ref string pathnm()] )` |
| `long` | [seq.processor.finish](seq.processor.finish.md) | `(long sp)` |
| `long` | [seq.processor.push.compressor](seq.processor.push.compressor.md) | `(long sp, string mode,[long compression method])` |
| `long` | [seq.processor.push.decompressor](seq.processor.push.decompressor.md) | `(long sp, string mode,[long compression method])` |
| `string` | [seq.putc$](seq.putc.md) | `( string char, long fp )` |
| `long` | [seq.puts](seq.puts.md) | `( const string line, long fp )` |
|  | [seq.r.long](seq.r.long.md) | `(long fp)` |
|  | [seq.r.short](seq.r.short.md) | `(long fp)` |
|  | [seq.r.utc](seq.r.utc.md) | `(long fp, [long byte.count])` |
| `long` | [seq.read](seq.read.md) | `( ref string buffer(), long nrbytes, long fp )` |
| `long` | [seq.rewind](seq.rewind.md) | `( long fp )` |
| `long` | [seq.seek](seq.seek.md) | `( long offset, long opt, long fp )` |
| `long` | [seq.skip](seq.skip.md) | `( long nrbytes, long fp )` |
| `long` | [seq.tell](seq.tell.md) | `( long fp )` |
| `string` | [seq.ungetc$](seq.ungetc.md) | `( string char, long fp )` |
| `long` | [seq.unlink](seq.unlink.md) | `( string path_name(128) )` |
| `long` | [seq.unlock](seq.unlock.md) | `( long mode, long offset, long size, long fp )` |
|  | [seq.w.long](seq.w.long.md) | `(long value, long fp)` |
|  | [seq.w.short](seq.w.short.md) | `(long value, long fp)` |
|  | [seq.w.utc](seq.w.utc.md) | `(long value, long fp, [long byte.count])` |
| `long` | [seq.write](seq.write.md) | `( const string buffer, long nrbytes, long fp )` |
| `long` | [stat.info](stat.info.md) | `( string file_name(256), ref long size, ref long mode, ref long inode, ref long dev, ref long uid, ref long gid, ref long nlink, ref long ctime, ref long mtime, ref long atime )` |
| `long` | [stream.type](stream.type.md) | `( long stream )` |
| `long` | [zipfile.build](zipfile.build.md) | `( long zipinfo )` |
| `long` | [zipfile.create](zipfile.create.md) | `( const string zipfile, const string entry )` |
| `long` | [zipfile.extract](zipfile.extract.md) | `( const string zipfile, const string dir )` |
| `long` | [zipfile.info](zipfile.info.md) | `( const string zipfile )` |
| `[long]` | [zipinfo.add](zipinfo.add.md) | `( long handle, const string entry, [long type] )` |
| `long` | [zipinfo.count](zipinfo.count.md) | `( long handle )` |
| `[long]` | [zipinfo.delete](zipinfo.delete.md) | `( long handle )` |
| `string` | [zipinfo.file](zipinfo.file.md) | `( long handle )` |
| `boolean` | [zipinfo.first](zipinfo.first.md) | `( long handle, ref string entry, ref long type )` |
| `long` | [zipinfo.new](zipinfo.new.md) | `( const string zipfile )` |
| `boolean` | [zipinfo.next](zipinfo.next.md) | `( long handle, ref string entry, ref long type )` |
| S3 streaming functions |  |  |
| `long` | [file.s3.rm](file.s3.rm.md) | `( long bucket, string key_addition )` |
| `json` | [seq.s3.ls](seq.s3.ls.md) | `( long bucket, string key_addition [, long options] )` |
| `long` | [seq.s3.open.file](seq.s3.open.file.md) | `( long bucket, string key_addition, string openmode )` |

## Related topics
- [Overview](overview.md)
