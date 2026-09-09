# refresh.curr.occ()

## Syntax:
`function void refresh.curr.occ( )`

## Description
This reads the current record and refreshes it on screen. All references on the form are read again. For example, in the case of a zoom from a field to a session where the record can be modified, calling *refresh.curr.occ()* refreshes the occurrence on the parent form also.
Note that the function locks the record before reading it; this is necessary for delayed locks.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
