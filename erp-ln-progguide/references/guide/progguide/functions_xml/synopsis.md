# XML object synopsis
XML object synopsis
| | |
|---|---|
|  | 3GL/4GL function |
| [Verify the used characters](contains_valid_characters_only.md) | `long xmlContainsValidCharactersOnly( string inputstring )` |
| [Replace the invalid characters](replace_invalid_characters.md) | `long xmlReplaceInvalidCharacters( string inputString, string replacementCharacter( 1 ) )` |
| [Serialize XML Object (xmlWrite)](serialize_xml_object.md) | `long xmlWrite( long fp, long fromNode, [ long toNode ] )` |
| [Serialize XML Object Formatted](serialize_xml_object_pretty.md) | `long xmlWritePretty( long fp, long fromNode, [ long toNode ]` |
| [Serialize XML Object to String](serialize_xml_object_string.md) | `long xmlWriteToString( ref string buffer$, long fromNode, [ long toNode ] )` |
| [Serialize XML Object to Formatted String](serialize_xml_object_string_pretty.md) | `long xmlWritePrettyToString( ref string buffer$, long fromNode, [ long toNode ]` |
| [Serialize XML Object to Returned String](serialize_xml_object_return.md) | `string xmlString$( long fromNode, [ long toNode ] )` `string xmlStringUtf8$( long fromNode, [ long toNode ] )` |
| [Serialize XML Object to Returned Formatted String](serialize_xml_object_return_pretty.md) | `string xmlPrettyString$( long fromNode, [ long toNode ] )` |
| [Serialize XML Object to Returned Tss String](serialize_xml_object_return_tss.md) | `string xmlStringTss$( long fromNode, [ long toNode ] )` |
| [Serialize XML Object to Based String](serialize_xml_object_alloc.md) | `long xmlAllocString( ref string basedString$, long fromNode, [ long toNode ] )` |
| [Serialize XML Object to Formatted Based String](serialize_xml_object_alloc_pretty.md) | `long xmlAllocPrettyString( ref string basedString$, long fromNode, [ long toNode ] )` |
| [Get length of a serialized XML Object](get_serialize_length.md) | `long xmlGetStringLength( long fromNode, [ long toNode ] )` |
| [Get length of a formatted serialized XML Object](get_serialize_length_pretty.md) | `long xmlGetPrettyStringLength( long fromNode, [ long toNode ] )` |
| [De-serialize XML Object](de_serialize_xml_object.md) | `long xmlRead( long fp, ref string error, [ long whitespacehandling ] )` |
| [De-serialize XML Object from String](de_serialize_xml_object_string.md) | `long xmlReadFromString( string xmlString, ref string error, [ long whitespacehandling ] )` |
| [Create a new Node](create_a_new_node.md) | `long xmlNewNode( string name, [ long type, long parentNode ] )` |
| [Check a long is a valid XML node](is_node.md) | `long xmlIsNode( long node )` |
| [Create an Element Node with Data Node](create_an_element_node_with_data_node.md) | `long xmlNewDataElement( string name, string data, [ long parentNode ] )` |
| [Rewrite Data Element](rewrite_data_element.md) | `long xmlRewriteDataElement( long node, string name, string data )` |
| [Get data of all Elements](get_data_of_all_elements.md) | `long xmlGetDataElement( long node, const string name, ref string data, [ const string data.separator, const string element.separator ] )` |
| [Get data of all Elements](get_data_of_all_elements_return.md) | `string xmlDataElement$( long node, const string name, [ const string default.value, const string data.separator, const string element.separator ] )` |
| [Get data of all Elements](get_data_of_all_elements_alloc.md) | `long xmlAllocDataElement( ref string basedString(), long node, const string name, [ const string default.value, const string data.separator, const string element.separator ] )` |
| [Get data length of all Elements](get_data_length_of_all_elements.md) | `long xmlGetDataElementLength( long node, const string name, [ long data.separator.length, long element.separator.length ] )` |
| [Set name of a Node](set_name_of_a_node.md) | `long xmlSetName( long node, string name )` |
| [Set data of a Node](set_data_of_a_node.md) | `long xmlSetData( long node, string data )` |
| [Set attribute](set_attribute.md) | `long xmlSetAttribute( long node, string attributeName, string data )` |
| [Delete attribute](delete_attribute.md) | `long xmlDeleteAttribute( long node, string attribute )` |
| [Get name of a Node](get_name_of_a_node.md) | `long xmlGetName( long node, ref string name )` |
| [Get name of a Node](get_name_of_a_node_return.md) | `string xmlName$( long node, [ string default.value ] )` |
| [Get name of a Node](get_name_of_a_node_alloc.md) | `long xmlAllocName( ref string basedString(), long node, [ string default.value ] )` |
| [Get name length of a node](get_name_length.md) | `long xmlGetNameLength( long node )` |
| [Get parent of a Node](get_parent_of_a_node.md) | `long xmlGetParent( long node )` |
| [Get first child of a Node](get_child_of_a_node.md) | `long xmlGetFirstChild( long node )` |
| [Get last child of a Node](get_last_child_of_a_node.md) | `long xmlGetLastChild( long node )` |
| [Get number of child Nodes](get_number_of_child_nodes.md) | `long xmlGetNumChilds( long node )` |
| [Get left sibling of a Node](get_sibling_of_a_node.md) | `long xmlGetLeftSibling( long node )` |
| [Get right sibling of a Node](get_right_sibling_of_a_node.md) | `long xmlGetRightSibling( long node )` |
| [Get number of sibling Nodes](get_number_of_sibling_nodes.md) | `long xmlGetNumSiblings( long node )` |
| [Get number of left sibling Nodes](get_number_of_left_sibling_nodes.md) | `long xmlGetNumLeftSiblings( long node )` |
| [Get number of right sibling Nodes](get_number_of_right_sibling_nodes.md) | `long xmlGetNumRightSiblings( long node )` |
| [Get SAML (security data) node](xmlGetSAMLnode.md) | `long xmlGetSAMLnode()` |
| [Get data of a Node](get_data_of_a_node.md) | `long xmlGetData( long node, ref string data, [ const string separator ] )` |
| [Get data of a Node](get_data_of_a_node_return.md) | `string xmlData$( long node, [ const string default.value, const string separator ] )` |
| [Get data of a Node](get_data_of_a_node_alloc.md) | `long xmlAllocData( ref string basedString(), long node, [ const string default.value, const string separator ] )` |
| [Get data length of a Node](get_data_length_of_a_node.md) | `long xmlGetDataLength( long node, [ long separator.length ] )` |
| [Get attribute value](get_attribute_value.md) | `long xmlGetAttribute( long node, string attributeName, ref string data )` |
| [Get attribute value](get_attribute_value_return.md) | `string xmlAttribute$( long node, string attributeName, [ string default.value ] )` |
| [Get attribute value](get_attribute_value_alloc.md) | `long xmlAllocAttribute( ref string basedString(), long node, string attributeName, [ string default.value ] )` |
| [Get attribute length](get_attribute_length.md) | `long xmlGetAttributeLength( long node, string attributeName )` |
| [Get attribute name](get_attribute_name.md) | `long xmlGetAttributeName( long node, long attributeNr, ref string attributeName )` |
| [Get attribute name](get_attribute_name_return.md) | `string xmlAttributeName$( long node, long attributeNr, [ string default.value ] )` |
| [Get attribute name](get_attribute_name_alloc.md) | `long xmlAllocAttributeName( ref string basedString(), long node, long attributeNr,[ string default.value ] )` |
| [Get attribute name length](get_attribute_name_length.md) | `long xmlGetAttributeNameLength( long node, long attributeNr )` |
| [Get number of attributes](get_number_of_attributes.md) | `long xmlGetNumAttributes( long node )` |
| [Get Node type](get_node_type.md) | `long xmlGetType( long node )` |
| [Delete Nodes](delete_nodes.md) | `long xmlDelete( long fromNode, [ long toNode ] )` |
| [Unlink Nodes](unlink_nodes.md) | `long xmlUnlink( long fromNode, [ long toNode ] )` |
| [Unlink and Insert Nodes](unlink_and_insert_nodes.md) | `long xmlInsert( long destinationNode, long fromNode, [ long toNode ] )` |
| [Unlink and Add Nodes](unlink_and_add_nodes.md) | `long xmlAdd( long destinationNode, long fromNode, [ long toNode ] )` |
| [Unlink and Append Nodes](unlink_and_append_nodes.md) | `long xmlAppend( long destinationNode, long fromNode, [ long toNode ] )` |
| [Unlink and Insert Nodes in Children](unlink_and_insert_nodes_in_children.md) | `long xmlInsertInChilds( long parentNode, long fromNode, [ long toNode ] )` |
| [Unlink and Append Nodes to Children](unlink_and_append_nodes_to_children.md) | `long xmlAppendToChilds( long parentNode, long fromNode, [ long toNode ] )` |
| [Duplicate Nodes](duplicate_nodes.md) | `long xmlDuplicate( long fromNode, [ long toNode ] )` |
| [Duplicate Nodes to Process](xmlduplicatetoprocess.md) | `long xmlDuplicateToProcess( long processId, long fromNode, [ long toNode ] )` |
| [Duplicate and Insert Nodes](duplicate_and_insert_nodes.md) | `long xmlDuplicateAndInsert( long destinationNode, long fromNode, [ long toNode ] )` |
| [Duplicate and Add Nodes](duplicate_and_add_nodes.md) | `long xmlDuplicateAndAdd( long destinationNode, long fromNode, [ long toNode ] )` |
| [Duplicate and Append Nodes](duplicate_and_append_nodes.md) | `long xmlDuplicateAndAppend( long destinationNode, long fromNode, [ long toNode ] )` |
| [Duplicate and Insert Nodes in Children](duplicate_and_insert_nodes_in_children.md) | `long xmlDuplicateAndInsertInChilds( long parentNode, long fromNode, [ long toNode ] )` |
| [Duplicate and Append Nodes to Children](duplicate_and_append_nodes_to_children.md) | `long xmlDuplicateAndAppendToChilds( long parentNode, long fromNode, [ long toNode ] )` |
| [Find first Node](find_first_node.md) | `long xmlFindFirst( string tagName, long fromNode, [ long toNode ] )` |
| [Find first Node using a Match Pattern](find_first_node_using_a_match_pattern.md) | `long xmlFindFirstMatch( string pattern, long fromNode, [ long toNode ] )` |
| [Find Nodes](find_nodes.md) | `long xmlFindNodes( long node, string criteria, long maxFound, [ ref long numFound ] )` |
| [Find Nodes using a Match Pattern](find_nodes_using_a_match_pattern.md) | `long xmlFindMatch( string pattern, long fromNode, [ long toNode ] )` |
| [Find set of Sibling Nodes](find_set_of_sibling_nodes.md) | `long xmlFindSetOfSiblingNodes( long node, string criteria, long maxFound, [ ref long numFound ] )` |

## Related topics
- [XML object overview](overview.md)

- [XML object constraints](constraints.md)

- [XML object glossary](glossary.md)

- [XML object API](api.md)
