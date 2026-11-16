# sel.use.parent.selection()

## Syntax:
`function boolean sel.use.parent.selection( string parent_table )`

## Description
This function can be used in a print or a processing session to determine whether to user wants to print/process based on a selection range, or based on the selection that is made in the parent. If the user wants to use the selection of the parent, you should use the function [do.parent.selection()](do.parent.selection.md) to get the selection. The user can indicate his choice with an optionset. Read below how to create that option set.
Because the information is not available, you can not use this function in the before.program section.

## Arguments
| | | |
|---|---|---|
| `string` | `parent_table` |  The table code (e.g. tccom100) of which you need to process records.  |

## Return values
true User wants to use the selection of the given table. (This also means that the parent session has the given table as maintable.)
false User wants to specify a custom range.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1075.

## How the create the selection field
The user can indicate his choice with an optionset. For an example of such an optionset start session ttams2200m000 ("Convert Changes to Runtime DD") from session ttaad2500m000 ("User Data"). The optionset on the top is the selection field.
To create the selection field, open the form of the print/processing session in the Dynamic Form Editor. Mark a group that contains a selection range as 'Selection Group' and specify a table code for which the selection range applies. Now the selection field is generated.
If the print/processing session is then started from another session, the 4GLE will check whether any group on the print/processing session is a selection group with the same table as the maintable of the parent. If that is the case and a record is selected in the parent, the 4LE does the following:

- the option 'selection from parent' is selected

- the selection group is disabled

In all other cases:

- the selection field is made invisible

- the selection group is enabled

The default for the selection field is always ignored by the 4GLE, and if the 'selection from parent' is selected the 'Add to Job' button will always be disabled.
Note  This function is avialable from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Related topics
- [Record selection Overview](overview.md)

- [Record selection Synopsis](synopsis.md)

- [Improved Record selection Cookbook](cookbook.md)
