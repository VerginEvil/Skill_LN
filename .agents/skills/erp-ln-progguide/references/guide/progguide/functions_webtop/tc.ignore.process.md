# tc.ignore.process()

## Syntax:
`function void tc.ignore.process( boolean flag, [ long processno ] )`

## Description
This function indicates if the WebUI or LN UI should ignore this session (process). By default, the WebUI/LN UI does not ignore a session. Therefore this function should only be called from a 3GL session which does not present a User Interface. When this function is not called from such 3GL session, the WebUI/LN UI will seriously delay when such a 3GL Session is started.

## Arguments
| | | |
|---|---|---|
| `boolean` | `flag` |  true when the WebUI/LN UI must ignore this session, otherwise false.  |
| `[ long` | `processno ]` |  The process number of the session to which this function applies. When omitted this function is applied to the current session  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [WebUI/LN UI support functions overview and synopsis](overview_and_synopsis.md)
