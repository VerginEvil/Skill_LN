# curl.slist.append()

## Syntax:
`function long curl.slist.append( ref long listId, const string text )`

## Description
curl.slist.append() appends a specified string to a linked list of strings. This linked list can be used in some [curl.setopt](curl.setopt.md) functions. The allowed value(s) of the passed string depend on the context where it is used. If the listId is zero, then a new list is created. The listId should be passed as the first argument if the string need to be appended to an existing list. The specified string has been added to the list when this function returns. The return value is the listId upon success or 0 upon error. The list should be freed after usage with [curl.slist.free.all()](curl.slist.free.all.md).

## Arguments
| | | |
|---|---|---|
| `ref long` | `listId` |  A new (= value zero) or existing list ID.  |
| `const string` | `text` |  A text that can be interpreted by cURL.  |

## Return values
A list ID upon success or zero upon error.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [cURL handling overview](overview.md)
