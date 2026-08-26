# curl.slist.free.all()

## Syntax:
`function void curl.slist.free.all( ref long listId )`

## Description
curl.slist.free.all() frees a linked list of strings. The listId will be reset to zero after completion.

## Arguments
| | | |
|---|---|---|
| `ref long` | `listId` |  A list ID, created with [curl.slist.append()](curl.slist.append.md) or [curl.slist.append_encrypted()](curl.slist.append_encrypted.md)  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [cURL handling overview](overview.md)
