# set.input.error()

## Syntax:
`function void set.input.error( string mess.or.code, [ void arg... ] )`

## Description
This causes the [4GL engine](../glossary/glossary.md#fourgl_engine) to display the specified error message and to force input again in the same input field. If you specify an empty string, no error message is displayed.

## Arguments
| | | |
|---|---|---|
| `string` | `mess.or.code` |  Specifies either the data dictionary code for the message or a literal string. In the latter case, the value of *mess.or.code* must start with the at sign [@]. Note that using a literal string makes the script language dependent.  |
| `[ void` | `arg... ]` |  The literal string or message specified with *mess.or.code* can contain format characters for parameter substitution. The values which must be substituted are specified in the 2nd, 3rd,... arguments of the function. The number of these arguments is variable. For details about formatting a string see the [sprintf$()](../functions_formatting_io/sprintf.md).  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.

## See also
[dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()](dal.set.error.message.md)
Notes  You can use *set.input.error()* only in *check.input* event sections of a 4GL script. The error message is displayed after the entire section has been executed. Consequently, you cannot display two error messages with this function. The predefined variable *stp.check.input.error* (read-only) indicates whether *set.input.error()* has been called.
Before a *choice.update.db* (except at delete) section, all *check.input* sections of all fields are executed. If one error is set with *set.input.error()*, the remaining sections are not executed. In a type 4 program, which does not support *choice.update.db*, you can call the function [check.all.input()](../functions_form_and_form_field_operations/check.all.input.md) in a *before.choice* section. With the predefined variable *before.update.check* (read-only), you can check whether the input check is executed before update or during input.

## Example
```

field.pctst900.item:
check.input:
if before.update.check then
        set.input.error("pctsts0001")      | before update
else
        set.input.error("pctsts0002", e)   | during input
endif
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
