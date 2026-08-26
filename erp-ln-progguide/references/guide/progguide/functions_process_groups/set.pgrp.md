# set.pgrp()

## Syntax:
`function long set.pgrp( long process_id, long group_id )`

## Description
This places a specified process in a specified process group. If the process group ID is the same as the process ID, a new process group is created with the specified ID. The specified process becomes the leader of the new group.
The parent of the process does not change when you call this function.

## Arguments
| | | |
|---|---|---|
| `long` | `process_id` |  |
| `long` | `group_id` |  |

## Return values
The function returns the ID of the process group.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and The specified process should be a not trusted process

## Example 1
```

long any_group
set.pgrp(pid, pid)         | creates a new process group
set.pgrp(pid, any_group)   | sets pid in any_group
```

## Example 2
```

long mwindow, child
mwindow = create.mwindow(....)
change.mwindow( mwindow )
child = activate( "my.program" )
if child then
        set.pgrp( child, child )
        grab.mwindow( mwindow, child )
endif
```

## Related topics
- [Process groups overview](overview.md)
- [Process groups synopsis](synopsis.md)
