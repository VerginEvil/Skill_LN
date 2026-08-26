# HTTP Client overview
The Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web. Hypertext is structured text that uses logical links (hyperlinks) between nodes containing text.
HTTP functions as a request–response protocol in the client–server computing model. A client requests a specific resource provided by a server, for example HTML files and other content. A client can also request the server to perform a specific task to which the server provides a result. HTTP resources are identified and located on the network by Uniform Resource Locators (URLs), using the Uniform Resource Identifiers (URI's) schemes http and https. URIs and hyperlinks in HTML documents form inter-linked hypertext documents.

## Scope and limitations
The API provides several functions for sending an HTTP request to a URL. Function [http.send()](http.send.md) is the generic function to configure and send a request. For ease of use the API provides some convenient wrapper functions for the most used HTTP methods, like [http.get()](http.get.md), [http.post()](http.post.md), [http.put()](http.put.md) etc. The API is object based and provides functions for dealing with the following object types:
- http.response
- http.queryparamlist
- http.routeparamlist
- http.headerlist
- http.header
- http.cookiejar
- http.cookie
- http.mimepartlist
- http.mimepart
- http.oauth1params
- http.oauth2params

## http.response
Represents the response returned from the webservice. It contains several properties like the HTTP statuscode, error information, the list of headers returned from the server, the body etc.

## http.queryparamlist
Represents a list of query parameter key-value pairs. This list can be used in case multiple requests have to be made to a webservice using the same query parameters.
The query parameters are expected to be non-URL encoded values. URL-encoding is done automatically upon sending the request, when they are added to the URL.
Example of a URL with query parameters: GET http://example.com/item?code=ABC&active=true

## http.routeparamlist
Represents a list of route parameter key-value pairs. Such a list helps in case multiple requests have to be made to a webservice using the same route parameters.
A route parameter is useful in case the path of the URL contains parts that identify objects that needs to be manipulated using the webservice.
Example: GET http://example.com/item/{item}
In this case {item} needs to be replaced with a real item code. A route parameter can do that.

## http.headerlist
Represents a list of HTTP header name-value pairs. The list can be used to send the same HTTP headers with multiple HTTP requests. An http.response object also contains an http.headerlist object containing the HTTP headers received from the webserver. The list can be traversed and searched in order check and retrieve specific HTTP headers.

## http.header
Represents a single HTTP header name-value pair.

## http.cookiejar
Introduced with TIV 2400.
Represents a collection of HTTP cookies. A cookiejar object is updated with cookies received from the server (Set-Cookie headers). When requests are made, any applicable cookies from the cookiejar are sent to the server (as a Cookie header). When cookies expire, they are removed from the cookiejar.
The cookies in an http.cookiejar object can be persisted to a file in Netscape format. Later on, an http.cookiejar object can be loaded again with the cookies stored in the file. In this way, cookies can be used across multiple HTTP sessions.

## http.cookie
Introduced with TIV 2400.
Represents a cookie.
An http.cookie object can be created by parsing a cookie string in Netscape format, by parsing a cookie string in Set-Cookie format or by specifying the individual attributes. It can also be converted back to a string in either Netscape or Set-Cookie format.

## http.mimepartlist
Introduced with TIV 2220.
Represents a list of MIME parts which can be used as the body of an HTTP multipart request. The list can be used to send the same MIME parts with multiple HTTP requests.

## http.mimepart
Introduced with TIV 2220.
Represents a single MIME part. This can be used as a part in an HTTP multipart request.
Mime parts can be constructed based on data stored in a string, a stream or a file. Each MIME part can have its own set of HTTP headers and can be encoded using different encodings. E.g. one part can be a UTF-8 JSON string, while another part can be a base64-encoded JPEG.

## http.oauth1params
Introduced with TIV 2340.
Represents a collection of OAuth1 parameters. This can be used to sign a request in an OAuth1 manner.
The following OAuth1 parameters can be specified:
- the signature method ("HMAC-SHA1", "HMAC-256", "PLAINTEXT")
- the consumer key
- the consumer secret
- the token (optional)
- the token secret (optional)
- the callback (optional)
- the verifier (optional)

## http.oauth2params
Introduced with TIV 2470.
Represents a collection of OAuth2 parameters. This can be used to sign a request in an OAuth2 manner.
The following OAuth2 parameters can be specified:
- either an OAuth 2.0 Parameter Set name from session ttaad0108m000
- or a combination of the following parameters:
- the grant type (client credentials or password credentials (default))
- where to put the client authentication (in header (default) or body)
- the client id
- the client secret
- the username (if password credentials grant type is used)
- the password (if password credentials grant type is used)
- the access token url
- the scopes

## Related topics
- [HTTP Client synopsis](synopsis.md)
- [HTTP Client examples](examples.md)
