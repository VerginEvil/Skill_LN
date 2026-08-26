# java.execute.static.application.method

## Syntax:
`function long java.execute.static.application.method( long Handle, ref string JavaReturnValue, string class.name, string method.name, [ void ... ] )`

## Description
Executes a versioned, dynamically loaded, Java method. These Java mehods can also return a (string) value to the 3 GL.

## Arguments
| | | |
|---|---|---|
| `long` | `Handle` |  A handle to a loaded application, obtained by a previous successful call to [java.load.application](java.load.application.md).  |
| `ref string` | `JavaReturnValue` |  The Java method can return any type that supports the toString() method. All return values are converted to a string. When an invoked method returns a null, this is converted to the empty string (the bshell does not have the concept of null pointers). So everything is returned as a string value to the bshell: a long is returned as a decimal string, a string is returned "as is", etc. This parameter is passed by reference and only valid when the return code of the function is 0 (success). A non-zero return value indicates a problem and in that case the JavaReturnValue is not used.  |
| `string` | `class.name` |  The Name of the Java class to call (e.g.: com.baan.baanvm.Test). This must be the name of a valid Java class in the (currently loaded) version of the application.  |
| `string` | `method.name` |  Name of the static Java method in that class to call (e.g.: runMe). This must be the name of a static method, returning a type that can be converted to a string (all return values are cast to a string). The selected class must have a parameter signature that matches the parameters that you specify. When one of these restrictions is violated, the function will return a non-zero value and the log will provide more details.  |
| `[ void` | `... ]` |  Optional parameters for that method. All BaanC types at this time (string, long, double) are supported. The 3GL type BOOLEAN is supported, but it maps to an int in Java. Also, it is worthwhile noting that the 3GL type LONG maps to the int type in Java. The signature of the method that you are calling must match the signature used by the 3GL call. It is supported to have several methods with the same name and different signatures. The matching method is selected automatically.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| 0 |  Success. The JavaReturnValue will contain the return value of the Java method. All return values are converted to a string (using toString() in Java) and returned to the bshell as a string. More complex interaction with Java can be achieved by means of message queues.  |
| -1 | Java not available or not licensed. |
| -2 | Java virtual machine could not be started (resource problems). |
| -3 | Invalid (unknown) handle specified. |
| -4 | Internal (resource) problems handling a request. |
| -5 | Invalid method (does not exist, bad signature, return type, etc) or error during execution of the method (Java exception).  |
More detailed error information may be available in the log file.
For an example, see [java.load.application](java.load.application.md)
Note: Java applications can be debugged using the -tracelevel option of the Bshell. This is translated as follows:
| | | |
|---|---|---|
| 0 | No Extra Logging | Level.SEVERE |
| 1 | Some Details | Level.WARNING |
| 2 | More Details | Level.INFO |
| 3 | Full Details | Level.FINE |
The Java application can log messages by using the standard Java logger:
```

Logger logger = Logger.getLogger("TestLogging");

logger.log(Level.FINEST,  "Level >= 3: Finest message");
logger.log(Level.INFO,    "Level >= 2: Info message");
logger.log(Level.WARNING, "Level >= 1: Warning message");
logger.log(Level.SEVERE,  "Level >= 0: severe message");
logger.log(Level.SEVERE, "Exception", new Exception("EXCEPTIONTEST"));
```
Level SEVERE is equivalent to an error: those messages will show up in the error log of the bshell and in the trace file.
All other levels (WARNING, INFO and FINEST) will show up only in the trace file, and only when the current tracelevel is high enough to show them.
Thrown exceptions will show up in the bshell trace file with an accompanying stack trace.

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
- [java.load.application](java.load.application.md)
- [java.unload.application](java.unload.application.md)
