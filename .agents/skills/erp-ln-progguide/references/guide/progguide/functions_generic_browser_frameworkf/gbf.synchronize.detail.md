# gbf.synchronize.detail()

## Syntax:
`function void gbf.synchronize.detail( long key.object )`

## Description
Refreshes (synchronizes) the Details session of a Tree-Detail session

## Arguments
| | | |
|---|---|---|
| `long` | `key.object` |  A Key Object containing the key values of the record to be displayed.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2230.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restriction
This function may only be called by the application if the GBF is part of a Tree-Detail session.

## Related topics
- [Key fields Object overview](../functions_keyfields/overview.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)
