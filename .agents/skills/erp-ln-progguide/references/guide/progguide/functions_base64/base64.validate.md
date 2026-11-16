# base64.validate()

## Syntax:
`function boolean base64.validate( string data.in, ref long error.index )`

## Description
Validates the input string whether it contains valid base64.

## Arguments
| | | |
|---|---|---|
| `string` | `data.in` |  String with binary input. All bytes of the input are used, as determined by the [byte capacity](../3gl_features/data_types.md#byte capacity).  |
| `ref long` | `error.index` |  See the description of the return value.  |

## Return values
True is returned when the string contains valid base64. Value of error.index is not changed
False is returned when size of data.in is not a multiple of 4. Optional error.index is set to 0.
False is returned when a non-based64 character is found in data.in. Optional argument error.index is set to index in the data.in where the non-based64 input is found.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  If the input string is not completely filled, pass the input string as: your.string(1;number.of.filled.bytes). This avoids that any following unspecified bytes are validated.
```

bytesread = seq.read( filebuffer, 60, filepointer )
while bytesread > 0
    | The last bytestring is usually not completely filled.
    | Avoid undesired bytes in the encoding by passing the number
    | of read bytes.
    base64.error = base64.validate( filebuffer(1;bytesread), error.index )
    if base64.error then
    | handle error, use error.index
         break | error found
    endif
    | do something useful with the base64encodebuffer here
    bytesread = seq.read( filebuffer, 60, filepointer )
endwhile
```

## Related topics
- [Base64 overview](base64_overview.md)

- [Base64 synopsis](base64_synopsis.md)
