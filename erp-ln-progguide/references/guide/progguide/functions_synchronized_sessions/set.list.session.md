# set.list.session()

## Syntax:
`function void set.list.session( string sess_code )`

## Description
This changes the current details session to a list-detail session and also defines the overview session to be used for populating the list panel. Both sessions act on the same maintable and the details panel acts as the synchronized dialog of overview session.
When a record is saved in the details panel, the 4GL engine updates the occurrence in the list panel.
This function can be used only in the before.program section of 4GL scripts.

## Arguments
| | | |
|---|---|---|
| `string` | `sess_code` |  The session code of the overview session.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2140.
Notes  For this function to have effect:
- the current session must be started as a modeless single occurrence session.
- the overview session must have one group defined as a Navigation List group.

## Example
```

before.program:
    set.list.session("bpmdm0101m100")
    |* bpmdm0101m100 is the overview session with a navigation list group
```

## Related topics
- [Synchronized sessions synopsis](synopsis.md)
