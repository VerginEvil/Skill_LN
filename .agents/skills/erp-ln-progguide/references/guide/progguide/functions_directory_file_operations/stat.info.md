# stat.info()

## Syntax:
`function long stat.info( string file_name, ref long size, ref long mode, ref long inode, ref long dev, ref long uid, ref long gid, ref long nlink, ref long ctime, ref long mtime, ref long atime )`

## Description
This returns information about a named file. It provides the same information as [fstat.info()](fstat.info.md), but for a named file.

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
