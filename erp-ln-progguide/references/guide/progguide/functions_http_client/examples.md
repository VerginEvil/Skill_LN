# HTTP Client examples

## Perform a HTTP GET request (Basic Authentication)
Example of how to perform an HTTP request (using basic authentication) and process the response.
```

        #include <bic_http>       |* Common HTTP Definitions
        #include <bic_httpclt>    |* HTTP Client Definitions

function http_example()
{
        long    response
        long    statuscode
        string  statustext(128)
        long    curlcode
        string  request.url(1024)
        string  request.method(16)
        long    response.headerlist
        long    response.header
        string  header.name(128)
        string  header.value(512)
        long    bodystream
        long    jsonvalue
        string  jsontext(1024 * 8)      |* 8 Kb
        long    numbytes
        string  errormsg(JSON_ERRSTR_SIZE)

        |* Perform an HTTP GET request with Basic Authentication
        |* URL: http://mockbin.com/request?nick=thefosk&mary=thequeen
        response = http.get("http://mockbin.com/request",
           HTTP_ACCEPT,         HTTP_CTYPE_APPLICATION_JSON,
           HTTP_HEADER,         "Custom-Header", "Some value",
           HTTP_QUERYPARAM,     "nick", "thefosk",
           HTTP_QUERYPARAM,     "mary", "thequeen",
           HTTP_AUTH,           HTTP_AUTH_BASIC, "user", "password")

        |* Get the CURL code from the response object
        |* curlcode = 0 means communication was OK
        curlcode = http.response.curlcode(response)

        |* Get a CURL error message (in case curlcode <> 0)
        errormsg = http.response.error_message(response)

        |* Get the HTTP status code; for example:
        |* 200 [HTTP_STATUS_OK] means the request was processed successfully
        |* 400 [HTTP_STATUS_BAD_REQUEST] means the request was not understood
        |* 500 [HTTP_STATUS_INTERNAL_SERVER_ERROR] means the server encountered an error while processing
        statuscode = http.response.statuscode(response)

        |* Get an HTTP status text, like "OK", "Bad Request", "Internal Server Error" etc.
        statustext = http.response.statustext(response)

        |* Get the URL of the request resulting in this response
        request.url = http.response.request_url(response)

        |* Get the HTTP Method (GET, POST, PUT, etc) of the request resulting in this response
        request.method = http.response.request_method(response)

        |* Get the HTTP headers of the response and traverse them
        response.headerlist = http.response.headerlist(response)
        response.header = http.headerlist.first(response.headerlist)

        while response.header <> 0
                header.name = http.header.name(response.header)
                header.value = http.header.value(response.header)

                |* process the header
                |* ...

                response.header = http.header.next(response.header)
        endwhile

        |* Or just get a single HTTP header value
        response.header = http.headerlist.get(response.headerlist, "Content-Type")
        header.value = http.header.value(response.header)

        |* Get the HTTP Body of the response, in this case a JSON value
        bodystream = http.response.bodystream(response)
        |* Read the JSON from the stream and process it
        jsonvalue = Json.read(bodystream, errormsg)
        |* Just get the JSON text (in this example)
        numbytes = Json.writeString(jsonvalue, jsontext, JSON_WRITE_PRETTY)

        |* Cleanup, this will also delete the HTTP headerlist; also the body stream is closed
        http.response.delete(response)
}
```

## Perform an OAuth1.0 HTTP GET request
Example of how to perform a so-called "signed-fetch" or "zero-legged" OAuth1 request.
```

        #include <bic_http>       |* Common HTTP Definitions
        #include <bic_httpclt>    |* HTTP Client Definitions

function http_oauth1.0_example()
{
        long    oauth1params
        long    response

        |* Create an http.oauth1params object
        |* (in this case only a consumer key and secret are used)
        |* Note: this object can be re-used for multiple HTTP requests
        oauth1params = http.oauth1params.new(
           HTTP_OAUTH1_SIGNATUREMETHOD, "HMAC-SHA1",
           HTTP_OAUTH1_CONSUMERKEY,     "the-consumer-key",
           HTTP_OAUTH1_CONSUMERSECRET,  "the-consumer-secret")

        |* Perform an HTTP GET request with OAuth1.0 Authentication
        |* URL: http://mockbin.com/request?nick=thefosk&mary=thequeen
        response = http.get("http://mockbin.com/request",
           HTTP_ACCEPT,                 HTTP_CTYPE_APPLICATION_JSON,
           HTTP_HEADER,                 "Custom-Header", "Some value",
           HTTP_QUERYPARAM,             "nick", "thefosk",
           HTTP_QUERYPARAM,             "mary", "thequeen",
           HTTP_OAUTH1PARAMS,           oauth1params)

        |* Process the response
        ...

        |* Delete the http.response object
        http.response.delete(response)

        |* Delete the http.oauth1params object
        http.oauth1params.delete(oauth1params)
}
```

