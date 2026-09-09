# XML object API
The XML Object API defines the functions that can be used by any 3GL/4GL application to create, access and destroy an XML object.

## Object structure
- A node which describes an XML element (XML_ELEMENT).

- A node which describes an XML DTD (XML_DTD).

- A node which describes an XML data item (XML_DATA). n

- A node which describes an XML Processing Instruction (XML_PI).

Nodes of type XML_ELEMENT and XML_DTD can be nodes or leaves in the tree. So nodes of these types can have child nodes. Furthermore nodes of these two types can have a list of attributes. An Attribute is always a name-value pair.
Nodes of type XML_DATA and XML_PI are always leaf nodes and can thus not have any child nodes.
Below a sample XML document is shown. In Figure 1 the corresponding XML Object tree is shown.
```

<?xml version="1.0"?>
<!DOCTYPE CMF SYSTEM "cmf1.dtd">
<CMF>
        <IDENTIFICATION
                MESSAGE-ID="34a98u0erirori"
                CLASS="order"
                SUBJECT="Subject string"
        />
        <RECIPIENTS>
                <FROM
                        NAME="Jan Jansen"
                        TYPE="SMTP"
                        ADDRESS="jjansen@example.com"
                />
         </RECIPIENTS>
        <MESSAGE>The message text
</CMF>
```

## Figure 1 - XML Object tree corresponding with sample XML document
The XML functions access these nodes using unique id's. These id's are unique within the scope of one instantiation of a Baan VM. So these id's can be handed over to another 3GL processes running inside the same Baan VM but cannot be passed to a process running in another Baan VM.

## Multi-process issues
For passing XML nodes to other Baan VM processes, the following restrictions apply:

- There is always one owner process of an XML tree.

- Only the owner process is allowed to change or delete (parts of) an XML tree. Other processes in the same Baan VM only have read access.

- When the process, which is an owner of an XML tree, exits, the XML tree is implicitly deleted. This means that other processes, which might still have a reference to this tree, are not allowed to use this reference anymore.

- [De-serialize XML Object](de_serialize_xml_object.md)

- [De-serialize XML Object](de_serialize_xml_object.md)

- [Create a new Node](create_a_new_node.md)

- [Create an Element Node with Data Node](create_an_element_node_with_data_node.md)

- [Rewrite Data Element](rewrite_data_element.md)

- [Duplicate Nodes](duplicate_nodes.md)

- [Duplicate and Insert Nodes](duplicate_and_insert_nodes.md)

- [Duplicate and Append Nodes](duplicate_and_append_nodes.md)

- [Duplicate and Insert Nodes in Children](duplicate_and_insert_nodes_in_children.md)

- [Duplicate and Append Nodes to Children](duplicate_and_append_nodes_to_children.md)

- [Duplicate Nodes to Process](xmlduplicatetoprocess.md) (with own pid as argument).

- A process can transfer owner ship of a copy of an XML tree to another 3GL process by using [Duplicate Nodes to Process](xmlduplicatetoprocess.md) with passing the pid of the 3GL process which becomes the owner of this newly created XML tree.

## White-space handling
When parsing a document, white space is handled in one of three ways, depending on the value of the argument of xmlRead or xmlReadFromString and on the value of the xml:space attribute. Allowed values for this argument are XmlWhiteSpaceLegacyMode, XmlPreserveWhiteSpace, and XmlReplaceWhiteSpaceBySingleSpace. For a detailed description of the meaning of these values, see [De-serialize XML Object](de_serialize_xml_object.md).

## Character Data escaping
According to [XMLSTD], the ampersand character (&) and the left angle bracket (<) may not appear in element content data nor in attribute values. Furthermore an attribute value may not contain any double-quote character ("). If these characters are needed, they must be escaped using either numeric character references or the strings `&`, `<` and `"` respectively. The XML parser replaces these escape strings with the corresponding literal representation. The XML generator escapes the ampersand, left angle bracket and double-quote characters in node content and attribute values before serializing this to the output stream. This relieves applications from checking the data for these characters.

## Allowed characters
According to [XMLSTD], the following Unicode characters are allowed in an XML document:
```

  Char ::=  #x9 | #xA | #xD | [#x20-#xD7FF] | [#xE000-#xFFFD] | [#x10000-#x10FFFF]
```
All other characters are forbidden. There is no possibility to escape them. The forbidden characters are:

- ASCII control characters in the range [#x0-#x1F], except the allowed characters #x9 (Horizontal Tab), #xA (Line Feed), and #xD (Carriage Return);

- Unicode surrogate characters in the range [#xD800-#xDFFF];

- The <not a character> Unicode values #xFFFE and #xFFFF.

The XML generator verifies that no forbidden characters are produced. When a forbidden character is encountered, the serialization is stopped and an error is returned.
It can be checked beforehand whether a string (after conversion from TSS to UTF-8) contains valid characters only. See
xmlContainsValidCharactersOnly
.

## Handling of fromNode and toNode arguments
Several xml functions take as arguments *long fromNode, [ long toNode ]*. These arguments are references to XML nodes on which the operation must be performed. This includes all children of these nodes.
If only *fromNode* is specified, or *fromNode* and *toNode* specify the same node, then the operation is performed on the tree of which the specified node is the top node. The default tree traversal order is depth first. In this order the tree is traversed starting at the top node followed by the first (leftmost) child. See *Figure 2* for an example of the depth first traversal order. The traversal order in this tree corresponds with the *order* attribute value. In some cases a breadth first traversal order is used. See *Figure 3* for an example.
If both *fromNode* and *toNode* are specified, and *toNode* specifies a right sibling node of *fromNode*, then the operation is performed on *fromNode* and all its right sibling nodes, up to and including *toNode*.
If both *fromNode* and *toNode* are specified, and *fromNode* has a value of zero, then the operation is performed on *toNode* and all its left sibling nodes, starting at the leftmost sibling node of *fromNode*.
If both *fromNode* and *toNode* are specified, and *fromNode* has a value different from zero, and *toNode* does not specify a right sibling node of *fromNode* (including the case when *toNode* has a value of zero), then the operation is performed on *fromNode* and all its right sibling nodes, starting at *fromNode*.

## Figure 2 - Depth first Tree traversal order

## Figure 3 - Breadth first Tree traversal order

## Related topics
- [XML object overview](overview.md)

- [XML object constraints](constraints.md)

- [XML object glossary](glossary.md)

- [XML object synopsis](synopsis.md)
