# choice.again()

## Syntax:
`function void choice.again( )`

## Description
This cancels execution of a standard command and transfers control to the [4GL engine](../glossary/glossary.md#fourgl_engine). Statements programmed after this function will never be executed. You can call this function during execution of a standard command. You can also call the function in field sections, as these are called indirectly during execution of some commands.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  It is not allowed to call `choice.again()` in the `choice.update` section, as this interferes with the transaction management of the [4GL engine](../glossary/glossary.md#fourgl_engine).

## Example
```

field.pctst999.item:
after.input:
	if pctst999.item = 99999 then
		mess("pctst.0001", 1)
		choice.again()
	endif

| Modifying a record with item = zero is not allowed
choice.modify.set:
before.choice:
	if pctst999.item = 0 then
		mess("pctst.0002", 1)
		choice.again()
	endif
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
