# xmlBuildNamespaceList$()

## Syntax:
`function string xmlBuildNamespaceList$( const string prefix, const string URI, [ ... ] )`

## Description
This is a utility function that creates a string of namespace bindings, to be used for the [xmlFindFirstMatchNs()](xmlFindFirstMatchNs.md) and [xmlFindMatchNs()](xmlFindMatchNs.md) functions.

## Arguments
| | | |
|---|---|---|
| `const string` | `prefix` |  *prefix* is the prefix of a namespace.  |
| `const string` | `URI` |  *URI* is the URI of a namespace.  |
| `[ ...` | `]` |  Use optional parameters to supply more pairs of *prefix* and *URI*.  |

## Return values
| | |
|---|---|
| non-empty string | Success; A string of the form <prefix>="<URI>"[,<prefix>="<URI>"...]. |
| empty string | Error; One of the optional parameters is not of type string. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string namespaceList(100)
namespaceList = xmlBuildNamespaceList$(
	"soap", "http://www.w3.org/2001/12/soap-envelope",
	"m", "http://www.example.org/stock")

| namespaceList now contains 'soap="http://www.w3.org/2001/12/soap-envelope",m="http://www.example.org/stock"'
| The following statement, though a little less readable,  would produce the same result:

namespaceList = "soap=""http://www.w3.org/2001/12/soap-envelope"",m=""http://www.example.org/stock"""
```

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
- [XML object synopsis (namespace support)](synopsis_namespace.md)
