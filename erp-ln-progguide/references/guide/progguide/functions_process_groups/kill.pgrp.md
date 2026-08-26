# kill.pgrp()

## Syntax:
`function void kill.pgrp( long process_id )`

## Description
This ends all processes within the specified process group. All windows and graphical parts of the processes are removed.

## Arguments
| | | |
|---|---|---|
| `long` | `process_id` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long child_group, child_pid
child_group = set.pgrp( child_pid, child_pid )
....
....
kill.pgrp( child_group )
```

## Related topics
- [Process groups overview](overview.md)
- [Process groups synopsis](synopsis.md)
