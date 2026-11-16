# sha.compute.output()

## Syntax:
`function long sha.compute.output( long id, ref string data.out )`

## Description
Adds some padding and a bit count to the message, as prescribed in the standard, and computes the resulting message digest. After this, the Secure Hash Algorithm state may be reused for hashing another message, by calling [sha.initialize()](sha.initialize.md), [sha.add.data()](sha.add.data.md), and [sha.compute.output()](sha.compute.output.md) again.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  Id of the Secure Hash Algorithm state, allocated by [sha.create()](sha.create.md).  |
| `ref string` | `data.out` |  String which will receive the Secure Hash Algorithm output.  |

## Return values
The size of the Secure Hash Algorithm output is returned. If this value is greater than the size of data.out, then no output at all is written to data.out, and sha.compute.output() may be called again with a larger output buffer.
The size of the Secure Hash Algorithm output is in all cases 20 bytes.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Secure Hash Algorithm overview](sha_overview.md)

- [Secure Hash Algorithm synopsis](sha_synopsis.md)
