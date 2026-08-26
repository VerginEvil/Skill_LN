# remove.textfields()

## Syntax:
`function void remove.textfields( const string field.name.string, [ const string ... ] )`

## Description
The text manager completely ignores the named text field(s) for this session.

## Arguments
| | | |
|---|---|---|
| `const string` | `field.name.string` |  The name(s) of the text field(s) to be removed. See [Text fields overview](overview.md).  |
| `[ const string` | `... ]` |  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  This function can only be used in the before.program or after.form.read section.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
