# disable.zoom.buttons()

## Syntax:
`function void disable.zoom.buttons( string field [,occurrence],... )`

## Description
This disables single-occurrence and multi-occurrence zoom buttons on a form.
This function can not be used in the before.program section.
The zoom button will only get disabled if the field is enabled. The state of the zoom button can only be changed if the field is enabled.

## Arguments
| | | |
|---|---|---|
| `string` | `field [,occurrence],...` |  This identifies the zoom button to be disabled. For a single-occurrence field, this is the field name. For a multioccurrence field, this can be either the field name or the field name followed by an occurrence number (depending on whether you wish to disable all occurrences of the zoom button or only one particular occurrence). For array fields, UTC fields, and segmented fields, you can append suffixes to the field name to indicate the particular zoom button of the element or segment to be disabled. If you omit these suffixes, all zoom buttons of all elements/segments are disabled. To disable the zoom button of a particular element of an array field, append the element number (in parentheses) to the field name. The element number must be an integer, formatted as a string. It cannot be a variable. For example: "tfmod100.perd(10)". To disable only the zoom button of the date or time element of a UTC field, append either.date or.time to the field name. For example: "ttadv300.cdat.time". To disable the zoom button of a particular segment of a segmented field, append.segment.segment_id to the field name. For example: "tiitm001.item.segment.1".  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## TIV
This function is available from TIV level 1900.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
