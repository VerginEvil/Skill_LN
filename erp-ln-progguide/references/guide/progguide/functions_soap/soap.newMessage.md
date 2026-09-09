# soap.newMessage()

## Syntax:
`function long soap.newMessage( const string soapNsURI )`

## Description
Creates a new SOAP Message, including a new SOAP Envelope and returns a handle to the new SOAP Message. The new SOAP Envelope will be created based on the specified SOAP namespace URI.
The newly created SOAP Envelope will have the following layout:
```

	<?xml version="1.0"?>
	<soap:Envelope>
		xmlns:soap="<soapNsURI>"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xmlns:xsd="http://www.w3.org/2001/XMLSchema"
		soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
		<soap:Header/>
		<soap:Body/>
	</soap:Envelope>
```
The specified `soapNsURI` will be used to fill in the `xmlns:soap` namespace declaration.

## Arguments
| | | |
|---|---|---|
| `const string` | `soapNsURI` |  the soap namespace URI; use `URI_SOAP11` for a SOAP 1.1 Envelope; use `URI_SOAP12` for a SOAP 1.2 Envelope.  |

## Return values
| | |
|---|---|
| <> 0 | a handle to the created SOAP Message object; this SOAP Message contains the created SOAP Envelope XML document |
| 0 | in case of an error |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
The specified `soapNsURI` must be one of the following strings:

- "http://schemas.xmlsoap.org/soap/envelope/" (defined as `URI_SOAP11` in `bic_soap`).

- "http://www.w3.org/2003/05/soap-envelope" (defined as `URI_SOAP12` in `bic_soap`).

## Related topics
- [SOAP client overview](overview.md)

- [SOAP client synopsis](synopsis.md)
