# XML object constraints
The XML object is not meant to implement a full XML parser/generator for building advanced XML document processing applications. The purpose of the XML object is to allow 3GL/4GL applications to exchange structured data using the XML format. Therefore not the complete XML standard is supported by the parser/generator, but only the sub-set needed to meet its requirement. Below a list of restrictions with respect to [XMLSTD] is given. This section should be read in conjunction with [XMLSTD]. All references to XML production rules in the [XMLSTD] are represented in italic.

## XML generator restrictions
- A fixed XMLDecl is generated. This declaration is always: `<?xml version="1.0"?>`
- For generation of `doctypedecl` contents (e.g. `markupdecl` and `PEReference`) no XML tag generation support is given. Correct formatting of this contents is left to the application.
- For element `content` other than `element` and `PI` (e.g. `Chardata`, `Reference`, `CDSect`, `Comment`) no XML tag generation support is given. Correct formatting of this content is left to the application.
- The output encoding is always UTF-8.
- A complete XML object must be constructed in Baan VM memory, before an XML document can be generated from it.

## XML parser restrictions
- The XML parser does not validate the document against its DTD. It only performs the well-formedness checks.
- The application does not have access to the document type definition (DTD).
- Default values for attributes defined in an external DTD are not passed to the application only default values defined in internal DTD sections are passed to the application.
- References to external parsed general entities are not processed by the parser but are ignored. So documents consisting out of multiple entities (modules) are not supported. References to internal entities are expanded before they are passed to the application.
- References to (external) unparsed entities (binary data) are ignored.
- The following document encodings are supported:
- UTF-8
- UTF-16 (unicode)
- ISO-8859-1
- Parsing of a document stops when an error is encountered.
- Only parsing of a complete XML document is supported, resulting in a complete XML object in Baan VM memory.
- A maximum XML element nesting depth of 256 is allowed.

## Related topics
- [XML object overview](overview.md)
- [XML object glossary](glossary.md)
- [XML object synopsis](synopsis.md)
- [XML object API](api.md)
