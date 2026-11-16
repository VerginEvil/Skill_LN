# cmf.getNextRecipient()

## Syntax:
`function long cmf.getnextrecipient( long mid, ref enum role )`

## Description
Retrieves the recipient entry in the message identified by the combination of role and the id of the previous recipient listed in the XML document. It returns the id of the recipient object. If previous is 0 (zero), the id of the first recipient listed in the XML document is returned.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `ref enum` | `role` |  The recipient's role: “FROM” | “TO” | “CC” | “BCC” | “OBO” | “NOTIFY”  |

## Return values
| | |
|---|---|
| <> 0 | Recipient Id. |
| 0 | No (next) recipient found or invalid object id. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
