# free.mem()

## Syntax:
`function void free.mem( void variable )`

## Description
This deallocates memory space previously allocated to the specified variable by [alloc.mem()](alloc.mem.md). The freed memory becomes available for another allocation. The variable cannot be used again after deallocation, unless it is reallocated memory space again using *alloc.mem()*.

## Arguments
| | | |
|---|---|---|
| `void` | `variable` |  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Memory operations overview and synopsis](overview_and_synopsis.md)
