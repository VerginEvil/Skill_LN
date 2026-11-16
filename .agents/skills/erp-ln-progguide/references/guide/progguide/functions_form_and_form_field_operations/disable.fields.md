# disable.fields()

## Syntax:
`function void disable.fields( [ long mode ], string field [,occurrence],... )`

## Description
This disables single-occurrence and multi-occurrence fields on a form.
To disable all fields of a group, see [disable.group()](disable.group.md).
Because the information is not available, you cannot use this function in the before.program or after.form.read section.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  This is an optional argument. It has two possible values: DISABLE This is the default mode and does not need to be specified. READONLY The field(s) become read-only fields that cannot be edited by the user.  |
| `string` | `field [,occurrence],...` |  This identifies the field to be disabled. For a single-occurrence field, this is the field name. For a multioccurrence field, this can be either the field name or the field name followed by an occurrence number (depending on whether you wish to disable all occurrences of the field or only one particular occurrence). For array fields, UTC fields, and segmented fields, you can append suffixes to the field name to indicate the particular element or segment to be disabled. If you omit these suffixes, all elements/segments are disabled. To disable a particular element of an array field, append the element number (in parentheses) to the field name. The element number must be an integer, formatted as a string. It cannot be a variable. For example: "tfmod100.perd(10)". To disable only the date or time element of a UTC field, append either.date or.time to the field name. For example: "ttadv300.cdat.time". To disable a particular segment of a segmented field, append *.segment.segment_id* to the field name. For example: "tiitm001.item.segment.1".  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Examples
```

| Disable two named single-occurrence fields
disable.fields( "tccom010.beca", "tccom010.dsca" )

| Change to read-only fields the current occurrences of the multi-
| occurrence fields tccom010beca and tcccom101.dsca
disable.fields( READONLY, "tccom010.beca", actual.occ, "tccom010.dsca",
                actual.occ )

| Disable element number 10 of an array field
disable.fields( "tfmod100.perd(10)" )

| Disable elements 1 to 12 of an array field
for i  = start to 12
                disable.fields( "month(" & str$(i) & ")" )
endfor

| Disable the date element of a UTC field
ttaad500.fidt = 0
disable.fields( "ttaad500.fidt.date" )

| Disable the first and second segments of a segmented field
disable.fields( "tcibd001.dfit.segment.1", "tcibd001.dfit.segment.2" )
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
