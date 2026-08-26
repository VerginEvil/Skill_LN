# Improved Record selection Cookbook

## Introduction
When moving a UI script from a [Tools Interface Version (TIV)](../tiv/tiv_overview.md) level below [TIV 1075](../tiv/tiv_1075.md) to [TIV 1075](../tiv/tiv_1075.md) or higher, rework might be needed because the 4GL engine uses a new record selection mechanism. Rework may be needed when one of the following variables or functions is used:
| | |
|---|---|
| [marked](../misc/predefined_variables.md) | doesn't work anymore |
| [unmarked](../misc/predefined_variables.md) | doesn't work anymore |
| [mark.table](../misc/predefined_variables.md) | only reflects the state of records that are visible in the window. Note that with TIV higher than 1075 there can also be records selected that are not visible, but are scrolled out of the window. For this purpose, [do.selection()](../functions_form_and_form_field_operations/do.selection.md) can be used.  |
| [choice.global.delete](../4gl_features/4gl_choice_sections.md) | doesn't work anymore |
| [mark.occ()](../functions_form_and_form_field_operations/mark.occ.md) | behavior has changed, see [mark.occ()](../functions_form_and_form_field_operations/mark.occ.md) |
So in case the above variables are not used, no rework is needed. There are a couple of scenarios in which the above variables are used. The most important ones are mentioned below.

## Use mark.occ to append records to selection
When you want [mark.occ()](../functions_form_and_form_field_operations/mark.occ.md) to append a record to the selection, specify true for the second argument of mark.occ . E.g.:
```

mark.occ( 1, true)
```
The behavior has changed because in most cases the application expects that only one record is selected after a find.data and a mark.occ. An example of such a construction is:
```

execute(find.data)
mark.occ( 1)
```

## Transfer selection to print/processing session
In different ways selections are transfered to child sessions for processing or printing. In all cases [mark.table](../misc/predefined_variables.md) is used. In most cases this construction can easily be replaced by the use of [do.parent.selection()](do.parent.selection.md) in the child session.

## Do a check in choice.mark.occur
There were three ways to check whether a record is selected in the after.choice section of the mark.occur event and act on that:
```

choice.mark.occur:
after.choice:
	if mark.table(actual.occ) then
		some.check()
	endif
```
or
```

choice.mark.occur:
after.choice:
	if marked = actual.occ then
		some.check()
	endif
```
or
```

choice.mark.occur:
after.choice:
	if not unmarked = actual.occ then
		some.check()
	endif
```
All these constructions only work if the choice section is executed for every record that is selected. With a TIV level below 1075 this is not the case when the user selects a range of record. With a TIV level of 1075 or higher the choice section is executed once for every mark action. So it is executed once when the user selects one record, and it is executed once when the user selects range of records (e.g. by using the a shift-click). Therefore, at least when moving to a TIV level of 1075 or higher, these constructions should be rewritten to something that uses [do.selection()](../functions_form_and_form_field_operations/do.selection.md). E.g.:
```

choice.mark.occur:
after.choice:
do.selection(false, some.check())
```

## Process selected records or enable/disable commands in mark.occur section
To process selected records a construction like the following is used. The same is also used for determining the state of commands after a user selected a record.
```

for counter = 1 to filled.occ
	if mark.table(counter) then
		restore.rcd.main(counter)
		do.it()
	endif
endfor
```
In both cases the construction must be replaced by a construction that uses [do.selection()](../functions_form_and_form_field_operations/do.selection.md). E.g.:
```

do.selection(false, do.it)
```

## check whether any record is marked
In some cases the value of the variable [marked](../misc/predefined_variables.md) is used to determine the whether there are any records selected. On these places the function [sel.num.selected()](sel.num.selected.md) must be used.
Note  Improved record selection functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Related topics
- [Record selection Overview](overview.md)
- [Record selection Synopsis](synopsis.md)
