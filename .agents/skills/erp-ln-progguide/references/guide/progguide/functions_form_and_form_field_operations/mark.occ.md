# mark.occ()

## Syntax:
`function void mark.occ( long occurence )`

## Description
This marks the specified occurrence with a reverse bar, makes the marked record the current record in the database, and sets the predefined variable *actual.occ* to the marked occurrence.
For sessions with [TIV](../tiv/tiv_overview.md) lower than [TIV 1075](../tiv/tiv_1075.md) the following predefined variables are relevant to this function:
| | |
|---|---|
| marked | Use this to check whether an occurrence is marked or not. This can also be tested in the *on.exit* subsection of a zoom process. |
| mark.status | This is available in the subsections *before.choice* and *after.choice* of *choice.mark.occur*. It indicates the type of marking that the [4GL engine](../glossary/glossary.md#fourgl_engine) is executing. It can have the following values: DUPL.OCCUR during marking for copying TEXT.MANAGER during marking for edit text 0 in all other cases and when not marking |
For sessions with [TIV](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md) or higher see the [Form and form field operations synopsis](synopsis.md) for an overview of related functions and variables.

## Arguments
| | | |
|---|---|---|
| `long` | `occurence` |    |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  This function will do nothing, in case a field has input in an editable grid session.
Use [remove.mark()](remove.mark.md) to clear the selection.
The default behavior for sessions with [TIV](../tiv/tiv_overview.md) lower than [TIV 1075](../tiv/tiv_1075.md) is that the occurence is added to the selection. For sessions with [TIV](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md) or higher the default is that the selection is cleared and only one occurence is selected. However it is possible to change this behavior with the optional argument addToSelection.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
