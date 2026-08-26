# Doctype element in relation to XML
The optional document type element (created with function xmlNewNode("name", XML_DTD) ) can be used to generate an XML-document with a DTD. When an XML object results from parsing an XML document, no document type (XML_DTD) node is created.
For the document type element of an XML object the following mapping rules apply:
- The name of the XML_DTD node is the name of the document type definition.
- The value of the optional attribute "NAMEURL" is the value of the XML expression *SystemLiteral* part of the XML expression *ExternalID*.
- The value of the optional attribute "NAMEPUBLICID" is the value of the XML expression *PubidLiteral* part of the XML expression *ExternalID*. When attribute "NAMEURL" is defined and attribute "NAMEPUBLICID" is not defined, the XML expression *ExternalID* gets the form: "SYSTEM *SystemLiteral*. When both attributes are defined, the XML expression *ExternalID* gets the form: "PUBLIC *PubidLiteral SystemLiteral* "
- No child nodes other than XML_DATA or XML_PI are allowed for a XML_DTD node.
- When data is added to a XML_DTD node, this is written as-is to the XML document. The generator does not generate XML tags for the declarations.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
