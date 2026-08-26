# xmlGetURI()

## Syntax:
`function long xmlGetURI( long node, ref string URI )`

## Description
Get the URI of the namespace of the specified node.

## Arguments
| | | |
|---|---|---|
| `long` | `node` |  *node* is a reference to an XML node.  |
| `ref string` | `URI` |  *URI* is the return argument to receive the URI.  |

## Return values
| | |
|---|---|
| <> 0 | Success; The value of *node*.  |
| 0 | The *node* is invalid or the namespace of the *node* is the *default* namespace.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

long xml_envelope
string error(100)
xml_envelope = xmlReadFromStringNs( "<soap:Envelope xmlns:soap=""http://www.w3.org/2001/12/soap-envelope""/>", error )

long ret
string URI(100)
ret = xmlGetURI( xml_envelope, URI )
| ret now contains the value of xml_envelope
| URI now contains "http://www.w3.org/2001/12/soap-envelope"
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
