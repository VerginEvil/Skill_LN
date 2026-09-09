# remove.session.index()

## Syntax:
`function long remove.session.index( long session.index )`

## Description
This removes the specified session index. Session index is identified by a session index number as defined by the session.
Removing session index 1 and removing the current active session index is not allowed.
Active session index can be found with the variable curr.key

## Arguments
| | | |
|---|---|---|
| `long` | `session.index` |    |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid session Index. Session index should be > 1 |
| -2 | Invalid session Index. Not allowed to disable the current index |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1801.
Note  Use this function only in the before.program section or after.form.read section.

## Example
```

after.form.read:
  	ret = remove.session.index(2)
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
