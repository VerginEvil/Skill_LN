# on.main.table()

## Syntax:
`function void on.main.table( string function_name, [ string ... ] )`

## Description
This copies the contents current record of the main table to the record buffer of that table, saves the record, and executes the specified function. After that the saved record buffer is restored. This enables you to perform actions on the record contents without affecting the values in the table.

## Arguments
| | | |
|---|---|---|
| `string` | `function_name` |  The name of the function that must be executed. The function must be of type void.  |
| `[ string` | `... ]` |  Use these optional arguments to pass one or more arguments to the function.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example
```

| Suppose you have a table to which you can add numbers only
| if a certain value is present in the main table

declaration:
                long go_ahead

field.pctst999.number:
check.input:
                on.main.table( check_number, 5 )
                if not go_ahead then
                                set.input.error("pctst0003", 5)
|"Number %d not present"
                endif

functions:
function void check_number( long number )
{
                select pctst999.*
                from pctst999
                where pctst999.number = :number
                as set with 1 rows
                selectdo
                                go_ahead = TRUE
                selectempty
                                go_ahead = FALSE
                endselect
                return
}
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
