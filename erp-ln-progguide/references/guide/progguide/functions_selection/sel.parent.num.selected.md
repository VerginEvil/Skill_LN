# sel.parent.num.selected()

## Syntax:
`function long sel.parent.num.selected( )`

## Description
This function returns the number of records that is selected in the parent of the current session.
If the number of records cannot be determined, -1 is returned.
Note  Note that this function returns the number of records that is selected in the parent session at the moment the function is called. If the selection changes because the parent is not blocked (the child is started modeless), the number is not valid anymore.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1075.
Note  This function is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Related topics
- [Record selection Overview](overview.md)
- [Record selection Synopsis](synopsis.md)
- [Improved Record selection Cookbook](cookbook.md)
