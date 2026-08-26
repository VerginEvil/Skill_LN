# skip.io()

## Syntax:
`function void skip.io( string mesg, [ string ... ] )`

## Description
*This function is deprecated!*
Use this to skip the current database action on the current record. The predefined variable *stp.skip.error* indicates whether or not *skip.io()* has been called.

## Arguments
| | | |
|---|---|---|
| `string` | `mesg` |  This specifies a message that is defined in the data dictionary. This message is displayed on screen when you call *skip.io()*. If you specify an empty string, the 4GL engine displays a default message.  |
| `[ string` | `... ]` |  The message can contain substitution symbols such as %d or face= %s (see [sprintf$()](../functions_formatting_io/sprintf.md). The values that must be substituted are specified in the second, third, etc. arguments of the function. The number of arguments is variable.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  For performance reasons, it is preferable to use [query.extend.where()](../functions_sql_query_extensions/query.extend.where.md) instead of *skip.io()*.

## Example
```

main.table.io:
before.delete:
                if pctst999.number = 0 then
                                skip.io("pctsts0010")
                                | record with number zero may not
be deleted
                endif
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
