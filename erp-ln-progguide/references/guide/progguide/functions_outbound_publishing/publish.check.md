# publish.check()

## Syntax:
`function long publish.check( const string bus.component.name, ref long result.xml )`

## Description
This function checks whether a destination (bus component) is available for publishing events. Note that publish.open() and publish.message() will not always report errors, but will send messages to an error handler or log file instead. To avoid publishing many message to the error handler or log file, this check function can be used before using publish.open().

## Arguments
| | | |
|---|---|---|
| `const string` | `bus.component.name` |  (input) Name of the bus component to be used.  |
| `ref long` | `result.xml` |  (output): xml containing result in case of errors or warnings; see [Outbound Publishing functions overview](overview.md) for details. The result.xml is available if return value <> 0.  |

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
