# group.exists()

## Syntax:
`function boolean group.exists( const string groupname )`

## Description
This checks whether a specified group is defined on the system. Whether group names are case-sensitive or case-insensitive is a system-dependent feature.

## Arguments
| | | |
|---|---|---|
| `const string` | `groupname` |  |

## Return values
TRUE group exists
FALSE group does not exist

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string groupid(12)

groupid = getenv$( "GROUP" )
if not group.exists( groupid ) then
       mess( "First create group " & groupid &
                   " on the system and restart the installation", 0 )
       exit()
endif
```

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
