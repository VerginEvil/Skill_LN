# publish.webpart.message()

## Syntax:
`function void publish.webpart.message( const string type, long fromNode, [ long toNode ] )`

## Description
Sends a message to the Companyon shell, where it is passed on to any webparts registered to this message type.

## Arguments
| | | |
|---|---|---|
| `const string` | `type` |  The message type.  |
| `long` | `fromNode` |  Argument *fromNode* is a reference to an XML node. See [fromNode and toNode](../functions_xml/api.md#fromnode_tonode).  |
| `[ long` | `toNode ]` |  Optional argument *toNode* is a reference to an XML node. See [fromNode and toNode](../functions_xml/api.md#fromnode_tonode).  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Notes  This function is only usable in WebUI.

## Related topics
- [register.webpart.handler()](register.webpart.handler.md)
