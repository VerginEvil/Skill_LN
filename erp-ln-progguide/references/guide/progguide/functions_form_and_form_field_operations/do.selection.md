# do.selection()

## Syntax:
`function void do.selection( long mode, function_name function_name, [ function_name ... ] )`

## Description
This executes the specified function for all marked occurrences. Depending on the mode parameter, this executes either [do.occ()](do.occ.md) or [do.occ.without.update()](do.occ.without.update.md) on the currently marked records.

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |  The mode. Specify true if [do.occ()](do.occ.md) should be used. This will lock the occurrences. Specify false if [do.occ.without.update()](do.occ.without.update.md) should be used.  |
| `function_name` | `function_name` |  The name of the function that must be executed for each marked occurrence. The function must be of type void.  |
| `[ function_name` | `... ]` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[do.occ()](do.occ.md), [do.occ.without.update()](do.occ.without.update.md) [do.parent.selection()](../functions_selection/do.parent.selection.md)

## Example
```

function extern void change.status()
{
    | Change the status of all marked occurrences
    do.selection(true, set.status, POSTED)
    execute(UPDATE.DB)
}

function void set.status(long new.status)
{
    ...
}
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Record selection Overview](../functions_selection/overview.md)
