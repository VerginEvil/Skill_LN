# uuid.format$()

## Syntax:
`function string uuid.format$( string uuid.compact )`

## Description
Computes the standard string representation, e.g. "17293b6c-4d4d-11d6-af08-080009da70ff", of a UUID which is supplied in compact string representation, e.g. "Fyk4JE1NEdaO4AgACdpw/w".

## Arguments
| | | |
|---|---|---|
| `string` | `uuid.compact` |  Input string with the compact string representation of a UUID, e.g. "Fyk4JE1NEdaO4AgACdpw/w".  |

## Return values
The standard string representation of the supplied UUID is returned, e.g. "17293b6c-4d4d-11d6-af08-080009da70ff".
The size of the standard string representation of a UUID is given by the predefined constant UUID.SIZE.STRING. Its value is 36.
When the supplied input is not a correct compact representation of a UUID (i.e. when it does not consist of exactly UUID.SIZE.COMPACT characters from the base64 character set, padded at the end with spaces only), then an empty string "" is returned.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [UUID overview](uuid_overview.md)

- [UUID synopsis](uuid_synopsis.md)
