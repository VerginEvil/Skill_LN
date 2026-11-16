# publish.close()

## Syntax:
`function long publish.close( long publication.id, ref long result.xml )`

## Description
This function closes a publication channel. After using this function, publish.message() and publish.error.message() cannot be used anymore unless a new publish.open() is done first.

## Arguments
| | | |
|---|---|---|
| `long` | `publication.id` |  (input) id for publication channel, which is provided as the return value of [publish.open()](publish.open.md)  |
| `ref long` | `result.xml` |  (output): xml containing result in case of errors or warnings; see [Outbound Publishing functions overview](overview.md) for details.  |

## Return values
| | |
|---|---|
| 0 | success. |
| <> 0 | an error value |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Outbound Publishing functions overview](overview.md)

- [Outbound Publishing functions synopsis](synopsis.md)