## Perform an OAuth 2.0 HTTP GET request
Examples of how to perform an OAuth 2.0 request.
```

        #include <bic_http>       |* Common HTTP Definitions
        #include <bic_httpclt>    |* HTTP Client Definitions

function http_oauth2.0_example()
{
        long    oauth2params
        long    response

        |* Create an http.oauth2params object
        |* Note: this object can be re-used for multiple HTTP requests

        |* in this case a reference to an OAuth 2.0 Parameter Set is used
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_PARAMSET,        "Param Set 001")

        |* you can also specify the attributes yourself:
        oauth2params = http.oauth2params.new(
           HTTP_OAUTH2_GRANTTYPE,       HTTP_OAUTH2_PASSWORD_CREDENTIALS,
           HTTP_OAUTH2_CLIENTAUTH,      HTTP_OAUTH2_AS_BASIC_AUTH_HEADER,
           HTTP_OAUTH2_CLIENTID,        "<client_id>",
           HTTP_OAUTH2_CLIENTSECRET,    "<client_secret>",
           HTTP_OAUTH2_USERNAME,        "<username>",
           HTTP_OAUTH2_PASSWORD,        "<password>",
           HTTP_OAUTH2_ACCESSTOKENURL,  "https://example.com/oauth2/token",
           HTTP_OAUTH2_SCOPE,           "<scope>")

        |* Perform an HTTP GET request with OAuth 2.0 Authentication
        |* URL: http://mockbin.com/request?nick=thefosk&mary=thequeen
        response = http.get("http://mockbin.com/request",
           HTTP_ACCEPT,                 HTTP_CTYPE_APPLICATION_JSON,
           HTTP_HEADER,                 "Custom-Header", "Some value",
           HTTP_QUERYPARAM,             "nick", "thefosk",
           HTTP_QUERYPARAM,             "mary", "thequeen",
           HTTP_OAUTH2PARAMS,           oauth2params)

        |* Process the response
        ...

        |* Delete the http.response object
        http.response.delete(response)

        |* Delete the http.oauth2params object
        http.oauth2params.delete(oauth2params)
}
```

## Perform a (MIME) multipart HTTP POST request
Example of how to perform a multipart HTTP request using the HTTP_MIMEPART attribute.
```

        #include <bic_http>       |* Common HTTP Definitions
        #include <bic_httpclt>    |* HTTP Client Definitions

function http_mimepart_example()
{
        long    response
        long    headerlist

        |* In this example each part gets a Content-ID header (in this case a UUID)
        headerlist = http.headerlist.new("Content-ID", uuid.format$(uuid.generate$()))

        |* Create a request with 2 MIME parts:
        |* 1. a string containing some JSON
        |* 2. a file containing some XML, which must be base64-encoded
        response = http.post("http://mockbin.com/request",
           HTTP_MIMEPART,       http.mimepart.new(
                                   HTTP_MIME_CONTENTTYPE,       HTTP_CTYPE_APPLICATION_JSON,
                                   HTTP_MIME_NAME,              "part1",
                                   HTTP_MIME_FILENAME,          "hello.json",
                                   HTTP_MIME_ENCODER,           "binary",
                                   HTTP_MIME_STRING,            "{""hello"":""world""}",
                                   HTTP_MIME_HEADERLIST,        headerlist),
           HTTP_MIMEPART,       http.mimepart.new(
                                   HTTP_MIME_CONTENTTYPE,       HTTP_CTYPE_APPLICATION_XML,
                                   HTTP_MIME_NAME,              "part2",
                                   HTTP_MIME_ENCODER,           "bas64",
                                   HTTP_MIME_FILE,              "/path/to/file.xml",
                                   HTTP_MIME_HEADERLIST,        headerlist))

        |* Process response ...

    	|* Clean up
        http.response.delete(response)
        http.headerlist.delete(headerlist)
}
```
Example of how to perform a multipart HTTP request using the HTTP_MIMEPARTLIST attribute.
```

        #include <bic_http>       |* Common HTTP Definitions
        #include <bic_httpclt>    |* HTTP Client Definitions

function http_mimepartlist_example()
{
        long    response
        long    partlist
        long    headerlist

        |* Create a MIME part list and add 2 MIME parts
        partlist = http.mimepartlist.new()

        http.mimepartlist.add(partlist, http.mimepart.new(
           HTTP_MIME_CONTENTTYPE,       HTTP_CTYPE_APPLICATION_JSON,
           HTTP_MIME_NAME,              "part1",
           HTTP_MIME_FILENAME,          "hello.json",
           HTTP_MIME_ENCODER,           "binary",
           HTTP_MIME_STRING,            "{""hello"":""world""}")

        http.mimepartlist.add(partlist, http.mimepart.new(
           HTTP_MIME_CONTENTTYPE,       HTTP_CTYPE_APPLICATION_XML,
           HTTP_MIME_NAME,              "part2",
           HTTP_MIME_FILENAME,          "test.xml",
           HTTP_MIME_ENCODER,           "base64",
           HTTP_MIME_FILE,              "/path/to/file.xml")

        |* Perform a POST
        response = http.post("http://mockbin.com/request",
           HTTP_MIMEPARTLIST,           partlist)

        |* Process response ...

      	|* Clean up
        http.response.delete(response)
        http.mimepartlist.delete(partlist)
}
```

