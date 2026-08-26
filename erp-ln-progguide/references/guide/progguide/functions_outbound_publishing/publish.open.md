# publish.open()

## Syntax:
`function long publish.open( const string bus.component.name, ref long result.xml )`

## Description
This function initializes the publishing.

## Arguments
| | | |
|---|---|---|
| `const string` | `bus.component.name` |  (input) Name of the bus component to be used.  |
| `ref long` | `result.xml` |  (output): xml containing result in case of errors or warnings; see [Outbound Publishing functions overview](overview.md) for details.  |

## Return values
| | |
|---|---|
| 0 | Error. |
| <> 0 | Publication id to be used subsequently in [publish.message()](publish.message.md), [publish.error.message()](publish.error.message.md) and [publish.close()](publish.close.md) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Outbound Publishing functions overview](overview.md)
- [Outbound Publishing functions synopsis](synopsis.md)
