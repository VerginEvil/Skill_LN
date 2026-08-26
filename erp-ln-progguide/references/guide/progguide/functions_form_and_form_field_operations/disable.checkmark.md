# disable.checkmark()

## Syntax:
`function void disable.checkmark( string field [,occurrence],... )`

## Description
This disables single-occurrence and multi-occurrence checkmarks on a form.
Field will be displayed as checkbox after this function is applied.
Because the information is not available, you can not use this function in the before.program section.

## Arguments
| | | |
|---|---|---|
| `string` | `field [,occurrence],...` |  This identifies the checkbox field to be disabled. For array fields you can append suffixes to the field name to indicate the particular element or segment to be disabled. If you omit these suffixes, all elements/segments are disabled. To disable a particular element of an array field, append the element number (in parentheses) to the field name. The element number must be an integer, formatted as a string. It cannot be a variable. For example: "tfmod100.perd(10)".  |
-

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Availability  This function is available from TIV 2040.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
