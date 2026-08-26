# ncrs.is.session.empty()

## Syntax:
`function boolean ncrs.is.session.empty( )`

## Description
This function can be used in a print or a processing session in an init.form section. The function can be used to decide whether the functional default command should be triggered. Possible the default command is another one, than the command that actually trigges the wanted functionality. The function tells whether the session has no fields left, because the selection group has been made invisible.

## Return values
TRUE No fields are left, session won't be shown
FALSE Session will be shown

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1306.
Note  This function is avialable from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1306](../tiv/tiv_1306.md).

## Related topics
- [Record selection Overview](overview.md)
- [Record selection Synopsis](synopsis.md)
- [Improved Record selection Cookbook](cookbook.md)
