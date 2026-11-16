# copy.image.to.company()

## Syntax:
`function long copy.image.to.company( long source.company, string source.guid, string source.tablename, long target.company, string target.guid, string target.tablename, [ boolean overwrite, boolean omit.transaction ] )`

## Description
This function will copy an image or set of images based on its guid into the image repository referred to by the target guid and company. This function can be used when copying records to a different company.

## Arguments
| | | |
|---|---|---|
| `long` | `source.company` |  The company for which the existing image is stored.  |
| `string` | `source.guid` |  The unique identification of an image existing in the repository.  |
| `string` | `source.tablename` |  The name of the table to which the source image is linked.  |
| `long` | `target.company` |  The company to which the image should be copied.  |
| `string` | `target.guid` |  The unique identification for the copy of the image.  |
| `string` | `target.tablename` |  The name of the table to which the target image should be linked.  |
| `[ boolean` | `overwrite ]` |  If for the target guid/table image set already exists then these will be deleted and overwritten with the image set referred to by the source.guid. Default value for overwrite is true.  |
| `[ boolean` | `omit.transaction ]` |  If this function is called inside of a transaction, this argument must be set to true. Otherwise this function will start a new transaction, which will lead to errors. The default value for omit.transaction is false.  |

## Return values
| | |
|---|---|
| 0 | Successful |
| -1 | The target exist and overwrite was false |
| -2 | The source Image does not exist |
| -3 | The copy of the image failed |
| -4 | Failed to call the copy function |
| -5 | The source and target image sets are equivalent after mapping logical tables |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2110.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  The second optional parameter, `omit.transaction` is available from TIV level 2120.

## Related topics
- [Images on Forms Overview](overview.md)

- [Images on Forms synopsis](synopsis.md)

- [Images on Forms Examples](examples.md)
