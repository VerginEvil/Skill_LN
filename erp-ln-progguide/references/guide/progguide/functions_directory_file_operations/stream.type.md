# stream.type()

## Syntax:
`function long stream.type( long stream )`

## Description
This function returns the type of a of stream as returned by for example seq.open(), dir.open(), sock.listen(), sock.connect(), sock.accept(), ims.openFBA(), ims.openVBA().

## Arguments
| | | |
|---|---|---|
| `long` | `stream` |  This is the stream as returned by the functions listed above.  |

## Return values
| | |
|---|---|
| STREAM.TYPE.INVALID | The stream argument is not associated to a valid stream. |
| STREAM.TYPE.FILE | The stream is opened with seq.open(). |
| STREAM.TYPE.DIRECTORY | The stream is opened with dir.open() or dir.open.tree(). |
| STREAM.TYPE.PIPE | The stream is opened with pipe.open(). |
| STREAM.TYPE.LISTEN.SOCKET | The stream is opened with sock.listen(). |
| STREAM.TYPE.SOCKET | The stream is opened with sock.connect() or sock.accept(). |
| STREAM.TYPE.FIXED.BYTEARRAY | The stream is opened with ims.openFBA(). |
| STREAM.TYPE.VARIABLE.BYTEARRAY | The stream is opened with ims.openVBA(). |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2330.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