## Create new HTTP query parameter list
Example of how to create a new HTTP query parameter list
```

        #include <bic_http>       |* Common HTTP Definitions
        #include <bic_httpclt>    |* HTTP Client Definitions

function http_queryparamlist_example()
{
        long    queryparamlist
        long    response

        queryparamlist = http.queryparamlist.new(
           "name",              "John Doe",
           "address",           "34, Mainstreet",
           "city",              "New York")

        response = http.get("http://example.com/get",
           HTTP_QUERYPARAMLIST, queryparamlist)

        http.queryparamlist.delete(queryparamlist)
}
```

## Create an HTTP cookie object and add it to a cookiejar
Example of how to create a new http.cookie object, add it an http.cookiejar object and save it to a file
```

        #include <bic_http>       |* Common HTTP Definitions
        #include <bic_httpclt>    |* HTTP Client Definitions

function http_cookie_example()
{
        long    cookie
        long    cookiejar
        long    ret

        |* 1. by specifying attributes (name and domain are required!)
        cookie = http.cookie.new(
           HTTP_COOKIE_NAME,            "id",
           HTTP_COOKIE_VALUE,           "abcdefg",
           HTTP_COOKIE_DOMAIN,          ".infor.com",    |* the preceding dot indicates subdomains are allowed
           HTTP_COOKIE_PATH,            "/api",
           HTTP_COOKIE_SECURE,          true,
           HTTP_COOKIE_HTTPONLY,        true,
           HTTP_COOKIE_EXPIRES,         1630494970)      |* Wed, 01 Sep 2021 11:16:10 GMT

        |* 2. by parsing a Netscape formatted cookie
        cookie = http.cookie.parse(HTTP_COOKIE_NETSCAPE_FORMAT,
           "#HttpOnly_.infor.com" & chr$(9) &    |* domain; note the #HttpOnly_ prefix!
           "TRUE"                 & chr$(9) &    |* subdomains allowed
           "/api"                 & chr$(9) &    |* path
           "TRUE"                 & chr$(9) &    |* secure
           "1630494970"           & chr$(9) &    |* expires
           "id"                   & chr$(9) &    |* name
           "abcdefg")                            |* value

        |* 3. by parsing a Set-Cookie formatted cookie
        cookie = http.cookie.parse(HTTP_COOKIE_SET_COOKIE_FORMAT,
           "id=abcdefg; Expires=Wed, 01 Sep 2021 11:16:10 GMT; " &
           "Domain=.infor.com; Path=/api; Secure; HttpOnly")

        |* create a cookiejar and add the cookie to it
        cookiejar = http.cookiejar.new()
        http.cookiejar.add(cookiejar, cookiejar)

        |* save the cookiejar
        ret = http.cookiejar.save(cookiejar, path.combine(bse.appdata.dir$(), "cookiejar.txt"))

        |* cleanup, this also deletes any http.cookie objects in the http.cookiejar object
        http.cookiejar.delete(cookiejar)
}
```

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
