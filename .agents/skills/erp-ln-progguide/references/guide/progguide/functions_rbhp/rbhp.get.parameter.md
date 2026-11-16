# rbhp.get.parameter()

## Syntax:
`#pragma used dll "ottstprbhp"`
`function string rbhp.get.parameter( const string name )`

## Description
This function returns the named drillback parameter value that was passed by the Role Based Home Page drillback URL. This function can be called from the application function: tcint.dll0001.drill.back(). This function can also be called from a 4GL session when it was started from a Role Based Home Page drillback.

## Arguments
| | | |
|---|---|---|
| `const string` | `name` |  The name of the parameter for which the value is requested. For example LogicalId. These names are case sensitive !  |

## Return values
The value of the named parameter or an empty string when this parameter was not present.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Role Based Home Pages overview](overview.md)

- [Role Based Home Pages synopsis](synopsis.md)
