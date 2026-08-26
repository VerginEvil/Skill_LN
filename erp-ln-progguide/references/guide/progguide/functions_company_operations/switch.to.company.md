# switch.to.company()

## Syntax:
`function long switch.to.company( long new_compnr )`

## Description
This switches to another company and sets the read-only variable COMPNR to the specified company number. It performs several checks before switching company and switches company only if the checks are successful. For example, it checks if the user is authorized to change to the new company, it checks if the package combination linked to the old company contains the same package VRC's as the package combination linked to the new company, and it checks if the old and new companies have the same first day of the week.

## Arguments
| | | |
|---|---|---|
| `long` | `new_compnr` |  |

## Return values
| | |
|---|---|
| 1 | Success. |
| -1 | Company not available. |
| -2 | No permission to change to this company. |
| -3 | Package combination does not correspond with new company number.  |
| -4 | First day of the week does not correspond to first day of the week of original company.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  [compnr.check()](compnr.check.md) and *switch.to.company()* perform similar functions, but *switch.to.company()* performs additional checks. So *switch.to.company()* makes heavier demands on system resources.
Be aware that when there is a switch to another company, the user's first day of the week does not change, even if the new company has a different first day of the week. *switch.to.company()* returns an error value if the old and new companies have different first days of the week. *compnr.check()* does not.
Super users are authorized for all company numbers. They always have authority to switch to a different company number. In addition, super users can also use the data dictionary to authorize other users for particular company numbers.

## Related topics
- [Company operations overview and synopsis](overview_and_synopsis.md)
