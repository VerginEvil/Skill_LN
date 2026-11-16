# base64.decode()

## Syntax:
`function long base64.decode( string data.in, ref string data.out )`

## Description
Decodes the base64-encoded input to binary output.

## Arguments
| | | |
|---|---|---|
| `string` | `data.in` |  String with base64-encoded input. All bytes of the input are used, as determined by the [byte capacity](../3gl_features/data_types.md#byte capacity). All non-base64 bytes are skipped, including [NULL characters](../3gl_features/null_characters_in_strings.md) and unexpected padding characters (=).  |
| `ref string` | `data.out` |  String which will receive the binary output.  |

## Return values
The size of the binary output is returned. If this value is greater than the [byte capacity](../3gl_features/data_types.md#byte capacity) of data.out, then the output is completely filled with binary output, but that is less than the complete decoded version of the base64-encoded input.
If the size of the binary output is less than the [byte capacity](../3gl_features/data_types.md#byte capacity) of data.out, then the remaining bytes in data.out are left unchanged.
To compute the size of the binary output, it is not enough to know the [byte capacity](../3gl_features/data_types.md#byte capacity) of the base64-encoded input, because all unexpected input bytes are skipped. For each four not skipped base64-encoded input characters, normally three binary output bytes are produced. However, when these four characters end with a single padding character (=), then two output bytes are produced, and when they end with two padding characters (==), then one output byte is produced.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Base64 overview](base64_overview.md)

- [Base64 synopsis](base64_synopsis.md)
