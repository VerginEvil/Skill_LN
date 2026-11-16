# enable.fields()

## Syntax:
`function void enable.fields( [ long mode ], string field [,occurrence],... )`

## Description
This enables the specified single-occurrence and/or multi-occurrence field(s) on a form.
To enable all fields of a group, see [enable.group()](enable.group.md).
The *field* argument identifies the field to be enabled. For a single-occurrence field, this is the field name. For a multioccurrence field, this can be either the field name or the field name followed by an occurrence number (depending on whether you wish to enable all occurrences of the field or only one particular occurrence).
For array fields, UTC fields, and segmented fields, you can append suffixes to the field name to indicate the particular element or segment to be enabled. If you omit these suffixes, all elements/segments are enabled.

- To enable a particular element of an array field, append the element number (in parentheses) to the field name. The element number must be an integer, formatted as a string. It cannot be a variable. For example: `"tfmod100.perd(10)"`.

- To enable only the date or time element of a UTC field, append either.date or.time to the field name. For example: `"ttadv300.cdat.time"`.

- To enable a particular segment of a segmented field, append *.segment.segment_id* to the field name. For example: "tiitm001.item.segment.1".

Because the information is not available, you cannot use this function in the before.program or after.form.read section.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  This is an optional argument. It has one possible value: ENABLE This is the default mode and does not need to be specified.  |
| `string` | `field [,occurrence],...` |  This identifies the field to be enabled. For a single-occurrence field, this is the field name. For a multioccurrence field, this can be either the field name or the field name followed by an occurrence number (depending on whether you wish to enable all occurrences of the field or only one particular occurrence). For array fields, UTC fields, and segmented fields, you can append suffixes to the field name to indicate the particular element or segment to be enabled. If you omit these suffixes, all elements/segments are enabled. To enable a particular element of an array field, append the element number (in parentheses) to the field name. The element number must be an integer, formatted as a string. It cannot be a variable. For example: "tfmod100.perd(10)". To enable only the date or time element of a UTC field, append either.date or.time to the field name. For example: "ttadv300.cdat.time". To enable a particular segment of a segmented field, append *.segment.segment_id* to the field name. For example: "tiitm001.item.segment.1".  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Examples
```

| Enable two named single-occurrence fields
enable.fields( "tccom010.beca", "tccom010.dsca" )

| Enable element number 10 of an array field
enable.fields( "tfmod100.perd(10)" )

| Enable elements 1 to 12 of an array field
for i = start to 12
	enable.fields( "month(" & str$(i) & ")" )
endfor

| Enable the date element of a UTC field
ttaad500.fidt = 0
enable.fields( "ttaad500.fidt.date" )

| Enable the first and second segments of a segmented field
enable.fields( "tcibd001.dfit.segment.1", "tcibd001.dfit.segment.2" )
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
