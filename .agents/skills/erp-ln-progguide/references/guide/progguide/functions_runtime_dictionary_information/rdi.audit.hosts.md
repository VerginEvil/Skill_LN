# rdi.audit.hosts()

## Syntax:
`function long rdi.audit.hosts( string table_name(9), long comp_nr, ref string hosts() )`

## Description
This returns the names of the hosts on which audit information for a particular table is stored.

## Arguments
| | | |
|---|---|---|
| `string` | `table_name(9)` |  The name of the table.  |
| `long` | `comp_nr` |  The company number of the table.  |
| `ref string` | `hosts()` |  This returns a string containing the names of all hosts on which audit information for the specified table is stored. The host names are separated by commas [,]. The local host is referred to as 'localhost'.  |

## Return values
0 success
-1 error

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
Suppose that the table ttadv100, within company 100, is mirrored on the local system and on a remote system (host_99) and that the table is audited on both systems:
long ret
string hosts(20)
ret = rdi.audit.hosts("ttadv100", 100, hosts)
| after this function call, the 'hosts' argument contains:
| "localhost, host_99" or "host_99, localhost"

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
