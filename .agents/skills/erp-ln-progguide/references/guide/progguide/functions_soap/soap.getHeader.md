# soap.getHeader()

## Syntax:
`function long soap.getHeader( long soapMessage )`

## Description
Returns the Header of the SOAP Envelope of the given SOAP message.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to a SOAP Message  |

## Return values
| | |
|---|---|
| <> 0 | a handle to the SOAP Header |
| 0 | when the SOAP Header is not found |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
The specified `soapMessage` must be a valid handle.

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
