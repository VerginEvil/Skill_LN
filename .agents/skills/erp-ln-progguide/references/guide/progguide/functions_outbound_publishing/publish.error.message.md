# publish.error.message()

## Syntax:
`function long publish.error.message( long publication.id, long error.xml, ref long result.xml )`

## Description
This function reports an error instead of publishing a message. It can be used if a message could not be created or sent successfully. Note that the error message is not sent to the bus component as specified in publish.open(). Instead, the Adapter configuration specifies an error handler for the bus component and the error message is sent to that error handler. If the error handler cannot be found or is unavailable, the Adapter will take care that the error is logged.

## Arguments
| | | |
|---|---|---|
| `long` | `publication.id` |  (input) id for publication channel, which is provided as the return value of [publish.open()](publish.open.md)  |
| `long` | `error.xml` |  (input) error message to be published, which is an xml structure according to the Result definition of the BDE standard..  |
| `ref long` | `result.xml` |  (output): xml containing errors or warnings; see [Outbound Publishing functions overview](overview.md) for details. This only occurs if the functionality is unavailable in the current Adapter version; in all other cases the result.xml is empty.  |

## Return values
| | |
|---|---|
| 0 | success. |
| <> 0 | an error value (this only occurs if the functionality is unavailable in the current Adapter version) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Outbound Publishing functions overview](overview.md)

- [Outbound Publishing functions synopsis](synopsis.md)
