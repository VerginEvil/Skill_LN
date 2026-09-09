# soap.deleteMessage()

## Syntax:
`function void soap.deleteMessage( ref long soapMessage )`

## Description
Deletes the specified SOAP Message from memory, including all contained data. When the SOAP Message contains a SOAP Envelope, the SOAP Envelope is deleted as well. The passed `soapMessage` handle is set to `0` on return.

## Arguments
| | | |
|---|---|---|
| `ref long` | `soapMessage` |  a handle to the SOAP Message to delete; is set to `0` on return  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
The specified `soapMessage` must be a valid handle; in case the handle has the value `0`, nothing is done.

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
