# ostype()

## Syntax:
`function long ostype( )`

## Description
This function returns a long value that indicates the operating system environment. The possible values are:
| | |
|---|---|
| OS_WINDOWS_NT | All Windows variants. |
| OS_UNIX | All UNIX variants |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
