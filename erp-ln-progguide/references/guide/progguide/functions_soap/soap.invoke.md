# soap.invoke()

## Syntax:
`function long soap.invoke( long soapMessage, const string url, ref long responseMessage )`

## Description
Invokes a SOAP request as specified by the given SOAP Message. The request is sent to a SOAP service which is identified by the specified url. On return the response SOAP Message is returned in the `responseMessage` argument.

## Arguments
| | | |
|---|---|---|
| `long` | `soapMessage` |  a handle to the SOAP Message containing a SOAP Envelope describing the SOAP request  |
| `const string` | `url` |  the url to send the SOAP request to  |
| `ref long` | `responseMessage` |  on return this will contain the returned SOAP response message; note that this SOAP Message must be deleted with [soap.deleteMessage()](soap.deleteMessage.md) when it is no longer needed  |

## Return values
| | |
|---|---|
| 0 | when communication with the SOAP service was successful |
| <> 0 | in case of a communication error with the SOAP service |
Note that in case 0 is returned the response SOAP Envelope can still contain a Fault node, describing either a client or a server side error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
- The specified `soapMessage` must be a valid handle.
- The specified `soapMessage` should contain a valid SOAP Envelope.
- The specified `url` may not be empty.

## Related topics
- [SOAP client overview](overview.md)
- [SOAP client synopsis](synopsis.md)
