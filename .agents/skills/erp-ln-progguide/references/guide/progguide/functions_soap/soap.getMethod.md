# soap.getMethod()

## Syntax:
`function long soap.getMethod( long soapMessage )`

## Description
Returns the Method which is contained in the Body of the SOAP Envelope of the specified SOAP message.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to a SOAP Message  |

## Return values
| | |
|---|---|
| <> 0 | a handle to the Method |
| 0 | when the Method is not found |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
The specified `soapMessage` must be a valid handle.

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
