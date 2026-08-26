# do.parent.selection()

## Syntax:
`function void do.parent.selection( long function_name, [ ... ] )`

## Description
This function can be used to process records selected in a parent session. For example: in a print session only print the records that are selected in the parent.
If updating the records is needed, then this should be done in the function "function_name". The function "function_name" is executed once for each marked record in the parent. At the moment the function is called, the primary keyfields of the marked records will be restored. If the function returns a value not equal to 0, then no more records are selected and do.parent.selection returns.

## Arguments
| | | |
|---|---|---|
| `long` | `function_name` |  The name of the function that must be executed for each marked occurrence. The function must be of type long.  |
| `[` | `... ]` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1075.

## Example
```

|fragment from ttams2200
...
on.choice:
	if exp.user = ttyeno.yes then
		if sel.use.parent.selection("ttaad200") then
			dump.completed = true
			do.parent.selection(dump.one.user, ttyeno.no, ttaad200.user)
		else
			dump.completed = dump.users( ttyeno.no, user.f, user.t)
		endif
		...
```

## See also
[do.selection()](../functions_form_and_form_field_operations/do.selection.md)
Note  This function is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md). For this function the TIV level of the parent session doesn't matter.

## Example
```

|fragment from ttams2200
...
on.choice:
	if exp.user = ttyeno.yes then
		if sel.use.parent.selection("ttaad200") then
			dump.completed = true
			do.parent.selection(dump.one.user, ttyeno.no, ttaad200.user)
		else
			dump.completed = dump.users( ttyeno.no, user.f, user.t)
		endif
		...
```

## Related topics
- [Record selection Overview](overview.md)
- [Record selection Synopsis](synopsis.md)
- [Improved Record selection Cookbook](cookbook.md)
