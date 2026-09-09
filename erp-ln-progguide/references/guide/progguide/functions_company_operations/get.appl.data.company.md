# get.appl.data.company()

## Syntax:
`function long get.appl.data.company( string package(2), string application.id(30) Application Identifier see ttadv4589m000 )`

## Description
This function read the application data company for a user. First a search for the setting of the current user is done. If there is no setting for the current user available, the generic settings for the environment is read.
The data read is stored via session ttadv4589m000

## Arguments
| | | |
|---|---|---|
| `string` | `package(2)` |    |
| `string` | `application.id(30) Application Identifier see ttadv4589m000` |    |

## Return values
| | |
|---|---|
| Company number | Success. |
| -1 | Company not found for the package application ID. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  Be aware that this function only returns a company number, and switching to that company needs to be done with the function [compnr.check()](compnr.check.md) or [switch.to.company()](switch.to.company.md).

## Related topics
- [Company operations overview and synopsis](overview_and_synopsis.md)
