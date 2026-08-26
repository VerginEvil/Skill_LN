# stat.set.real.utc()

## Syntax:
`function void stat.set.real.utc( const long i.utc )`

## Description
This function sets the real utc value of a Stat-field.

## Arguments
| | | |
|---|---|---|
| `const long` | `i.utc` |  The real value of the Stat-field for conditional formatting.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Not selectable stat. |
| -3 | Error creating symbol. |
| -6 | Error during saving real Stat value. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2520.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section of the field defined as a Stat.

## Related topics
- [Stat overview and synopsis](overview_and_synopsis.md)
