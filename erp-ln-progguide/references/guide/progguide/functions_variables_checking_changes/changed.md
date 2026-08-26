# changed()

## Syntax:
`function boolean changed( string variable, [ long keep.flag.raised ] )`

## Description
This compares the current value of the specified variable with its checkpoint value to determine whether or not the value has changed.

## Arguments
| | | |
|---|---|---|
| `string` | `variable` |  The *variable* that is monitored.  |
| `[ long` | `keep.flag.raised ]` |  If the parameter *keep.flag.raised* gets the value KEEP.CHANGED.FLAG.RAISED, the function changed() works as a 'peek' and won't touch the status of the traced variable. See also the NOTE.  |

## Return values
TRUE variable has changed
FALSE variable has not changed

## Context
This function is implemented in the porting set and can be used in all script types.
Note  When the 'keep.flag.raised' parameter is not used, this function returns TRUE only if the value of the variable has changed since the last time you called the function. In other words, calling changed() without the extra parameter resets the internal trace flag for this variable and sets the current value as the new checkpoint.

## Related topics
- [Variables (checking changes) overview](overview.md)
- [Variables (checking changes) synopsis](synopsis.md)
- [Variables (checking changes): sample program](example.md)
