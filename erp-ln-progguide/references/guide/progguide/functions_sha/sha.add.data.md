# sha.add.data()

## Syntax:
`function void sha.add.data( long id, string data.in )`

## Description
Adds one block of data to be hashed. It is not needed to supply all input data at once in one large block. Sha.add.data() may be called several times with relatively small blocks. Internally, the SHA-1 algorithm processes the input in 512 bit blocks, i.e. 64 byte at a time.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  Id of the Secure Hash Algorithm state, allocated by [sha.create()](sha.create.md).  |
| `string` | `data.in` |  String with input data.  |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  If the input string is not completely filled, pass the input string as: your.string(1;number.of.filled.bytes). This avoids that any following unspecified bytes are hashed.
```

bytesread = seq.read( filebuffer, 60, filepointer )
while bytesread > 0
    | The last bytestring is usually not completely filled.
    | Avoid undesired bytes in the hash by passing the number
    | of read bytes.
    sha.add.data( sha.id, filebuffer(1;bytesread) )
    bytesread = seq.read( filebuffer, 60, filepointer )
endwhile
```

## Related topics
- [Secure Hash Algorithm overview](sha_overview.md)
- [Secure Hash Algorithm synopsis](sha_synopsis.md)
