# refresh.all.occs()

## Syntax:
`function void refresh.all.occs( )`

## Description
This re-reads all records that are currently on the screen and refreshes them (after all processes are idle).
Note that this is not done in the following cases:

- One of the occurrences on the screen has been modified by the user, but not yet saved.

- An occurrence is being added in an editable grid session.

- The session is a parent session and it has been updated due to the adding of a record in a synchronized dialog. In that case the occurrences of the parent session are not ordered on the screen: the record being added appears at the end of the grid.

This function works in both overview and details sessions.
This function does not work in display sections.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Process Change Manager (PRCM)
You can use this function in combination with the [Process Change Manager overview](../functions_prcm/overview.md) functionality to refresh occurrences. In case updates have been done by other sessions on one or more tables that your session uses, PRCM can be used to notify your session about those changes. Your session then can refresh its data. The refresh.all.occs will set an indicatore and the real refresh is done when the prcm command or any other command is finished.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
