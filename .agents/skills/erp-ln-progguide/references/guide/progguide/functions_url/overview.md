# URL Functions Overview

## Overview
You can use these functions to parse, construct, encode and decode URL strings and their components, according to [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986).

## URL encoding/decoding functions
| | | |
|---|---|---|
| `string` | [url.decode](url.decode.md) | `( const string encoded_str )` |
| `string` | [url.encode_host](url.encode_host.md) | `( const string host )` |
| `string` | [url.encode_user_info](url.encode_user_info.md) | `( const string user_info )` |
| `string` | [url.encode_path](url.encode_path.md) | `( const string path )` |
| `string` | [url.encode_path_segment](url.encode_path_segment.md) | `( const string path_segment )` |
| `string` | [url.encode_query](url.encode_query.md) | `( const string query )` |
| `string` | [url.encode_query_part](url.encode_query_part.md) | `( const string query_part )` |
| `string` | [url.encode_fragment](url.encode_fragment.md) | `( const string fragment )` |

## URL instance functions
| | | |
|---|---|---|
| `long` | [url.new](url.new.md) | `( )` |
| `long` | [url.parse](url.parse.md) | `( encoded_str )` |
| `void` | [url.delete](url.parse.md) | `( long url_instance )` |
| `string` | [url.to_string](url.to_string.md) | `( long url_instance )` |
| `boolean` | [url.is_absolute](url.is_absolute.md) | `( long url_instance )` |
| `string` | [url.scheme](url.scheme.md) | `( long url_instance )` |
| `void` | [url.set_scheme](url.set_scheme.md) | `( long url_instance, const string scheme )` |
| `string` | [url.user_info](url.user_info.md) | `( long url_instance )` |
| `void` | [url.set_user_info](url.set_user_info.md) | `( long url_instance, const string user_info )` |
| `string` | [url.host](url.host.md) | `( long url_instance )` |
| `void` | [url.set_host](url.set_host.md) | `( long url_instance, const string host )` |
| `long` | [url.port](url.port.md) | `( long url_instance )` |
| `void` | [url.set_port](url.set_port.md) | `( long url_instance, long port )` |
| `string` | [url.path](url.path.md) | `( long url_instance )` |
| `void` | [url.set_path](url.set_path.md) | `( long url_instance, const string path )` |
| `string` | [url.query](url.query.md) | `( long url_instance )` |
| `void` | [url.set_query](url.set_query.md) | `( long url_instance, const string query )` |
| `string` | [url.fragment](url.fragment.md) | `( long url_instance )` |
| `void` | [url.set_fragment](url.set_fragment.md) | `( long url_instance, const string fragment )` |

## Query parameter functions
| | | |
|---|---|---|
| `long` | [query_params.new](query_params.new.md) | `( )` |
| `long` | [query_params.parse](query_params.parse.md) | `( const string encoded_params )` |
| `void` | [query_params.delete](query_params.delete.md) | `( long query_params_instance )` |
| `string` | [query_params.to_string](query_params.to_string.md) | `( long query_params_instance )` |
| `void` | [query_params.add](query_params.add.md) | `( long query_params_instance, const string name, const string value )` |
| `void` | [query_params.set](query_params.set.md) | `( long query_params_instance, const string name, const string value )` |
| `void` | [query_params.del](query_params.del.md) | `( long query_params_instance, const string name )` |
| `boolean` | [query_params.has](query_params.has.md) | `( long query_params_instance, const string name )` |
| `boolean` | [query_params.get](query_params.get.md) | `( long query_params_instance, const string name, ref string value )` |
| `long` | [query_params.get_values](query_params.get_values.md) | `( long query_params_instance, const string name, ref string values(,) )` |
| `string` | [query_params.value](query_params.value.md) | `( long query_params_instance, const string name )` |
| `boolean` | [query_params.iterate](query_params.iterate.md) | `( long query_params_instance, ref long iterator, ref string name, ref string values(,), ref long num_values )` |
