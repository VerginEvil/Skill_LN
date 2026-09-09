# do.all.occ()

## Syntax:
`function void do.all.occ( <function_name>, [ <type>... ] )`

## Description
This executes the specified function for all occurrences on the current form. When included in the *before.choice* subsection of a *choice.update.db* section, the function is executed only for occurrences that are pending to be saved.
If the update.status has not yet been set, then do.all.occ() will first lock all records. After the function has been executed for all occurrences, all fields of all occurrences are redisplayed.

## Arguments
| | | |
|---|---|---|
| `<function_name>` |  | The name of the function that must be executed. The function must be of type void. |
| `[ <type>` | `... ]` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[do.occ()](do.occ.md), [do.occ.without.update()](do.occ.without.update.md), [do.selection()](do.selection.md), [on.old.occ()](on.old.occ.md)

## Example
```

declaration:
    long old.inventory

choice.cont.process:
on.choice:
    do.all.occ(update.occurrences, 9999)

main.table.io:
before.rewrite:
    on.old.occ(get.old.inventory)
    pctst999.change = pctst999.item - old.inventory

functions:

function void update.occurrences(long new.val)
{
    pctst999.special = new.val
}

function void get.old.inventory()
{
    old.inventory = pctst999.item
}
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
