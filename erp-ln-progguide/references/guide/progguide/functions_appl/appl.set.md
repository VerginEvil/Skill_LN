# appl.set()

## Syntax:
`function long appl.set( const string name, long mode )`

## Description
This creates an application lock for the current application.

## Arguments
| | | |
|---|---|---|
| `const string` | `name` |  The name of the application lock. This must be unique.  |
| `long` | `mode` |  The type of application lock to set: APPL.READ APPL.WRITE APPL.EXCL APPL.WIDE You can combine APPL.WIDE with any one of the other lock types.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | application-wide lock present |
| -3 | internal error |
| > 0 | application lock already present; mode is returned  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  For performance and to reduce locking issues, it’s preferred to use appl.excl which is much faster. However appl.excl does not support application wide locking, which should only be used with care.

## Examples
This example sets a write-type application lock for all companies. Only the owner can modify the application's data in all companies.
```

appl.set("00112334455", APPL.WRITE + APPL.WIDE)
```
This example sets an exclusive-type application lock on a production order and subsequently deletes it.
```

if appl.set( "tisfc001" & tisfc001.pdno, APPL.EXCL ) > 0 then
        | Lock is already present, give message
        return
endif
...
appl.delete( "tisfc001" & tisfc001.pdno )
```

## Related topics
- [Application locks: overview](application_locks_overview.md)
- [Application locks: synopsis](application_locks_synopsis.md)
