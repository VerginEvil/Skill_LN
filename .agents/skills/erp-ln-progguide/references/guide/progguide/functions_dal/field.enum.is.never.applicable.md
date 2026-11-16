# field.enum.is.never.applicable()

## Syntax:
`function boolean field.enum.is.never.applicable( )`

## Description
Use this hook to indicate if the enum keyword is never applicable. If a keyword is never applicable then the [4GL engine](../glossary/glossary.md#fourgl_engine) will not display the keyword in the UI (it is made invisible at start up of a session). A keyword can become never applicable based on a static constraint, like a parameter setting, or a value in the same occurence.

## Return values
The hook should return true in case the keyword is never applicable. In that case the [4GL engine](../glossary/glossary.md#fourgl_engine) will remove the keyword from the UI. In any other case the hook should return False.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Scope
The derived set of enumerate values is limited to sessions using 4GL scripts.

## When called
- Just before the [4GL engine](../glossary/glossary.md#fourgl_engine) calls the *after.form.read* section of the UI script

Note  In this hook you should test on enum keyword that have a *static* nature. In practice this means that you will test keywords that do not belong to the business object you're dealing with. So you should not use this hook to test a keyword of an order header in the DAL of the order lines. Instead, think of parameter settings, user profiles. meta data etc.

## Example (fictive)
```

function extern boolean tpppc301.rest.inst.add.work.is.never.applicable()
|* Invoicing Inst. Additional Work
{
    |* Project Inventory in Costs
    if tpppc000.ipiw = tcyesno.yes then
        return(true)
    endif

    return(false)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
