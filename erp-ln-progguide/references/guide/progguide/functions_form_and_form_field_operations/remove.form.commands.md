# remove.form.commands()

## Syntax:
`function void remove.form.commands( string command,... )`

## Description
This removes the specified form command(s). Form commands are identified either by a function name or a session code. There is no way to restore or create a new form command.

## Arguments
| | | |
|---|---|---|
| `string` | `command,...` |   |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

after.form.read:
  if cost.calculation.not.implemented then
     remove.form.commands( "calculate.costs",
"calculate.extra.costs")
  endif
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
