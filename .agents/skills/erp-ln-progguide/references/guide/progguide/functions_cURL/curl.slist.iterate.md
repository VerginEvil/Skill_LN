# curl.slist.iterate()

## Syntax:
`function boolean curl.slist.iterate( long listId, ref long IterId, ref string value )`

## Description
curl.slist.iterate() is used to iterate and retrieve the values from cURL's list. It can be used on the list returned by [curl.slist.append()](curl.slist.append.md) or [curl.slist.append_encrypted()](curl.slist.append_encrypted.md); and `curl.getinfo.cookielist()` functions.
When the list is freed using [curl.slist.free.all()](curl.slist.free.all.md).,all iterators are invalidated.

## Arguments
| | | |
|---|---|---|
| `long` | `listId` |  The id of existing list.  |
| `ref long` | `IterId` |  If 0(zero), then the iteration begins from the start of the list and it is updated with the new value upon successful return. This updated `iterId` must be used in subsequent calls to continue iteration.  |
| `ref string` | `value` |  The value stored in list at current position.  |

## Return values
True on successful iteration.False if iteration end or list does not exist

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [cURL handling overview](overview.md)
