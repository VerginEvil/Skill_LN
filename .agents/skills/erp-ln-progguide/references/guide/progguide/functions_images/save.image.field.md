# save.image.field()

## Syntax:
`function boolean save.image.field( string fieldname )`

## Description
This function is used to save an image, which is dropped onto the image control, into the repository or delete the image from the repository if deleted by the user. When an image with the bound guid already exists, it will be overwritten. This function should be called from the *after.update.db.commit:* section in a UI script and is only allowed when the image field is bound using [bind.image()](bind.image.md)

## Arguments
| | | |
|---|---|---|
| `string` | `fieldname` |  The name of the image field on the form.  |

## Return values
| | |
|---|---|
| true | When successful |
| false | When an error occurred |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Images on Forms Overview](overview.md)

- [Images on Forms synopsis](synopsis.md)

- [Images on Forms Examples](examples.md)
