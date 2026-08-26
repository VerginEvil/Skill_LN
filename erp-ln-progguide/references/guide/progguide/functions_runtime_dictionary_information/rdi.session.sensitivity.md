# rdi.session.sensitivity()

## Syntax:
`function long rdi.session.sensitivity( )`

## Description
Returns sensitivity of current session. The function rdi.session.sensitivity also checks all table fields on a form (if any). The returned sensitivity is the highest sensitivity applicable to a session of table field on a form.

## Return values
A value of 0 means that the session is not sensitive. A value of 1 - 99 is the sensitivity level. A value of < 0 or > 99 indicates an error.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
- [Tools Interface Version (TIV)](../tiv/tiv_overview.md)
