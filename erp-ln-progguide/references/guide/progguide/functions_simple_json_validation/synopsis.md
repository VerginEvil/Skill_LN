# Simple JSON Validation synopsis

## Validating JSON
```
long
```
| | | |
|---|---|---|
|  | [sjv.validate()](sjv.validate.md) | `( long json, const string definition )` |

## JSON validation types
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
| | | |
|---|---|---|
|  | [sjv.any()](sjv.any.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.object()](sjv.object.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.fields()](sjv.fields.md) | `( const string name, const string type, ... )` |
|  | [sjv.array()](sjv.array.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.tuple()](sjv.tuple.md) | `( const string aspect, ... )` |
|  | [sjv.string()](sjv.string.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.double()](sjv.double.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.long()](sjv.long.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.boolean()](sjv.boolean.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.date()](sjv.date.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.utc()](sjv.utc.md) | `( [ const string aspect, ... ] )` |
|  | [sjv.domain()](sjv.domain.md) | `( [ const string aspect, ... ] )` |

## JSON validation aspects
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
string
```
```
string
```
```
string
```
| | | |
|---|---|---|
|  | [sjv.filled()](sjv.filled.md) | `()` |
|  | [sjv.nullable()](sjv.nullable.md) | `()` |
|  | [sjv.required()](sjv.required.md) | `()` |
|  | [sjv.min()](sjv.min.md) | `( long|double value )` |
|  | [sjv.max()](sjv.max.md) | `( long|double value )` |
|  | [sjv.length()](sjv.length.md) | `( long length )` |
|  | [sjv.enum()](sjv.enum.md) | `( const string value, ... )` |

## JSON string validation formats
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
string
```
```
string
```
| | | |
|---|---|---|
|  | [sjv.alpha()](sjv.alpha.md) | `()` |
|  | [sjv.alphanum()](sjv.alphanum.md) | `()` |
|  | [sjv.base64()](sjv.base64.md) | `()` |
|  | [sjv.email()](sjv.email.md) | `()` |
|  | [sjv.hex()](sjv.hex.md) | `()` |
|  | [sjv.isodate()](sjv.isodate.md) | `()` |
|  | [sjv.isodatetime()](sjv.isodatetime.md) | `()` |
|  | [sjv.numeric()](sjv.numeric.md) | `()` |
|  | [sjv.url()](sjv.url.md) | `()` |
|  | [sjv.uuid()](sjv.uuid.md) | `()` |

## Related topics
- [Simple JSON Validation overview](overview.md)
- [Simple JSON Validation examples](examples.md)
