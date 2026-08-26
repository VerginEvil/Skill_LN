# abort.io()

## Syntax:
`function void abort.io( string mesg(14), [ ... ] )`

## Description
This cancels the current database transaction.
After this function is called, new values entered on the form remain on the form and the predefined variable *stp.abort.error* is set to TRUE. In the case of a single-occurrence form, the transaction is then canceled without further actions. In the case of a multioccurrence form, the transaction is canceled but the user is given the opportunity to retry the updates that did not cause an error. If the user chooses to retry the updates, occurrences that caused an error are skipped and those that did not are updated. If the user chooses not to retry the transaction, the transaction is canceled without further action. The user can then start the update again or recover.

## Arguments
| | | |
|---|---|---|
| `string` | `mesg(14)` |  This specifies a message defined in the data dictionary. The message is displayed on screen when *abort.io()* is called. If you specify an empty string here, the 4GL engine displays a default message. The argument can contain substitution symbols such as %d or face= %s (see [sprintf$()](../functions_formatting_io/sprintf.md). The values that must be substituted are specified in the second, third, etc. arguments of the function. The number of arguments is variable.  |
| `[` | `... ]` |  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  *abort.io()* is implicitly called by the 4GL engine when a DALHOOKERROR is returned by, for example, a [before.save.object()](../functions_dal/before.save.object.md) or [after.save.object()](../functions_dal/after.save.object.md) function call.

## Example
```

main.table.io:
before.rewrite:
                select tiitm001.*
                from tiitm001 for update
                where tiitm001.item between :item.f and :item.t
                selectdo
                                tiitm001.cwar = "002"
                                db.update(ttiitm001, DB.RETRY)
                selecterror
                                abort.io("pctsts0010",
tiitm001.item)
                                | transaction canceled on item %s
                endselect
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
