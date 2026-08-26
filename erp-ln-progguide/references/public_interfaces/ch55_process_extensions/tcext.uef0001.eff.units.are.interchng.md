# tcext.uef0001.eff.units.are.interchng

> Chapter: Chapter 55 Process Extensions
>
> Group: Process Extensions for EffectivityUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 2006-2008

```baan
Syntax: long tcext.uef0001.eff.units.are.interchng(
domain  tcitem           i.item,
domain  tcuef.effn       i.alternative.eff.unit,
domain  tcuef.effn       i.original.eff.unit,
boolean          i.standard.interchangeable,
ref             boolean          o.custom.rules.applied,
ref             boolean          o.interchangeable )
Usage:        Expl:   Use this method to add to or replace the standard logic
for the interchangeability check of 2 effectivity units.
This method is called during the check on interchangeability,
just before returning the result of the standard check.
Example 1: replace logic under certain conditions
o.custom.rules.applied = false
if <some condition> then
o.custom.rules.applied = true
if <some other condition> then
o.interchangeable = true
else
o.interchangeable = false
endif
endif
return(0)
Example 2: add logic when result standard check = not interchangeable
o.custom.rules.applied = false
if i.standard.interchangeable = false then
if <some condition> then
o.custom.rules.applied = true
if <some other condition> then
o.interchangeable = true
else
o.interchangeable = false
endif
endif
endif
return(0)
Pre:    Inputs are validated by the calling function
If input is invalid (e.g. i.original.eff.unit does not exist),
then this extension funcion is not called.
Input:  i.item
The item for which the effectivity units are defined
i.alternative.eff.unit
Alternative effectivity unit
i.original.eff.unit
Original effectivity unit
i.standard.interchangeable (true / false)
Indicates if the 2 effectivity units are
interchangeable according the standard logic.
This information may or may not be used in the
customized logic.
Output  o.custom.rules.applied (true / false):
true:  custom logic is applied.
The calling function will use the result
of the check in this extension (o.interchangeable)
false: no custom logic is applied; the the calling function
will return the result of the standard check
o.interchangeable (true / false):
The result of the check in this extension.
Is only relevant when o.custom.rules.applied = true.
true:  i.alternative.eff.unit is interchangeable with
i.original.eff.unit
false: i.alternative.eff.unit is NOT interchangeable with
i.original.eff.unit.
Return: 0    : OK
<> 0 : Error in customized logic; use dal.set.error.message()
to set a clear error message.
The return code of the calling function (= standard check)
will indicate 'data not valid'.
```

## Process Extensions for ExceptionMessagesByItem

The following process extension(s) is/are available: ExceptionMessagesByItem.SkipPrint
