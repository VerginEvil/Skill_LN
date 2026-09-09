# soap.addHeader()

## Syntax:
`function void soap.addHeader( long soapMessage, long method )`

## Description
Adds the specified Header Element to the Header of the SOAP Envelope of the given SOAP message.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to the SOAP Message to add the specified header to  |
| `long` | `method` |  a handle to the Header Element which must be added to the SOAP Envelope of the given SOAP message  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Preconditions
- The specified `soapMessage` and `method` must both be valid handles.

- The specified `soapMessage` must contain a valid SOAP Envelope.

Note  It is possible to add multiple Methods to a SOAP Envelope Body.

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
