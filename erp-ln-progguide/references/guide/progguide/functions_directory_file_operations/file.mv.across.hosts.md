# file.mv.across.hosts()

## Syntax:
`function long file.mv.across.hosts( const string source, const string target )`

## Description
This moves a specified source file to the location specified in the *target* argument. The file can be either local or remote. Source and target can be on different hosts.

## Arguments
| | | |
|---|---|---|
| `const string` | `source` |  Source file.  |
| `const string` | `target` |  Target file.  |

## Return values
| | |
|---|---|
| 1 | Success. |
| < 0 | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Examples
```

ret = file.mv.across.hosts("/prod/order.txt", "/actual/order.text")           | moves the file on the same host
ret = file.mv.across.hosts("/prod/order.txt", "OMEGA!/prod/order.text")       | moves the file from local host to host OMEGA
ret = file.mv.across.hosts("OMEGA!/prod/order.txt", "/prod/order.text")       | moves the file from host OMEGA to local host
ret = file.mv.across.hosts("ALPHA!/prod/order.txt", "OMEGA!/prod/order.text") | moves a file from host ALPHA to host OMEGA
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
