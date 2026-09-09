# soap.addMethod()

## Syntax:
`function void soap.addMethod( long soapMessage, long method )`

## Description
Adds the specified Method to the Body of the SOAP Envelope of the given SOAP message.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to the SOAP Message to add the specified Method to  |
| `long` | `method` |  a handle to the Method to add to the SOAP Envelope of the given SOAP message  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
- The specified `soapMessage` and `method` must both be valid handles.

- The specified `soapMessage` must contain a valid SOAP Envelope.

Note  It is possible to add multiple Methods to a SOAP Envelope Body.

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
