# discard.changed.image()

## Syntax:
`function void discard.changed.image( string fieldname )`

## Description
This function will discard an image which was possibly dropped on an image control and discard the saved backup image after a delete. This function is usually called from the *after.choice* section of choice: *recover.set*.

## Arguments
| | | |
|---|---|---|
| `string` | `fieldname` |  The name of the image field on the form.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Images on Forms Overview](overview.md)
- [Images on Forms synopsis](synopsis.md)
- [Images on Forms Examples](examples.md)
