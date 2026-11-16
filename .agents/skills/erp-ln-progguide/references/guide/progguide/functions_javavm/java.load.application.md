# java.load.application

## Syntax:
`function long java.load.application( string Application.Name )`

## Description
Load the most recent version of a Java application and return a handle to be used in subsequent operations. A Java virtual machine (JVM) is started when required (or an existing one is used), see [Java VM integration - Infor Enterprise Server 3GL](overview.md) for details.

## Arguments
| | | |
|---|---|---|
| `string` | `Application.Name` |  Name of the Java program to load. The system will look for this name in the "java/application" subdirectory of the (landlord) BSE. There must be a file there called <package_comb>.pacc, which lists the details of the installed java applications) one per line) for that package combination in the given BSE and current package combination. The string you pass as Application.Name must be listed in this file at least once. Every line in the.pacc file consists of a tag name (the argument specified as Application.Name), a vertical bar (|) followed by the name of the directory the application is installed in. Each application can have multiple versions installed, the java.load.application will automatically determine the most recent version (the last matching line in the.pacc file) and use that. Every application can have dependent applications which are loaded recursively until all dependencies are satisfied. The application must have an application.xml file installed for this in the (versioned) application directory that lists the dependencies (even when there are none). When the loading process is successful, a handle is returned (a positive integer value). When problems are detected, a negative value is returned and one or more log messages are generated.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2020.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| > 0 | Success. The value is a handle that can be used in subsequent calls to [java.execute.static.application.method](java.execute.static.application.method.md). Eventually, the handle must be released (the application unloaded and the resources freed) by a call to [java.unload.application](java.unload.application.md). When the application exits without calling unload, the bshell will automatically call [java.unload.application](java.unload.application.md) for you to unload all active applications. |
| <= 0 | Unable to start a JavaVM on this platform (not supported, configuration or resource problem, application program not found, etc.). Additional details will be available in the message log. |

## Examples:
```

    long Handle, retval
    long MyInt
    string MyString
    string Answer(1000)

    Handle = java.load.application("TestApplication")
    if (Handle <= 0) then ReportProblemsAndExit()
    endif

    MyInt = 10
    MyString = "Hello, World!"
    retval = java.execute.static.method(Handle,Answer,"MyClass","MyMethod",MyInt,MyString)
    ...
    java.unload.application(Handle)
```
The Java code in an application TestApplication.java might contain a class + method like this:
```

    public class MyClass
    {
        public static String MyMethod (long a, String b)
        {
            return("MyMethod called with " + a + " " + b);
        }
    }
```
The file $BSE/java/application/b61au.pacc might look like follows (if the current package combination is b61au):
```

    TestApplication|tt7.6a/TestApplication/1
    TestDepA|tt7.6a/TestDepA/1
    TestDepB|tt7.6a/TestDepB/1
```
The file $BSE/java/application/tt7.6a/TestApplication/1/application.xml might look like:
```

    <application version="1.0">
      <dependencies>
	 <dependency name="TestDepA" />
      </dependencies>
    </application>
```
This would allow you to call java.load.application("TestApplication").
The system would see that the current version is installed in $BSE/java/application/tt7.6a/TestApplication/1. The TestApplication.jar and application.xml file would have to be stored in that directory.
Reading that application.xml file will tell the system that TestApplication version 1 depends on application TestDepA.
The TestDepA is found in the.PACC file as living in $BSE/java/application/tt7.6a/TestDepA/1, which is then loaded and its application.xml file ($BSE/java/application/tt7.6a/TestDepA/1/appication.xml) is read. This process is repeated until all dependencies are satisfied (or an error occurs in which case the function will fail and the log will show the details of the problem).
The above code would invoke the java method 'MyMethod' with parameters a=10 and b="Hello, World!". It would return the string "MyMethod called with 10 Hello, World!" which would show up in the Answer string in the 3GL code. The retval would be 0 in that case. When there is a problem, retval will be negative, Answer will be unaltered and the log will describe the problem.

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)

- [java.execute.static.application.method](java.execute.static.application.method.md)

- [java.unload.application](java.unload.application.md)
