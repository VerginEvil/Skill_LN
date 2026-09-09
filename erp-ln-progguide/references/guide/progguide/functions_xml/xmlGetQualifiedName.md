# xmlGetQualifiedName()

## Syntax:
`function long xmlGetQualifiedName( long node, ref string name )`

## Description
Get the qualified name of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `ref string` | `name` |  *name* is the return argument to receive the qualified name.  |

## Return values
| | |
|---|---|
| <> 0 | Success; The value of *node*. |
| 0 | The *node* is invalid. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

long ret
string qname(20)
ret = xmlGetQualifiedName( xml_envelope, qname )
| ret now contains the value of xml_envelope
| qname now contains "soap:Envelope"
```

## Related topics
- [XML object overview](overview.md)

- [XML object synopsis](synopsis.md)

- [XML object synopsis (namespace support)](synopsis_namespace.md)
