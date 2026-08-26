# SOAP client overview
SOAP, originally defined as Simple Object Access Protocol, is a protocol specification for exchanging structured information in the implementation of Web Services in computer networks. It relies on eXtensible Markup Language (XML) as its message format, and usually relies on other Application Layer protocols (most notably Remote Procedure Call (RPC) and HTTP) for message negotiation and transmission. SOAP can form the foundation layer of a web services protocol stack, providing a basic messaging framework upon which web services can be built. This XML based protocol consists of three parts: an envelope - which defines what is in the message and how to process it - a set of encoding rules for expressing instances of application-defined datatypes, and a convention for representing procedure calls and responses.
As a layman's example of how SOAP procedures can be used, a SOAP message could be sent to a web-service-enabled web site (for example, a house price database) with the parameters needed for a search. The site would then return an XML-formatted document with the resulting data (prices, location, features, etc). Because the data is returned in a standardized machine-parseable format, it could then be integrated directly into a third-party site.

## Scope and limitations
3GL SOAP client implementations are available as of Infor Enterprise Server Server 8.3 (ES8.3). The implementation used in ES8.3 - ES8.6 has some limitations:
- It uses a simple, limited HTTP client (full HTTP is not supported; e.g. redirection is not supported)
- There is no HTTPS support;
- There is no XML namespace support.  As of Infor Enterprise Server Server 8.7, the 3GL SOAP client supports full HTTP and HTTPS, as well as XML namespaces.

## Example (using ES8.7 with XML namespace support)
The below code fragment shows how the SOAP client functions are typically used. Note that `#include <bic_soap>` must be done.
```

#include <bic_soap>

function main()
{
	long msgNode
	long requestNode
	long responseNode
	long methodNode
	long status
	long ns
	string zip( 64 )
	string result( 128 )

	zip = "10001"

	| Create a new SOAP message
	msgNode = soap.newMessage( URI_SOAP11 )

	| Define the method to call
	requestNode = xmlNewNode( "GetInfoByZIP" )
	| Declare and set the namespace
	ns = xmlNewNamespace( requestNode, "", "http://www.webserviceX.NET" )
	xmlSetNamespace( requestNode, ns )
	xmlNewDataElementNs( ns, "USZip", zip, requestNode )

	| Add the method to the SOAP envelope contained the in the SOAP message
	soap.addMethod( msgNode, requestNode )

	| Set the SOAP Action
	soap.setAction( msgNode, "http://www.webserviceX.NET/GetInfoByZIP" )

	| Invoke the SOAP request
	status = soap.invoke( msgNode, "http://www.webservicex.net/uszip.asmx", responseNode )

	| Check the response
	if status = 0 then
		| Get the method result
		methodNode = soap.getMethod( responseNode )
		result = xmlDataElement$( methodNode, "GetInfoByZIPResult" )
	else
		| Something went wrong...
		message( "SOAP Error: %d", status )
	endif

	| Cleanup
	soap.deleteMessage( msgNode )
	soap.deleteMessage( responseNode )
}
```

## Example (using ES8.3-8.6 without XML namespaces support)
```

#include <bic_soap>

function main()
{
	long msgNode
	long requestNode
	long responseNode
	long methodNode
	long status
	string zip( 64 )
	string result( 128 )

	zip = "10001"

	| Create a new SOAP message
	msgNode = soap.newMessage( URI_SOAP11 )

	| Define the method to call
	requestNode = xmlNewnode( "GetInfoByZIP" )
	| Set the default namespace
	xmlSetAttribute(requestNode, "xmlns", "http://www.webserviceX.NET" )
	xmlNewDataElement( "USZip", zip, requestNode )

	| Add the method to the SOAP envelope contained the in the SOAP message
	soap.addMethod( msgNode, requestNode )

	| Set the SOAP Action
	soap.setAction( msgNode, "http://www.webserviceX.NET/GetInfoByZIP" )

	| Invoke the SOAP request
	status = soap.invoke( msgNode,
	   "http://www.webservicex.net/uszip.asmx", responseNode )

	| Check the response
	if status = 0 then
		| Get the method result
		methodNode = soap.getMethod( responseNode )
		result = xmlDataElement$( methodNode, "GetInfoByZIPResult" )
	else
		| Something went wrong...
		message( "SOAP Error: %d", status )
	endif

	| Cleanup
	soap.deleteMessage( msgNode )
	soap.deleteMessage( responseNode )
}
```

## Related topics
- [SOAP client synopsis](synopsis.md)
