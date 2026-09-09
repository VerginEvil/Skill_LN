# field.is.derived()

## Syntax:
`function boolean field.is.derived( [ long mode, long element ] )`

## Description
Use this hook to indicate whether the field is derived. If a field is derived then the [4GL engine](../glossary/glossary.md#fourgl_engine) makes the field readonly in the UI. The field however, still can have a value.
The difference with the readonly hook is: the field's value can be modified, but *only by the DAL to which the field belongs*. So the end-user is not allowed to change the field's value. Often, derived fields are *redundant* fields.

## Static vs. dynamic
Derived fields can be more or less static or dynamic:
| | |
|---|---|
| Static | The field will have a value derived from fields not belonging to the DAL's table. Examples: The Business Partner from the Order Header is added to the Order Lines for sorting purposes Fields like a Business Partner Balance, or a Quantity Received on an Order Line A Total Order Amount field that is stored in the database for performance reasons |
| Dynamic | The field will have a value derived from fields belonging to the DAL's table. Examples: Home Currency Amounts on an Invoice which is stored for performance reasons The start and end date that indicate the relation between the NLG and the EUR currencies. This is a fixed period starting at 1999-01-01 and ending at 2002-06-30. However, for other relationships this value does not have to be derived. |

## Public vs. private
Some derived fields are publicly known by other components, like the Stock on Order of an Item. Others are more or less an internal field (private fields).
*Public derived fields* could have a business method that allows other components to modify the field's value. Example:
```

function extern long update.stock.on.order(domain tegen.quan quantity)
{
        FunctionUsage
        Updates the Stock on Order of the current Item. The Item record is not yet
        written to the database.

        Preconditions
                -

        Postconditions
                the Stock on Order property is updated

        Parameters
                In  quantity    the quantity to update the Stock on Order with
                                if negative, the Stock on Order is decremented
                                if positive, the Stock on Order is incremented

        Returns
                0               on success
        EndFunctionUsage

        teitm020.ostk = teitm020.ostk + quantity
        return(0)
}
```
*Private derived fields* should be modified by means of the [field.update()](field.update.md) hook. Example:
```

|* Updates the Start Date
function extern void temmt020.sdat.update()
{
        |* In case the Parent Currency is the Euro, set the start date
        |* to 1999-01-01.
        if temmt020.prnt = temmt001.euro then
                temmt020.sdat = date.to.num(1999, 01, 01)
        endif
}
```

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  optional mode flag, one of { 0, DAL_NEW, DAL_UPDATE }  |
| `[ long` | `element ]` |  optional element number in case the field is an element of an array (for non array fields this value is 1)  |

## Return values
The hook should return True in case the field is derived. In that case the [4GL engine](../glossary/glossary.md#fourgl_engine) will make the field appear readonly on the UI. In any other case the hook should return False (i.e. the field is not derived).

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- At the time the [4GL engine](../glossary/glossary.md#fourgl_engine) determines whether fields need to be disabled cq. enabled: this is done just before calling the *before.display.object* and the *when.field.changes* sections

- At the time of checking the field's value, in case the field was changed

- Derived is defined as: the field's value is determined by the application. The end-user is *not* allowed to modify the field.

- If this hook does not exist, it is assumed that the field is not derived.

- The [4GL engine](../glossary/glossary.md#fourgl_engine) will show the following message to the end-user in case the field is changed and it appears to be derived: It is not allowed to change the %1$s field.

- It is advised to set an error message with [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the field is derived.

## Example
```

function extern boolean temmt020.sdat.is.derived()
{
        if temmt020.prnt = temmt001.euro then
            dal.set.error.message("tecals0493")
            |* Start date cannot be modified in case the Euro is
            |* chosen as parent currency.
            return(true)
        endif
        return(false)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)

- [DAL Context](dal_context.md)
