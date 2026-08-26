# Object information tool
To display information about an object, use the object information tool bic_info6.2. Note that maximum information is displayed when the object has been compiled with the debug option.

## Syntax
```

bic_info6.2 [-aidshwcV] [-eu] [-f[flags]] object
```

## Options
```

-a
```
```

-I
```
```

-d
```
```

-s
```
```

-h
```
```

-w
```
```

-c
```
```

-V
```
```

-e
```
```

-u
```
```

-f
```
```

-f<flag>
```
| | |
|---|---|
|  | Show all available object information (default).  |
|  | Show instructions in object (Disassembler). This is only possible when the object is compiled with the debug option.  |
|  | Show used DLLs and where the external functions used are defined.  |
|  | Show list of used variables, (global) functions, string constants, and double constants.  |
|  | Show Object header. |
|  | Show #ident <strings>. |
|  |  Check checksum. exit(0) ok exit(1) corrupted  |
|  | Show version/release and portings information of bic_info6.2.  |
|  | Show prototypes of all external functions defined in the object.  |
|  | Show the general usage of the library (see below).  |
|  | Show flags. |
|  |  Check flags. When this options is used, all other options are ignored. <flag> can be a combination of the following: 1 NOTRANSACTION 2 DEBUG 4 PROFILE 8 DLL exit(0) flag(combination) is in object exit(1) flag(combination) is not in object  |
Combining -e and -u displays the description of the object and the descriptions and prototypes of all external functions within the object (see below).

## Object and function descriptions
You specify the object description between the keywords DLLUSAGE and ENDDLLUSAGE in the program script. You place the information outside all functions so that it is global for the entire program. The description should explain the general usage of the object. The description is added to the object and you can retrieve it with the command `<bic_info6.2 -u <object>`.
You also specify a function's description between the keywords FUNCTIONUSAGE and ENDFUNCTIONUSAGE in the program script. However, you place the information within the body of the function, between the { and } characters. The description should explain the general usage of the object, its arguments, and its return value, for example. You can retrieve function descriptions and prototypes with the command bic_info6.2 -eu <object>.

## Example
```

DllUsage
This is the object description.
EndDllUsage

function extern long abs( long arg )
{
        FunctionUsage
        This function returns the absolute value of the specified argument.
        Input:  ARG     The value for which the absolute value is to be returned.
        Output: -
        Return: the positive value of ARG.
        EndFunctionUsage

        return ( arg >= 0 ? arg : -arg )
}
```

## Related topics
- [Dynamic-link libraries](overview.md)
