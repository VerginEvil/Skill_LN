# xmlAllocPrefix()

## Syntax:
`function long xmlAllocPrefix( ref string basedString, long node, [ const string default.value ] )`

## Description
Get the prefix of the namespace of the specified node.

## Arguments
| | | |
|---|---|---|
| `ref string` | `basedString` |  *basedString* is the return argument to receive the prefix. It must be declared *based*.  |
| `long` | `node` |  *node* is a reference to an XML node.  |
| `[ const string` | `default.value ]` |  *default.value* is a string that is used as return value when the function fails.  |

## Return values
| | |
|---|---|
| 0 | Success; The *basedString* contains the prefix if the *node* is valid and is in a namespace. It contains the *default.value*, or when this is omitted, the empty string otherwise. |
| -1 | The *basedString* is not declared *based*. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

long ret
string prefix based
ret = xmlAllocPrefix( prefix, xml_envelope )
| ret now contains 0
| prefix now contains "soap"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
