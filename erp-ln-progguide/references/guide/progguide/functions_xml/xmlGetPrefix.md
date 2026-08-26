# xmlGetPrefix()

## Syntax:
`function long xmlGetPrefix( long node, ref string prefix )`

## Description
Get the prefix of the namespace of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `ref string` | `prefix` |  *prefix* is the return argument to receive the prefix.  |

## Return values
| | |
|---|---|
| <> 0 | Success; The value of *node*.  |
| 0 | The *node* is invalid or the namespace of the *node* is invalid or the *default* namespace.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

long ret
string prefix(10)
ret = xmlGetPrefix( xml_envelope, prefix )
| ret now contains the value of xml_envelope
| prefix now contains "soap"
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
