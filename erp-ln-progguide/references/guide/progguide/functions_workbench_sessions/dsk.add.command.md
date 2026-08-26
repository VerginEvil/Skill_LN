# dsk.add.command()

## Syntax:
`function void dsk.add.command( string command )`

## Description
Define a Workbench 3GL command. This method must be called before the call to start.ext.desk() is done.

## Arguments
```
function extern string command(long paramsNode)
```
| | | |
|---|---|---|
| `string` | `command` |  This parameter must contain the name of an external function which is defined in the 3GL script. This function will be called when the Workbench client application invokes this call. The signature of this 3GL function must be: This call back function is called when the Workbench client application wants to execute this command. The return value of this function will be returned to the Workbench client application. The format of this string must be agreed between the Workbench 3GL Session and the Workbench client application. The parameter paramsNode can be used to pass additional parameters from the Workbench client to this command. When parameters are passed by the Workbench client application, paramsNode is an XML object node, which contains one or more attributes. These attributes correspond with the "commandParameters" passed to the ExecuteCommand() client method  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Workbench Sessions overview](overview.md)
- [Workbench Sessions synopsis](synopsis.md)
