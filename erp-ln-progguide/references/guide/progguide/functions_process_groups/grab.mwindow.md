# grab.mwindow()

## Syntax:
`function void grab.mwindow( long mwindow, long process_group )`

## Description
This specifies the process group to which a particular main window must send its events. After calling this function, all events that occur in the main window are sent to the process group. *grab.mwindow()* is mainly used immediately after creation of a new process group.

## Arguments
| | | |
|---|---|---|
| `long` | `mwindow` |  The ID of the main window.  |
| `long` | `process_group` |  The ID of the process group.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long group, mwindow
group = set.pgrp(pid, pid)   | Create a new group
grab.mwindow(mwindow, group) | Send all events to the new group
```

## Related topics
- [Process groups overview](overview.md)
- [Process groups synopsis](synopsis.md)
