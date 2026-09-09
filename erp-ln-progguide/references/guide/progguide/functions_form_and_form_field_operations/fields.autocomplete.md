# fields.autocomplete()

## Syntax:
`function void fields.autocomplete( boolean try.autocomplete,..., [ string fieldname(18) ] )`

## Description
Auto-complete is automatically executed by the 4GLE for fields that have a reference path to another table and have a zoom session and has no button and is not segmented. With this function auto-complete can be turned off ( try.autocomplete = FALSE ) and on again ( try.autocomplete = TRUE ).
For array fields, the element number should be sent as part of the string, between brackets. See example

## Arguments
| | | |
|---|---|---|
| `boolean` | `try.autocomplete,...` |    |
| `[ string` | `fieldname(18) ]` |    |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function cannot be used in the `"before.program"` or `"after.form.read"` sections.

## Example
```

group.1:
init.group:
	fields.autocomplete(false, "ttadv200.cmod", "ttadv200.cmop(2)")
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
