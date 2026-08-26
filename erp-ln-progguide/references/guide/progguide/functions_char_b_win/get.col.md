# get.col()

## Syntax:
`function long get.col( )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This retrieves the number of the column where the cursor is currently positioned. The function uses [get.cp()](get.cp.md), so it is slower than that function.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
