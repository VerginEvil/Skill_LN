# Functions
In a program, a function performs a particular task that can be executed many times, with different values. The syntax of a function is as follows (parts between brackets [] are optional):
```

FUNCTION [ function_type ] function_name( [ arglist ] )
{
        declaration of local variables
        statement(s)
        RETURN[( return_value )]
}
```
where *arglist* consists of one or more argument declarations with the following syntax:
```

[REFERENCE / CONST] argument_type argument_name
```
When including more than one argument declaration, use commas [,] to separate the declarations. Note that the key word REFERENCE can be replaced by REF.
Normally, the limit for the number of arguments is 255. From TIV level 2570 and higher and when using the bic command line argument -largecalls, it is possible to have functions with up to 2047 arguments. The same holds for variable arguments and optional arguments. The new limit also applies to bshell functions.
When a “largecalls” function in a DLL is called from another script or DLL, the calling script or DLL also needs to be compiled with the -largecalls bic command line option, even in case of variable arguments.
For further information about functions, see the following topics:

- [Function type and return value](function_type_and_return_value.md)

- [Local variables](local_variables.md)

- [Static variables](static_variables.md)

- [Global variables](global_variables.md)

- [External variables](external_variables.md)

- [Function arguments](function_arguments.md)

- [Function prototypes](function_prototypes.md)

- [Function calls](function_calls.md)

## Related topics
- [3GL programming language features: overview](overview.md)
