# get.image.last.modified.date()

## Syntax:
`function domain ttutc get.image.last.modified.date( string guid, long sequence, [ string tablename ] )`

## Description
This function is used bind an image form field to the (table) field which holds the application GUID value. This function must be called from the *after.form.read* section or from the *before.display.object* section in the application UI script.

## Arguments
| | | |
|---|---|---|
| `string` | `guid` |  The unique identification that will be assigned to this image set.  |
| `long` | `sequence` |  A one based sequence number to identify a specific image in the set.  |
| `[ string` | `tablename ]` |  Optional argument in which the name of the table to which this image is linked is passed. The default value is the current maintable.  |

## Return values
| | |
|---|---|
| >= 0 | The last modified date of the image in UTC long format. |
| 0 | Error. The Image was not found |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2522.

## Related topics
- [Images on Forms Overview](overview.md)

- [Images on Forms synopsis](synopsis.md)

- [Images on Forms Examples](examples.md)
