# input.again()

## Syntax:
`function void input.again( )`

## Description
After input by a user, this forces the user to input the data again. If there is an input error, it is preferable to use [set.input.error()](../functions_message_handling/set.input.error.md) in the *check.input* subsection for the field.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

field.pctst999.item:
on.input:
          if pctst999.item(1;1) = "p" then
                  print_item()
                  input.again()
          endif
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
