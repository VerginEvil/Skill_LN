# stat.info()

## Syntax:
`function long stat.info( string file_name, ref long size, ref long mode, ref long inode, ref long dev, ref long uid, ref long gid, ref long nlink, ref long ctime, ref long mtime, ref long atime )`

## Description
This returns information about a named file. It provides the same information as [fstat.info()](fstat.info.md), but for a named file.

## Arguments
| | | |
|---|---|---|
| `string` | `file_name` |  The name of the file. All files listed in the path name must be searchable. To specify a remote file, include the host name. For example: "host!/usr/myfile".  |
| `ref long` | `size` |  The file size in bytes.  |
| `ref long` | `mode` |  This contains a bit pattern that indicates the access permission (posix) of the file. Use the following defines to check the file mode:  |
| `ref long` | `inode` |  inode number. This field is deprecated. Its value is operating system dependent and on 64-bit systems its value may be truncated.  |
| `ref long` | `dev` |  Device where file is stored. This field is deprecated. Its value is operating system dependent and on 64-bit systems its value may be truncated.  |
| `ref long` | `uid` |  User ID of the file’s owner.  |
| `ref long` | `gid` |  The file’s group ID.  |
| `ref long` | `nlink` |  Number of links to the file.  |
| `ref long` | `ctime` |  The time when the file status was last changed, as a number of seconds since 00:00:00 GMT, January 1, 1970.  |
| `ref long` | `mtime` |  The time when the file was last modified, as a number of seconds since 00:00:00 GMT, January 1, 1970.  |
| `ref long` | `atime` |  The time when the file data was last accessed, as a number of seconds since 00:00:00 GMT, January 1, 1970.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Operating system error code. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  You can use the following macros to check the file type:

## Example
```

long    ret
long    size, mode, inode, dev, uid, gid, n.link, c.time, a.time,
m.time
string file_name(256)

file_name = "/usr/bse/lib/ipc_info"
ret = stat.info(        file_name,
                                                        size,
                                                        mode,
                                                        inode,
                                                        dev,
                                                        uid,
                                                        gid,
                                                        n.link,
                                                        c.time,
                                                        m.time,
                                                        a.time )
if ret then
                | stat.info failed, probably file not found
endif
if ( S_ISDIR( mode ) ) then
                sprintf$( "%s is a directory", file_name )
endif
if ( bit.and( S_IRUSR, mode ) ) then
                sprintf$( "User has read permission" )
endif
if ( bit.and( S_IWUSR, mode ) ) then
                sprintf$( "User has write permission" )
endif
if ( bit.and( S_IXUSR, mode ) ) then
                sprintf$( "User has execute permission" )
endif
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
