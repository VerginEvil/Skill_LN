# fstat.info()

## Syntax:
`function long fstat.info( long fp, ref long size, ref long mode, ref long inode, ref long dev, ref long uid, ref long gid, ref long nlink, ref long ctime, ref long mtime, ref long atime )`

## Description
This returns information about a specified file. It provides the same information as [stat.info()](stat.info.md). But instead of retrieving information about a named file, it returns information about an open file that is known by the file descriptor *fp*. This descriptor can be obtained, for example, from a successful [seq.open()](seq.open.md) call.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  The file descriptor, as returned, for example, by [seq.open()](seq.open.md).  |
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
| 1 | Success. |
| <> 0 | Operating system error code. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  You can use the following macros to check the file type:
```

if ( S_ISDIR(mode) )    | file is a directory (perm: drwxrwxrwx)
if ( S_ISREG(mode) )    | file is an ordinary file (perm: -rwxrwxrwx)
if ( S_ISBLK(mode) )    | file is a block-oriented device (disk or tape)
  (perm: brwxrwxrwx)
if ( S_ISCHR(mode) )    | file is a character-oriented device
  (perm: crwxrwxrwx)
if ( S_ISFIFO(mode) )   | file is a fifo special file (perm: prwxrwxrwx)
if ( S_ISSOCK(mode) )   | file is a socket file (perm: srwxrwxrwx)
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
