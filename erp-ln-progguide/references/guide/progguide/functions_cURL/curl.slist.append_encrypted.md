# curl.slist.append_encrypted()

## Syntax:
`function long curl.slist.append_encrypted( ref long listId, const string headerName,... )`

## Description
curl.slist.append_encrypted() appends specified element to a linked list of strings. If the element is encrypted, it would be decrypted first, otherwise, it is parsed as it is.
This linked list can be used in some [curl.setopt](curl.setopt.md) functions. The allowed value(s) of the passed string depend on the context where it is used.
If the listId is zero, then a new list is created. The listId should be passed as the first argument if the string need to be appended to an existing list. The specified strings have been added to the list when this function returns.
The return value is the listId upon success or negative integer to define issue upon error.
The list should be freed after usage with [curl.slist.free.all()](curl.slist.free.all.md).

## Arguments
| | | |
|---|---|---|
| `ref long` | `listId` |  A new (= value zero) or existing list ID.  |
| `const string` | `headerName` |  Header name (header key) of the HTTP header content to append.  |
|  | `...` | List of const string type texts to generate header value that can be interpreted by cURL. |

## Return values
| | |
|---|---|
| > 0 | Append is successful. Returns the list ID. |
| INVALID_SLIST_ELEMENT_TYPE (-1) | One of elements to append is not valid type. |
| INVALID_ENCRYPTION_METHOD (-2) | Encryption method is not one of known types. |
| SLIST_APPEND_ERROR (-3) | Error ocurred while appending given data to curl header list. |
| DECRYPTION_ERROR (-4) | Decryption of data is not successful. |
| UNKNOWN_ERROR (-127) | Error ocurred because of unknown reasons. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2530.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [cURL handling overview](overview.md)
