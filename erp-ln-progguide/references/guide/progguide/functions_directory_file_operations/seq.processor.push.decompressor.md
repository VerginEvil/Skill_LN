# seq.processor.push.decompressor()

## Syntax:
`function long seq.processor.push.decompressor( long sp, string mode, [ long method ] )`

## Description
The function adds a gzip decompressor to the specified stream.
The data read from the stream afterwards will be decompressed first.If the decompression fails, it will set the stream state as error.
Adding the decompressor is irreversible.
Adding a decompressor to a stream having read some data already is allowed.
The function modifies the behavior of the underlying stream in the following ways:
The stream becomes read-only: any attempt to write to the stream will return an error.
The functions [seq.read()](seq.read.md), [seq.getc$()](seq.getc.md), [seq.gets()](seq.gets.md), [seq.close()](seq.close.md), [xmlRead()](../functions_xml/de_serialize_xml_object.md), and [Json.read()](../functions_json/Json_read.md) are supported.

## Arguments
| | | |
|---|---|---|
| `long` | `sp` |  A stream (file pointer) as returned from [seq.open()](seq.open.md), [seq.open.bse.file()](seq.open.bse.file.md), [ims.openfba()](../functions_ims/ims.openfba.md), [ims.openvba()](../functions_ims/ims.openvba.md) or [pipe.open()](../functions_interprocess_communication_os_level/pipe.open.md) functions.  |
| `string` | `mode` |  "r" for reading  |
| `[ long` | `method ]` |  compression method. Can be either *SEQ_COMPRESSION_METHOD_GZIP* or *SEQ_COMPRESSION_METHOD_DEFLATE.* Default is *SEQ_COMPRESSION_METHOD_GZIP*.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | failure |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [seq.processor.push.compressor()](seq.processor.push.compressor.md)
- [seq.processor.finish()](seq.processor.finish.md)
