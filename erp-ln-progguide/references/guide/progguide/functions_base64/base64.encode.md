# base64.encode()

## Syntax:
`function long base64.encode( string data.in, ref string data.out )`

## Description
Encodes the binary input to base64-encoded output.

## Arguments
| | | |
|---|---|---|
| `string` | `data.in` |  String with binary input. All bytes of the input are used, as determined by the byte limit.  |
| `ref string` | `data.out` |  String which will receive the base64-encoded output. The output is *not* [NULL-terminated](../3gl_features/null_characters_in_strings.md). Any further bytes in the output string are left unchanged.  |

## Return values
The size of the base64-encoded output is returned. If this value is greater than the byte limit of data.out, then no output at all is written to data.out.
To compute the size of the base64-encoded output, only the byte limit of the binary input must be known, the actual input itself is not needed. For each three binary input bytes, four base64-encoded output characters are produced. For any (one or two) remaining binary input bytes at the end, also four base64-encoded output characters are produced.
So, to compute the size of the base64-encoded output, divide the byte limit of the binary input by 3, and if that is not an integer, round up to the next integer. Multiply the result by 4.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  If the input string is not completely filled, pass the input string as: your.string(1;number.of.filled.bytes). This avoids that any following unspecified bytes are encoded.
```

bytesread = seq.read( filebuffer, 60, filepointer )
while bytesread > 0
    | The last bytestring is usually not completely filled.
    | Avoid undesired bytes in the encoding by passing the number
    | of read bytes.
    base64.encode( filebuffer(1;bytesread), base64encodebuffer )
    | do something useful with the base64encodebuffer here
    bytesread = seq.read( filebuffer, 60, filepointer )
endwhile
```

## Related topics
- [Base64 overview](base64_overview.md)
- [Base64 synopsis](base64_synopsis.md)
