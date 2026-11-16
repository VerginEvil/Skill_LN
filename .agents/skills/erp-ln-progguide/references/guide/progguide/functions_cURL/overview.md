# cURL handling overview
Below is a list of all cURL functions.
A detailed description of the cURL functions can be found in the [documentation of the libcurl c interface](https://curl.se/libcurl/c/).

## cURL 3GL convenience functions
| | | |
|---|---|---|
| `long` | [curl.create.oauth1.authorization.header()](curl.create.oauth1.authorization.header.md) | `( const string method, const string url, const string consumer.key, const string consumer.secret, ref string header )` |
| `long` | [curl.download.data()](curl.download.data.md) | `( const string url, ref string data, ref long data.size [, long header.list] )` |
| `long` | [curl.download.file()](curl.download.file.md) | `( const string url, const string file [, long header.list] )` |
| `long` | [curl.download.stream()](curl.download.stream.md) | `( const string url, long response.stream [, long header.list] )` |
| `long` | [curl.download.string()](curl.download.string.md) | `( const string url, ref string data [, long header.list] )` |
| `string` | [curl.http.status$()](curl.http.status$.md) | `( long http.status )` |
| `long` | [curl.upload.data()](curl.upload.data.md) | `( const string url, const string data, long data.size, long response.stream [, long header.list] [, const string method] )` |
| `long` | [curl.upload.file()](curl.upload.file.md) | `( const string url, const string file, long response.stream [, long header.list] [, const string method] )` |
| `long` | [curl.upload.stream()](curl.upload.stream.md) | `( const string url, long request.stream, long data.size, long response.stream [, long header.list] [, const string method] )` |
| `long` | [curl.upload.string()](curl.upload.string.md) | `( const string url, const string data, long response.stream [, long header.list] [, const string method] )` |

## General cURL functions
| | | |
|---|---|---|
| `string` | [curl.get.errorbuffer$()](curl.get.errorbuffer$.md) | `()` |
| `double,long,string` | [curl.getinfo](curl.getinfo.md) | `()` |
| `long` | [curl.setopt](curl.setopt.md) | `()` |
| `long` | [curl.perform()](curl.perform.md) | `()` |
| `long` | [curl.slist.append](curl.slist.append.md) | `(ref long ListId, const string SomeText)` |
| `long` | [curl.slist.append_encrypted](curl.slist.append_encrypted.md) | `(ref long ListId,...)` |
| `void` | [curl.slist.free.all](curl.slist.free.all.md) | `(ref long ListId)` |
| `string` | [curl.strerror$()](curl.strerror$.md) | `(long CurlCode)` |
| `string` | [curl.xml.get.error$()](curl.xml.get.error$.md) | `()` |
| `void` | [curl.xml.set.whitespacehandling()](curl.xml.set.whitespacehandling.md) | `(long WhiteSpaceHandling)` |

## cURL MIME functions
| | | |
|---|---|---|
| `long` | `curl.mime.init` |  `()`  |
| `long` | `curl.mime.addpart` |  `(long mime_handle)`  |
| `long` | `curl.mime.name` |  `(long mime_handle, const string name())`  |
| `long` | `curl.mime.data` |  `(long PartId, const string data(), [long datasize])`  |
| `long` | `curl.mime.data_cb` |  `(long PartId, long sio_id, long datasize)`  |
| `long` | `curl.mime.filedata` |  `(long PartId, const string local_filename())`  |
| `long` | `curl.mime.filename` |  `(long PartId, const string remote_filename())`  |
| `long` | `curl.mime.subparts` |  `(long PartId, long mime_handle)`  |
| `long` | `curl.mime.type` |  `(long PartId, const string type())`  |
| `long` | `curl.mime.headers` |  `(long PartId, long slist_id)`  |
| `long` | `curl.mime.encoder` |  `(long PartId, const string encoding())`  |
| `void` | `curl.mime.free` |  `(long mime_handle)`  |
| `long` | `curl.setopt.mimepost` |  `(long mime_handle)`  |
[cURL MIME example](curl.mime.example.md)

## SSO functions
| | | |
|---|---|---|
| `string` | [curl.sso.user.encode$()](curl.sso.user.encode$.md) | `(const string User)` |
| `void` | [curl.sso.user.gettable()](curl.sso.user.gettable.md) | `(ref string EscapeTable)` |

## Escape functions
| | | |
|---|---|---|
| `string` | [curl.escape.decode$()](curl.escape.decode$.md) | `(const string SomeText)` |
| `string` | [curl.escape.encode$()](curl.escape.encode$.md) | `(const string SomeText)` |
| `string` | [curl.escape.encode.ext$()](curl.escape.encode.ext$.md) | `(const string EscapeTable, const string SomeText)` |
| `void` | [curl.escape.gettable()](curl.escape.gettable.md) | `(ref string EscapeTable)` |
