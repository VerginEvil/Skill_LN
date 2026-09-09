# XML object synopsis (namespace support)

## Syntax
| | | |
|---|---|---|
| `long` | [xmlAllocAttributeNs](xmlAllocAttributeNs.md) | `(ref string basedString(), long node, void namespaceOrURI, const string attributeName, [ const string default.value ] )` |
| `long` | [xmlAllocAttributePrefix](xmlAllocAttributePrefix.md) | `(ref string basedString(), long node, long attributeNr, [ const string default.value ] )` |
| `long` | [xmlAllocAttributeQualifiedName](xmlAllocAttributeQualifiedName.md) | `(ref string basedString(), long node, long attributeNr, [ const string default.value ] )` |
| `long` | [xmlAllocAttributeURI](xmlAllocAttributeURI.md) | `(ref string basedString(), long node, long attributeNr, [ const string default.value ] )` |
| `long` | [xmlAllocDataElementNs](xmlAllocDataElementNs.md) | `(ref string basedString(), long node, void namespaceOrURI, const string name, [ const string default.value, const string data.separator, const string element.separator ] )` |
| `long` | [xmlAllocPrefix](xmlAllocPrefix.md) | `(ref string basedString(), long node, [ const string default.value ] )` |
| `long` | [xmlAllocQualifiedName](xmlAllocQualifiedName.md) | `(ref string basedString(), long node, [ const string default.value ] )` |
| `long` | [xmlAllocURI](xmlAllocURI.md) | `(ref string basedString(), long node, [ const string default.value ] )` |
| `string` | [xmlAttributeNs$](xmlAttributeNs$.md) | `(long node, void namespaceOrURI, const string attributeName, [ const string default.value ] )` |
| `string` | [xmlAttributePrefix$](xmlAttributePrefix$.md) | `( long node, long attributeNr, [ const string default.value ] )` |
| `string` | [xmlAttributeQualifiedName$](xmlAttributeQualifiedName$.md) | `( long node, long attributeNr, [ const string default.value ] )` |
| `string` | [xmlAttributeURI$](xmlAttributeURI$.md) | `( long node, long attributeNr, [ const string default.value ] )` |
| `string` | [xmlBuildNamespaceList$](xmlBuildNamespaceList$.md) | `( const string prefix, const string URI,... )` |
| `string` | [xmlDataElementNs$](xmlDataElementNs$.md) | `(long node, void namespaceOrURI, const string name, [ const string default.value, const string data.separator, const string element.separator ] )` |
| `long` | [xmlDeleteAttributeNs](xmlDeleteAttributeNs.md) | `(long node, void namespaceOrURI, const string name )` |
| `long` | [xmlFindFirstMatchNs](xmlFindFirstMatchNs.md) | `(const string pattern, const string namespaceList, long fromNode, [ long toNode ])` |
| `long` | [xmlFindFirstNs](xmlFindFirstNs.md) | `(void namespaceOrURI, const string localName, long fromNode, [ long toNode ])` |
| `long` | [xmlFindMatchNs](xmlFindMatchNs.md) | `(string pattern, const string namespaceList, long fromNode, [ long toNode ])` |
| `long` | [xmlFindNamespace](xmlFindNamespace.md) | `(long node, const string URI)` |
| `long` | [xmlFindNodesNs](xmlFindNodesNs.md) | `(long node, void namespaceOrURI, const string localName, long maxFound, [ref long numFound] )` |
| `long` | [xmlFirstNamespaceDecl](xmlFirstNamespaceDecl.md) | `(long node)` |
| `long` | [xmlGetAttributeLengthNs](xmlGetAttributeLengthNs.md) | `(long node, void namespaceOrURI, string attributeName)` |
| `long` | [xmlGetAttributeNs](xmlGetAttributeNs.md) | `(long node, void namespaceOrURI, const string attributeName, ref string attributeValue )` |
| `long` | [xmlGetAttributePrefix](xmlGetAttributePrefix.md) | `(long node, long attributeNr, ref string attributeName)` |
| `long` | [xmlGetAttributePrefixLength](xmlGetAttributePrefixLength.md) | `(long node, long attributeNr)` |
| `long` | [xmlGetAttributeQualifiedName](xmlGetAttributeQualifiedName.md) | `(long node, long attributeNr, ref string attributeName)` |
| `long` | [xmlGetAttributeQualifiedNameLength](xmlGetAttributeQualifiedNameLength.md) | `(long node, long attributeNr)` |
| `long` | [xmlGetAttributeURI](xmlGetAttributeURI.md) | `(long node, long attributeNr, ref string attributeName)` |
| `long` | [xmlGetAttributeURILength](xmlGetAttributeURILength.md) | `(long node, long attributeNr)` |
| `long` | [xmlGetDataElementLengthNs](xmlGetDataElementLengthNs.md) | `(long node, void namespaceOrURI, const string name, [ long data.separator.length, long element.separator.length ] )` |
| `long` | [xmlGetDataElementNs](xmlGetDataElementNs.md) | `(long node, void namespaceOrURI, const string name, ref void data, [ const string data.separator, const string element.separator ] )` |
| `long` | [xmlGetNamespace](xmlGetNamespace.md) | `(long node)` |
| `long` | [xmlGetPredefinedNamespace](xmlGetPredefinedNamespace.md) | `(const string prefix)` |
| `long` | [xmlGetPrefix](xmlGetPrefix.md) | `(long node, ref string prefix )` |
| `long` | [xmlGetPrefixLength](xmlGetPrefixLength.md) | `(long node)` |
| `long` | [xmlGetQualifiedName](xmlGetQualifiedName.md) | `(long node, ref string name)` |
| `long` | [xmlGetQualifiedNameLength](xmlGetQualifiedNameLength.md) | `(long node)` |
| `long` | [xmlGetURI](xmlGetURI.md) | `(long node, ref string URI )` |
| `long` | [xmlGetURILength](xmlGetURILength.md) | `(long node )` |
| `string` | [xmlNamespacePrefix$](xmlNamespacePrefix$.md) | `(long namespace)` |
| `string` | [xmlNamespaceURI$](xmlNamespaceURI$.md) | `(long namespace)` |
| `long` | [xmlNewDataElementNs](xmlNewDataElementNs.md) | `(long namespace, const string name, void data, [ long parentNode ])` |
| `long` | [xmlNewNamespace](xmlNewNamespace.md) | `(long node, const string prefix, const string URI)` |
| `long` | [xmlNewNodeNs](xmlNewNodeNs.md) | `(long namespace, const string name, [long type, long parentNode ])` |
| `long` | [xmlNextNamespaceDecl](xmlNextNamespaceDecl.md) | `(long namespace)` |
| `string` | [xmlPrefix$](xmlPrefix$.md) | `(long node, [ const string default.value ] )` |
| `string` | [xmlQualifiedName$](xmlQualifiedName$.md) | `(long node, [ const string default.value ] )` |
| `long` | [xmlReadFromStringNs](xmlReadFromStringNs.md) | `(const string xmlString, ref string error, [ long whitespacehandling ] )` |
| `long` | [xmlReadNs](xmlReadNs.md) | `(long fp, ref string error, [ long whitespacehandling ] )` |
| `long` | [xmlRewriteDataElementNs](xmlRewriteDataElementNs.md) | `(long node, void namespaceOrURI, string localName, void data)` |
| `long` | [xmlSetAttributeNs](xmlSetAttributeNs.md) | `(long node, long namespace, const string name, void value)` |
| `long` | [xmlSetNamespace](xmlSetNamespace.md) | `(long node, long namespace)` |
| `string` | [xmlURI$](xmlURI$.md) | `(long node, [ const string default.value ] )` |

## Related topics
- [XML object overview](overview.md)

- [XML object constraints](constraints.md)

- [XML object glossary](glossary.md)

- [XML object API](api.md)
