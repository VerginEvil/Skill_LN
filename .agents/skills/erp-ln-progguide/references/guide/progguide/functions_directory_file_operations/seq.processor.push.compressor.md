# seq.processor.push.compressor()

## Syntax:
`function long seq.processor.push.compressor( long sp, string mode, [ long method ] )`

## Description
The function adds a gzip or deflate compressor to the specified stream.
The data written to the stream afterwards will be compressed first.
Adding the compressor is irreversible.
Adding a compressor to the stream is allowed even if some data has already been written.
The function modifies the behavior of the underlying stream in the following ways:
The stream becomes write-only (append only): any function attempting to read from the stream will return an error.
The functions [seq.write()](seq.write.md), [seq.puts()](seq.puts.md), [seq.putc$()](seq.putc.md), [seq.close()](seq.close.md), [xmlWrite()](../functions_xml/serialize_xml_object.md), [xmlWritePretty()](../functions_xml/serialize_xml_object_pretty.md), [Json.write()](../functions_json/Json_write.md) and [ims.write()](../functions_ims/ims.write.md) are supported.

## Arguments
| | | |
|---|---|---|
| `long` | `sp` |  A stream (file pointer) as returned from [seq.open()](seq.open.md), [seq.open.bse.file()](seq.open.bse.file.md), [ims.openfba()](../functions_ims/ims.openfba.md), [ims.openvba()](../functions_ims/ims.openvba.md) or [pipe.open()](../functions_interprocess_communication_os_level/pipe.open.md) functions.  |
| `string` | `mode` |  "w" for writing.  |
| `[ long` | `method ]` |  compression method. Can be either *SEQ_COMPRESSION_METHOD_GZIP* or *SEQ_COMPRESSION_METHOD_DEFLATE.* Default is *SEQ_COMPRESSION_METHOD_GZIP*.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | failure |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [seq.processor.push.decompressor()](seq.processor.push.decompressor.md)

- [seq.processor.finish()](seq.processor.finish.md)
