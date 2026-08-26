# appl.set.excl()

## Syntax:
`function long appl.set.excl( const string name )`

## Description
This creates an exclusive application lock for the current application.

## Arguments
| | | |
|---|---|---|
| `const string` | `name` |  The name of the application lock. This must be unique.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | application-wide lock present |
| -3 | internal error |
| > 0 | application lock already present; mode is returned  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
This example sets an exclusive application lock on a production order and subsequently deletes it.
```

if appl.set.excl( "tisfc001" & tisfc001.pdno ) > 0 then
        | Lock is already present, give message
        return
endif
...
appl.delete.excl( "tisfc001" & tisfc001.pdno )
```

## Related topics
- [Application locks: overview](application_locks_overview.md)
- [Application locks: synopsis](application_locks_synopsis.md)
