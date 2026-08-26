# compnr.check()

## Syntax:
`function boolean compnr.check( long new_compnr )`

## Description
This switches to another company and sets the read-only variable COMPNR to the specified company number. It checks whether the current session may be started in the specified company, and if so it switches.

## Arguments
| | | |
|---|---|---|
| `long` | `new_compnr` |  |

## Return values
| | |
|---|---|
| true | Session may be started in specified company; Company switched. |
| false | Session may not be started in specified company;; Company not switched. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  compnr.check() and [switch.to.company()](switch.to.company.md) perform similar functions, but *switch.to.company()* performs additional checks. So *switch.to.company()* makes heavier demands on system resources.
Be aware that when there is a switch to another company, the user's first day of the week does not change, even if the new company has a different first day of the week. *switch.to.company()* returns an error value if the old and new companies have different first days of the week. *compnr.check()* does not.
Super users are authorized for all company numbers. They always have authority to switch to a different company number. In addition, super users can use the data dictionary to authorize other users for particular company numbers.

## Example
```

if ( not compnr.check(200) ) then
     message( "No permission to change to this company number" )
endif
```

## Related topics
- [Company operations overview and synopsis](overview_and_synopsis.md)
