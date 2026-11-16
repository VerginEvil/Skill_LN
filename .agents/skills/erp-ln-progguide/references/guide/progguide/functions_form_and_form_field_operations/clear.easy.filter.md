# clear.easy.filter()

## Syntax:
`function void clear.easy.filter( )`

## Description
The clear.easy.filter() function is designed to reset both the advanced filter and the easy filter row.
This can be used in scenarios when view fields change and the filter does no longer apply.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2532.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  The function is used in specific sections of a 4GL Script
For a MMT satellite session:

- choice.first.set

- choice.bms

For Overview session with view fields

- choice.first.view

- choice.prev.view

- choice.next.view

- choice.last.view

## Examples
Here is an example of how clear.easy.filter() is implemented and used in an MMT session:
The MMT controller session contains an option to toggle the usage of clear.easy.filter in the satellites
```

|* The controller session code.
extern 	boolean	g.skip.clear.filter
function extern	toggle.clear.filter()
{
	if g.skip.clear.filter then
		g.skip.clear.filter = false
	else
		g.skip.clear.filter = true
	endif

	set.checked.command("toggle.clear.filter", g.skip.clear.filter)
}

|* The satellite session code
choice.first.set:
	clear.filter()

functions:
function clear.filter()
{
static	domain	tcorno	l.orno
	boolean		skip.clear

	if isspace(l.orno) then
		l.orno = tdpur401.orno
	endif

	|* check if the key field has changed.
	if tdpur401.orno <> l.orno then
		import("g.skip.clear.filter", skip.clear)
		if not skip.clear then
			clear.easy.filter()
		endif
		l.orno = tdpur401.orno
	endif
}
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
