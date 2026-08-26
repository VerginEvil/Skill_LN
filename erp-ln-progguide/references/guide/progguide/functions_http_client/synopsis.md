# HTTP Client synopsis

## HTTP request functions
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [http.send](http.send.md) | `( const string method, const string url, ... )` |
|  | [http.get](http.get.md) | `( const string url )` |
|  | [http.post](http.post.md) | `( const string url, ... )` |
|  | [http.put](http.put.md) | `( const string url, ... )` |
|  | [http.delete](http.delete.md) | `( const string url )` |
|  | [http.patch](http.patch.md) | `( const string url, ... )` |
|  | [http.connect](http.connect.md) | `( const string url )` |
|  | [http.head](http.head.md) | `( const string url )` |
|  | [http.options](http.options.md) | `( const string url, ... )` |
|  | [http.trace](http.trace.md) | `( const string url, ... )` |

## HTTP header functions
```
string
```
```
string
```
```
long
```
```
long
```
```
void
```
```
void
```
```
void
```
```
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [http.header.name](http.header.name.md) | `( long header )` |
|  | [http.header.value](http.header.value.md) | `( long header )` |
|  | [http.header.next](http.header.next.md) | `( long header )` |
|  | [http.headerlist.new](http.headerlist.new.md) | `( ... )` |
|  | [http.headerlist.delete](http.headerlist.delete.md) | `( long headerlist )` |
|  | [http.headerlist.add](http.headerlist.add.md) | `( long headerlist, const string name, const string value )` |
|  | [http.headerlist.add_list](http.headerlist.add_list.md) | `( long headerlist, long other_headerlist )` |
|  | [http.headerlist.first](http.headerlist.first.md) | `( long headerlist )` |
|  | [http.headerlist.get](http.headerlist.get.md) | `( long headerlist, const string name )` |
|  | [http.headerlist.get_all](http.headerlist.get_all.md) | `( long headerlist, const string name )` |

## HTTP OAuth1 parameter functions
```
long
```
```
void
```
| | | |
|---|---|---|
|  | [http.oauth1params.new](http.oauth1params.new.md) | `( ... )` |
|  | [http.oauth1params.delete](http.oauth1params.delete.md) | `( long oauth1params )` |

## HTTP OAuth2 parameter functions
```
long
```
```
void
```
| | | |
|---|---|---|
|  | [http.oauth2params.new](http.oauth2params.new.md) | `( ... )` |
|  | [http.oauth2params.delete](http.oauth2params.delete.md) | `( long oauth2params )` |

## HTTP cookie functions
```
long
```
```
long
```
```
void
```
```
string
```
```
string
```
```
string
```
```
string
```
```
boolean
```
```
boolean
```
```
boolean
```
```
long
```
```
long
```
```
string
```
```
long
```
```
void
```
```
void
```
```
long
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [http.cookie.new](http.cookie.new.md) | `( ... )` |
|  | [http.cookie.parse](http.cookie.parse.md) | `( const string format, const string cookie_string )` |
|  | [http.cookie.delete](http.cookie.delete.md) | `( long cookie )` |
|  | [http.cookie.name](http.cookie.name.md) | `( long cookie )` |
|  | [http.cookie.value](http.cookie.value.md) | `( long cookie )` |
|  | [http.cookie.domain](http.cookie.domain.md) | `( long cookie )` |
|  | [http.cookie.path](http.cookie.path.md) | `( long cookie )` |
|  | [http.cookie.subdomains](http.cookie.subdomains.md) | `( long cookie )` |
|  | [http.cookie.secure](http.cookie.secure.md) | `( long cookie )` |
|  | [http.cookie.httponly](http.cookie.httponly.md) | `( long cookie )` |
|  | [http.cookie.expires](http.cookie.expires.md) | `( long cookie )` |
|  | [http.cookie.next](http.cookie.next.md) | `( long cookie )` |
|  | [http.cookie.to_string](http.cookie.to_string.md) | `( long cookie, const string format )` |
|  | [http.cookiejar.new](http.cookiejar.new.md) | `( )` |
|  | [http.cookiejar.delete](http.cookiejar.delete.md) | `( long cookiejar )` |
|  | [http.cookiejar.add](http.cookiejar.add.md) | `( long cookiejar, long cookie )` |
|  | [http.cookiejar.load](http.cookiejar.load.md) | `( ref long cookiejar, const string path )` |
|  | [http.cookiejar.save](http.cookiejar.save.md) | `( long cookiejar, const string path )` |
|  | [http.cookiejar.first](http.cookiejar.first.md) | `( long cookiejar )` |

## HTTP MIME part functions
```
long
```
```
void
```
```
long
```
```
void
```
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [http.mimepart.new](http.mimepart.new.md) | `( ... )` |
|  | [http.mimepart.delete](http.mimepart.delete.md) | `( long mimepart )` |
|  | [http.mimepartlist.new](http.mimepartlist.new.md) | `( )` |
|  | [http.mimepartlist.delete](http.mimepartlist.delete.md) | `( long mimepartlist )` |
|  | [http.mimepartlist.add](http.mimepartlist.add.md) | `( long mimepartlist, long mimepart )` |
|  | [http.mimepartlist.add_list](http.mimepartlist.add_list.md) | `( long mimepartlist, long other_mimepartlist )` |

## HTTP query parameter functions
```
long
```
```
long
```
```
long
```
```
long
```
```
string
```
| | | |
|---|---|---|
|  | [http.queryparamlist.new](http.queryparamlist.new.md) | `( ... )` |
|  | [http.queryparamlist.delete](http.queryparamlist.delete.md) | `( long queryparamlist )` |
|  | [http.queryparamlist.add](http.queryparamlist.add.md) | `( long queryparamlist, const string name, const string value )` |
|  | [http.queryparamlist.add_list](http.queryparamlist.add_list.md) | `( long queryparamlist, long other_queryparamlist )` |
|  | [http.queryparamlist.to_string](http.queryparamlist.to_string.md) | `( long queryparamlist, [ string sep(1) ] )` |

## HTTP route parameter functions
```
long
```
```
void
```
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [http.routeparamlist.new](http.routeparamlist.new.md) | `( ... )` |
|  | [http.routeparamlist.delete](http.routeparamlist.delete.md) | `( long routeparamlist )` |
|  | [http.routeparamlist.add](http.routeparamlist.add.md) | `( long routeparamlist, const string name, const string value )` |
|  | [http.routeparamlist.add_list](http.routeparamlist.add_list.md) | `( long routeparamlist, long other_routeparamlist )` |

## HTTP response functions
```
long
```
```
string
```
```
long
```
```
string
```
```
long
```
```
long
```
```
string
```
```
string
```
```
void
```
| | | |
|---|---|---|
|  | [http.response.curlcode](http.response.curlcode.md) | `( long response )` |
|  | [http.response.error_message](http.response.error_message.md) | `( long response )` |
|  | [http.response.statuscode](http.response.statuscode.md) | `( long response )` |
|  | [http.response.statustext](http.response.statustext.md) | `( long response )` |
|  | [http.response.headerlist](http.response.headerlist.md) | `( long response )` |
|  | [http.response.bodystream](http.response.bodystream.md) | `( long response )` |
|  | [http.response.request_method](http.response.request_method.md) | `( long response )` |
|  | [http.response.request_url](http.response.request_url.md) | `( long response )` |
|  | [http.response.delete](http.response.delete.md) | `( long response )` |

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client examples](examples.md)
