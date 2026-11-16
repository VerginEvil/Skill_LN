# set.file.for.textfield()

## Syntax:
`function void set.file.for.textfield( const string field.name.string, string filename )`

## Description
This fills the textbox of a text field with the contents of a specified file present on the server.

## Arguments
| | | |
|---|---|---|
| `const string` | `field.name.string` |  The name of the multiline text formfield. For example, "ttadv996.type". For an array field, include the array element. For example, "tttadv996.type(5)".  |
| `string` | `filename` |  The path and the name of the file to display in the textbox.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  This function cannot be used in the before.program or after.form.read section, and cannot be used on input fields.

## Example
```

group.1:
init.group:
set.file.for.textfield("info.text", "${BSE}/log/log.bshell")
```

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
