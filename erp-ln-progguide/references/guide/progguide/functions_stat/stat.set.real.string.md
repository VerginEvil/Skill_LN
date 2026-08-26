# stat.set.real.string()

## Syntax:
`function void stat.set.real.string( string i.domain(14), const string i.string )`

## Description
This function sets the real string value of a Stat-field.

## Arguments
| | | |
|---|---|---|
| `string` | `i.domain(14)` |  The name of domain for conditional formatting.  |
| `const string` | `i.string` |  The real value of the Stat-field for conditional formatting.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Not selectable stat. |
| -2 | Unknown domain. |
| -3 | Error creating symbol. |
| -4 | Type change of same real Stat-field. |
| -5 | Domain change of same real Stat-field. |
| -6 | Error during saving real Stat value. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2520.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section of the field defined as a Stat.

## Related topics
- [Stat overview and synopsis](overview_and_synopsis.md)
