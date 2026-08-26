# for.each.record.in.view.do()

## Syntax:
`function void for.each.record.in.view.do( string callback_function )`

## Description
Executes the specified UI script callback function for each record in the current view on the maintable.
This means that for the current view (e.g. a sales order), all records (e.g. all order lines) are fetched from the maintable one by one, and for each fetched record, the given callback function is called. In case the session has no view fields, then all records of the maintable are fetched.
Any filter, query extend etc. is taken into account. So e.g. a filter set by the user has influence on the number of records being fetched.

## Arguments
| | | |
|---|---|---|
| `string` | `callback_function` |  The name of the function that must be executed. The function must be of type 'extern long'.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1020.
Notes
- This function takes any filter, query extend etc. into account. So depending on e.g. the filter set by the user, a different set of records can be fetched.
- The callback function must be declared in the UI script as 'extern long'.
- This function is performance critical, especially if there are a lot of records in the view.

## Example
```

declaration:
    extern  domain  tfgld.amnt  total.d.amnt
    extern  domain  tfgld.amnt  total.c.amnt

choice.find.data:
after.choice:
    if actual.occ = filled.occ then
        reset.total.amounts()
        for.each.record.in.view.do("increment.total.amounts")
        display.total.amounts()
    endif

functions:

function void reset.total.amounts()
{
    total.d.amnt = 0
    total.c.amnt = 0
}

function void display.total.amounts()
{
    display("total.d.amnt")
    display("total.c.amnt")
}

function extern long increment.total.amounts()
{
    FunctionUsage
    Desc:   Increments the total debit and credit amounts.
    Note:   This callback function is executed by
'for.each.record.in.view()'.
        It acts like the 'selectdo' clause of an Embedded SQL
query.
    Pre:    -
    Post:   total.d.amnt or total.c.amnt incremented with the
transaction amount
    Input:  -
    Output: -
    Return: 0   to continue fetching the next record
        <> 0  to stop fetching
    EndFunctionUsage

    if tfgld102.dbcr = tfgld.dbcr.debit then
        total.d.amnt = total.d.amnt + tfgld102.amnt
    else
        total.c.amnt = total.c.amnt + tfgld102.amnt
    endif

    | Everything went fine
    return (0)
}
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
