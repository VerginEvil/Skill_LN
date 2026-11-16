# print.const()

## Syntax:
`function void print.const( )`

## Description
This displays a specified constant string value in the current form field. The current value of the database field is not affected.
If you do not include the *fill_string* argument, the field is filled with asterisk characters (*). If the argument is a string of length one, the field is filled with the specified character. If the argument is a string of length greater than one, the specified string is displayed in the field, without repetition. The maximum length for the string is 127 characters.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

field.pctst999.desc:
after.display:
        if pctst999.number = 0 then
                print.const("?")        | Display "????????" in the current field
        endif
        if pctst999.number = 99999 then
                print.const(" ")        | Blank the current field
        endif
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
