# Find first Node using a Match Pattern

## Syntax:
`function long xmlFindFirstMatch( string pattern, long fromNode, [ long toNode ] )`

## Description
Search in a tree or a list of trees and return the first XML_ELEMENT or XML_DTD, which matches with the string pattern. The string pattern contains a search path relative to the starting node. The starting node is the list of nodes indicated by *fromNode* to *toNode*.

## Arguments
```

Pattern        ::=   Part [ '.' Part ]*
Part           ::=   DepthSearch | BreadthSearch | ParentSearch | Tag |
                     RightSibling | LeftSibling |  FirstChild | LastChild | Parent
DepthSearch    ::=   '?' Tag
BreadthSearch  ::=   '-' Tag
ParentSearch   ::=   '^' Tag
Tag            ::=   '<' [Name] [Attribute]*  '>'
Name           ::=   Element name, see for a definition:  [XMLSTD].
Attribute      ::=   attname'='attvalue | attname | attname'=' | '='attvalue
RightSibling   ::=   "right"
LeftSibling    ::=   "left"
FirstChild     ::=   "fChild"
LastChild      ::=   "lChild"
Parent         ::=   "parent"
```
| | | |
|---|---|---|
| `string` | `pattern` |  The parameter *pattern* is a string which should conform to the following syntax: Attribute values should be surrounded by double quotes. When the text inside a tag starts with a stand alone identifier (not followed by an equals sign '='), then, according to the above syntax, it is ambiguous whether it is an element name or an attribute name. In fact, it is interpreted as an element name. When an attribute name is meant, it should in this case be followed by an equals sign '='. This is not necessary for further attributes. For an example see [Example XML parsing](example_xml_parsing.md). See also [XML object API](api.md).  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See fromNode and toNode.  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See fromNode and toNode.  |

## Return values
| | |
|---|---|
| <> 0 | Success; The new tree containing references to the found nodes. In case no match is found the tree consists of a single node.  |
| 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [XML object overview](overview.md)
- [XML object synopsis](synopsis.md)
