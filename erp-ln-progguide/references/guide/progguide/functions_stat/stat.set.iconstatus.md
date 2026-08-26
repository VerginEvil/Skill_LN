# stat.set.iconstatus()

## Syntax:
`function void stat.set.iconstatus( const string i.iconstatus )`

## Description
This function sets the icon status of a Stat field. The icon status is displayed by the icon related to the status.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.iconstatus` |  The status that is represented by an icon on the Stat. Options: STAT.ICONSTATUS.ERROR STAT.ICONSTATUS.WARNING STAT.ICONSTATUS.SUCCESS STAT.ICONSTATUS.INFO STAT.ICONSTATUS.NONE STAT.ICONSTATUS.SELECTED Initial default: STAT.ICONSTATUS.NONE. If not given the icon status will not change.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section of the field defined as a Stat.

## Related topics
- [Stat overview and synopsis](overview_and_synopsis.md)
