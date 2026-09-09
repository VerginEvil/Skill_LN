# seq.processor.finish()

## Syntax:
`function long seq.processor.finish( long sp )`

## Description
The function flushes any remaining data in the compressor to the stream and adds needed trailing bits to mark the data as a standard gzip or deflate container, and then disables the compressor. Any more write requests to the stream will therefore fail.
The function is helpful in streams with a compressor attached and which are opened with [ims.openfba()](../functions_ims/ims.openfba.md) or [ims.openvba()](../functions_ims/ims.openvba.md) or any other function that works exclusively with buffers. Before reading from such streams, this function must be called, or some data may be missing.
The data in the buffer can then be read using [ims.getproperties()](../functions_ims/ims.getproperties.md) function.

## Arguments
| | | |
|---|---|---|
| `long` | `sp` |  A stream (file pointer) as returned by [seq.open()](seq.open.md), [seq.open.bse.file()](seq.open.bse.file.md), [ims.openfba()](../functions_ims/ims.openfba.md), [ims.openvba()](../functions_ims/ims.openvba.md), or [pipe.open()](../functions_interprocess_communication_os_level/pipe.open.md).  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | failed |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long ret
long sio
string buf(1) based
long size
string msg(100)

msg =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit"

| open vba with compressor processor and write some data
sio = ims.openvba("w+")
seq.processor.push.compressor(sio,"w")
ret = ims.write(msg, len(msg), sio)

| call seq.processor.finish after all the write is done.
seq.processor.finish(sio)

| This data can now be read with ims.getproperties function.
ret = ims.getproperties(sio, buf, size)

| close vba
ret = ims.close(sio)
```

## Related topics
- [seq.processor.push.decompressor()](seq.processor.push.decompressor.md)

- [seq.processor.push.compressor()](seq.processor.push.compressor.md)
