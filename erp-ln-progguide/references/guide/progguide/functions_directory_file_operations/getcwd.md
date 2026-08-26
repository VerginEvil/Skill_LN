# getcwd()

## Syntax:
`function string getcwd( )`

## Description
This returns the current path as a string. Note that on Windows NT systems, pathnames can include drive letters (for example, `c:/baan/bin`).

## Return values
The current path as a string. Or an empty string if an error occurs.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
