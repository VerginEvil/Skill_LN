# sig.get.keys.info

## Syntax:
`#include <bic_sig>`
`function long sig.get.keys.info( string i.user, long o.keyinfo.node )`

## Description
Retrieve the configured keys for the given user, as defined in the configuration session.

## Arguments
```
<KeyInfo>
  (<Alias slot={slot number} onHSM={true|false}>{key alias}</Alias>)*
<KeyInfo>
```
| | | |
|---|---|---|
| `string` | `i.user` |  The user for which to retrieve the configured keys.  |
| `long` | `o.keyinfo.node` |  A new XML node, to be deleted by the caller, with the following structure:Note that when the alias is empty, no data node will be present.  |

## Return values
| | |
|---|---|
| 0 | The information was retrieved successfully |
| DALHOOKERROR | The user cannot be found. A DAL message has been set. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Digital Signatures overview](overview.md)
- [Digital Signatures synopsis](synopsis.md)
- [Digital Signatures examples](examples.md)
