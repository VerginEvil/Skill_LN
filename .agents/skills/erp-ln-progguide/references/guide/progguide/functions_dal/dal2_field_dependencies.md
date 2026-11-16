# DAL2 Field dependencies

## Overview
Since the introduction of the DAL concept, the integrity checks have moved from the UI scripts to the Data Access Layer. However, with the DAL concept being implemented, still a lot of business logic remains in the UI scripts. An important category is the logic to determine defaults at the time of inserting a record (in the *before.new.object* section) and after a field change (in the *when.field.changes* section).
In order to be able to re-use this logic, this logic should be moved to the DAL. DAL2 allows you to do that. For this the [field.update()](field.update.md) hook has been introduced.
In the Corelli release it was already possible to define a field sequence in the Table Definitions session for determining defaults. Baan OpenWorld uses this sequence to call the [fieldname.set.defaults()](fieldname.set.defaults.md) hooks in the right order. The main drawback of this is that these hooks are not called by the [4GL engine](../glossary/glossary.md#fourgl_engine) or the [Data Access Methods (DAM)](dam.md). This also makes it very hard to test the hooks.
The DAL2 concept now makes it possible to define field dependencies in such a way that they can also be used by the Infor Enterprise Server applications in order to determine default values. Once these field dependencies are defined, they are used in order to trigger dependent fields to update themselves when required.
Another difference with Corelli is that the field dependencies are also used by the [4GL engine](../glossary/glossary.md#fourgl_engine) in order to update the User Interface, with regards to disabling/enabling of fields and determining enum values.
The following functions are available to define and handle field dependencies:

- [dal.field.depends.on()](dal.field.depends.on.md)

- [dal.require.field()](dal.require.field.md)

- [dal.any.parent.changed()](dal.any.parent.changed.md)

## Example
Suppose we have table temmt020 Currencies in which, amongst others, the following 3 fields exist:

- temmt020.prnt - Parent Currency of the Currency being edited

- temmt020.sdat - Start date of the relation between the Currency and its Parent Currency

- temmt020.edat - End date of the relation between the Currency and its Parent Currency

An example of this relationship could be the Euro (EUR) currency being the parent of the Dutch Guilder (NLG) with a start date of 1999-01-01 and an end date of 2002-06-30.
The following direct field dependencies exist:

- temmt020.prnt --& temmt020.sdat

- temmt020.prnt --& temmt020.edat

- temmt020.sdat --& temmt020.edat

Here you can see that the start date depends only on the parent currency, and that the end date depends on both the parent currency and the start date. This is defined in the [before.open.object.set()](before.open.object.set.md) hook as follows:
```

function extern long before.open.object.set()
{
    ...

    dal.field.depends.on("temmt020.sdat",
        HOOK_IS_APPLICABLE + HOOK_UPDATE,   "temmt020.prnt")
    dal.field.depends.on("temmt020.edat",
        HOOK_IS_APPLICABLE + HOOK_UPDATE,   "temmt020.prnt",
        HOOK_UPDATE,            "temmt020.sdat")

    ...

    return(0)
}
```
Explanation:

- the Start Date (temmt020.sdat) field only depends on the Parent Currency (temmt020.prnt) field. The Parent Currency field is used in both the temmt020.sdat.is.applicable() and temmt020.sdat.update() hooks.

- the End Date (temmt020.edat) field depends on both the Parent Currency and the Start Date fields. The Parent Currency field is used in the temmt020.edat.is.applicable() and temmt020.edat.update() hooks. The Start Date field is only used in the temmt020.edat.update() hook.

- the is.applicable() hook is called in order to see if the Start and End Date fields must be cleared. In case the field is applicable, then the update() hook is called. Note that this is also the case if the HOOK_IS_APPLICABLE dependency is defined without a HOOK_UPDATE dependency.

In case the Parent Currency field changes, then the is.applicable() and update() hooks of the Start and End Date fields will be executed, so that these fields can determine a correct value based on the value of the Parent Currency:
```

function extern void temmt020.sdat.update()
{
    if temmt020.prnt = temmt001.euro then
        temmt020.sdat = date.to.num(1999, 01, 01)
        return
    endif
    if temmt020.sdat = 0 and temmt020.sdat.is.mandatory() then
        temmt020.sdat = date.num()
        return
    endif
}

function extern void temmt020.edat.update()
{
    if temmt020.prnt = temmt001.euro then
        temmt020.edat = date.to.num(2002, 06, 30)
        return
    endif
    if temmt020.edat = 0 and temmt020.edat.is.mandatory() then
        set.max(temmt020.edat)
        return
    endif
    if temmt020.sdat > temmt020.edat then
        temmt020.edat = temmt020.sdat
        return
    endif
}
```
The [4GL engine](../glossary/glossary.md#fourgl_engine) also uses the defined field dependencies in order to (re)determine the new state of the dependent fields with regards to enabling/disabling and - for enum fields - the applicable enum values.

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [field.update()](field.update.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)
