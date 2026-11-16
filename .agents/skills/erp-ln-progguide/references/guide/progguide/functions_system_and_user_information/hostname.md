# hostname$()

## Syntax:
`function string hostname$( [ boolean getcanonicalname ] )`

## Description
This returns the hostname of the local machine.
If no hostname is found, the function returns an empty string.

## Arguments
| | | |
|---|---|---|
| `[ boolean` | `getcanonicalname ]` |  As of TIV level 2000 this optional parameter has been added to this function. When the value of this parameter is true, then the canonical hostname is returned. It is up to the system or DNS administrator to provide a correct name. It is a common practice to return fully qualified names (FQN) when requesting for a canonical hostname.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

field.ttaad410.syst:
before.input:
        if isspace(ttaad410.syst) then
                ttaad410.syst = hostname$()
        endif
```

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
