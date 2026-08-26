# get.os.user()

## Syntax:
`function string get.os.user( )`

## Description
Retrieves the current OS user of the bshell

## Return values
Success returns the name of the OS user
Error An empty string is returned

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
