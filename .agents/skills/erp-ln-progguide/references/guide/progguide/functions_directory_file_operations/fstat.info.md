# fstat.info()

## Syntax:
`function long fstat.info( long fp, ref long size, ref long mode, ref long inode, ref long dev, ref long uid, ref long gid, ref long nlink, ref long ctime, ref long mtime, ref long atime )`

## Description
This returns information about a specified file. It provides the same information as [stat.info()](stat.info.md). But instead of retrieving information about a named file, it returns information about an open file that is known by the file descriptor *fp*. This descriptor can be obtained, for example, from a successful [seq.open()](seq.open.md) call.

## Arguments
| | |
|---|---|
| S_IRWXU | read, write, execute permission by owner |
| S_IRUSR | read permission by owner |
| S_IWUSR | write permission by owner |
| S_IXUSR | execute, search permission by owner |
| | |
|---|---|
| S_IRWXG | read, write, execute permission by group |
| S_IRGRP | read permission by group |
| S_IWGRP | write permission by group |
| S_IXGRP | execute, search permission by group |
| | |
|---|---|
| S_IRWXO | read, write, execute permission by others |
| S_IROTH | read permission by others |
| S_IWOTH | write permission by others |
| S_IXOTH | execute, search permission by others |
| | |
|---|---|
| S_ISUID | set user id on execution (sbit) |
| S_ISGID | set group id on execution (sbit) |
| | |
|---|---|
| S_ISVTX | save text after execution |

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
