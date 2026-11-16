# delete.image()

## Syntax:
`function boolean delete.image( string guid, long company, [ boolean no.transaction ] )`

## Description
This function will delete an image and all it's thumbnails

## Arguments
| | | |
|---|---|---|
| `string` | `guid` |  The unique identification that is assigned to this image set  |
| `long` | `company` |  The company for which the image is stored.  |
| `[ boolean` | `no.transaction ]` |  Delete the image without transaction handling. This argument is available from TIV 2522  |

## Return values
| | |
|---|---|
| true | Successful |
| false | The Image did not exist |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Images on Forms Overview](overview.md)

- [Images on Forms synopsis](synopsis.md)

- [Images on Forms Examples](examples.md)
