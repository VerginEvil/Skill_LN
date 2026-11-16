# stat.set.value()

## Syntax:
`function void stat.set.value( const string i.value )`

## Description
This function sets the value (KPI) of a Stat field.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.value` |  The value (kpi) formatted as a string.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section of the field defined as a Stat.

## Related topics
- [Stat overview and synopsis](overview_and_synopsis.md)
