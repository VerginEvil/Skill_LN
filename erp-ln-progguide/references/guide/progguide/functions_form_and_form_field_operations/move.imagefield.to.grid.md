# move.imagefield.to.grid()

## Syntax:
`function long move.imagefield.to.grid( const string image.field )`

## Description
If an image is added to an overview session it will be displayed in the view area of the session. This function can be used to move the image field from the view area to the grid. Be aware that moving an image to the grid can have a (major) performance impact. For each row the image needs to be retrieved and send to the frontend. An image should only be moved to the grid if having the image for each row directly displayed is a big advantage and the possible performance decrease is not a big issue.

## Arguments
| | | |
|---|---|---|
| `const string` | `image.field` |  The name of the image field to be moved to the grid.  |

## Return values
| | |
|---|---|
| 0 | Success, image field moved to the grid. |
| -1 | Function called from wrong section, should be called from after.form.read section. |
| -2 | Session is not running as an overview session. |
| -3 | Field not found. |
| -4 | Field is not of type image. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2410.
Note  Use this function only in the after.form.read section.

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
