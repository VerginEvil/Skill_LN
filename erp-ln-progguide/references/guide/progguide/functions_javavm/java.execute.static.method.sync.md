# java.execute.static.method.sync

## Syntax:
`function long java.execute.static.method.sync( string class.name, string method.name, [ void ... ] )`
`function long java.execute.static.method.async( string class.name, string method.name, [ void ... ] )`

## Description
Executes a Java static method, with no return type, within the JavaVM.
java.execute.static.method.sync() returns to the caller AFTER completion of the Java method.
java.execute.static.method.async() returns to the caller BEFORE completion of the Java method.
See also [java.execute.static.application.method](java.execute.static.application.method.md) for an alternative Java interface that allows a result to be returned from the Java method.

## Arguments
| | | |
|---|---|---|
| `string` | `class.name` |  name of the Java class to call (e.g.: com.baan.baanvm.Test)  |
| `string` | `method.name` |  name of the static Java method in that class to call (e.g.: runMe).  |
| `[ void` | `... ]` |  Optional parameters for that method. All BaanC types at this time (string, long, double) are supported. The 3GL type BOOLEAN is supported, but it maps to an int in Java. Also, it is worthwhile noting that the 3GL type LONG maps to the int type in Java.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| 0 | Success |
| -1 | JavaVM not supported on this platform; or unable to locate Java class and method at the Java end.  |
| -2 | JavaVM integration not available (not supported on this OS) |
| -3 | JavaVM integration not available (Java VM not properly configured). |
| -4 | Invalid method argument. |

## Example
```

    long retval
    long longArg
    string stringArg(30)

    | fill longArg and stringArg here...

    | This will call the "runMe" method in the given class that has a
    | signature of "runMe(int, string)"
    retval = java.execute.static.method.async("com.baan.baanvm.Test", "runMe", longArg, stringArg)
```

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
