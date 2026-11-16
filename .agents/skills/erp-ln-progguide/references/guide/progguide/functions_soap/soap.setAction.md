# soap.setAction()

## Syntax:
`function void soap.setAction( long soapMessage, const string soapAction )`

## Description
Sets the SOAP Action of the specified SOAP Message. This action is sent together with the SOAP Envelope to the SOAP service.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to a SOAP Message  |
| `const string` | `soapAction` |  a string containing the SOAP action; often a (part of a) URL  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
The specified `soapMessage` must be a valid handle.

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
