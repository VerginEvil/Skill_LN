# on.old.occ()

## Syntax:
`function void on.old.occ( const string function_name, const string ... )`

## Description
This executes the specified function for the current occurrence, using the old values of the record. The record must have been previously modified.

## Arguments
| | | |
|---|---|---|
| `const string` | `function_name` |  The name of the function that must be executed. The function must be of type void.  |
| `const string` | `...` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[do.all.occ()](do.all.occ.md), [do.occ()](do.occ.md), [do.occ.without.update()](do.occ.without.update.md), [do.selection()](do.selection.md)
Note  In DAL scripts, [with.old.object.values.do()](../functions_db_operations/with.old.object.values.do.md) is the equivalent of *on.old.occ()*.

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
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
