# soap.getEnvelope()

## Syntax:
`function long soap.getEnvelope( long soapMessage )`

## Description
Returns the SOAP Envelope of the given SOAP message.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to a SOAP Message  |

## Return values
| | |
|---|---|
| <> 0 | a handle to the SOAP Envelope |
| 0 | when the SOAP Envelope is not found |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
The specified `soapMessage` must be a valid handle.

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
