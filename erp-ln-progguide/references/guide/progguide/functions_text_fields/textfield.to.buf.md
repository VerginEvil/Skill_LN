# textfield.to.buf()

## Syntax:
`function long textfield.to.buf( string text_field, string buffer )`

## Description
Reads the text of a multiline text formfield and stores the text into the passed buffer. The passed buffer should be defined as a based string. This is only relevant for multiline text formfields in a non-maintable session.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the multiline text formfield that must be retrieved. See [Text fields overview](overview.md).  |
| `string` | `buffer` |  buffer for storing the text.  |

## Return values
> 0 number of characters copied to buffer
-1 field is not a multiline text formfield.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example
```

| suppose you have formfield freetext
extern domain tttxt.text freetext
| define own field for text of freetext
extern string freetext.text.app(1) based

field.freetext:
when.field.changes:
    textfield.to.buf("freetext", freetext.app)
```

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
