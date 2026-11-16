# get.pgrp()

## Syntax:
`function long get.pgrp( long process_id )`

## Description
This returns the identification number of the process group to which the specified process belongs. If you specify an unknown process ID, -1 is returned.

## Arguments
| | | |
|---|---|---|
| `long` | `process_id` |    |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long group
group = get.pgrp( pid )
```

## Related topics
- [Process groups overview](overview.md)

- [Process groups synopsis](synopsis.md)
