# soap.getBody()

## Syntax:
`function long soap.getBody( long soapMessage )`

## Description
Returns the Body of the SOAP Envelope of the given SOAP message.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to a SOAP Message  |

## Return values
| | |
|---|---|
| <> 0 | a handle to the SOAP Body |
| 0 | when the SOAP Body is not found |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
The specified `soapMessage` must be a valid handle.

## Related topics
- [SOAP client overview](overview.md)
- [SOAP client synopsis](synopsis.md)
