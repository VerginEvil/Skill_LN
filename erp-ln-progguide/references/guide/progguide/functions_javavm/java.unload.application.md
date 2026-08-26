# java.unload.application

## Syntax:
`function long java.unload.application( long handle )`

## Description
Unloads an application loaded by [java.load.application](java.load.application.md).
This will free some resources depending on the garbage collector of the JVM and invalidates the handle. The JVM is not stopped upon this call. The JVM is only stopped when the bshell stops.

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  The handle of the application to unload, previously obtained by a successful call to [java.load.application](java.load.application.md).  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2020.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| 0 | Success. |
| < 0 | Problems occurred. Additional details will be available in the message log. |
For an example, see [java.load.application](java.load.application.md)

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
- [java.load.application](java.load.application.md)
- [java.execute.static.application.method](java.execute.static.application.method.md)
