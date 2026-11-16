# dsk.set.before.refresh()

## Syntax:
`function void dsk.set.before.refresh( string funcname )`

## Description
Define a Workbench "before.refresh" callback function. This callback function is called when function [dsk.refresh()](dsk.refresh.md) is called. The function dsk.set.before.refresh() must be called before the call to [start.ext.desk()](start.ext.desk.md) is done.

## Arguments
```
function extern void funcname(long arg)
```
| | | |
|---|---|---|
| `string` | `funcname` |  This parameter must contain the name of an external function which is defined in the 3GL script. The signature of this 3GL function must be: The parameter "arg" is used to pass additional information from the calling session to this Workbench session. It corresponds to the "arg" parameter passed to [dsk.refresh()](dsk.refresh.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Workbench Sessions overview](overview.md)

- [Workbench Sessions synopsis](synopsis.md)
