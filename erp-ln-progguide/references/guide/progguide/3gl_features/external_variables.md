# External variables
An external variable is declared outside the function blocks. You can use them in all functions that occur after the variable declaration, and also in other programs (for example, forms, reports, and runtime expressions). It is possible to declare external variables within a function block but this is not recommended.
If a local variable has the same name as an external variable, the local variable is used within the function. The external variable is not affected.

## Declaration, initialization, and scope
| | |
|---|---|
| Point of declaration | Outside the functions. (Or within a function, but this is not recommended.)  |
| Syntax of declaration | extern <type> name |
| Initialization |  At program start: numeric set to 0 strings ""  |
| Scope (validity and time) | Valid anywhere in the source, throughout the execution. Also valid outside the program. For example, on forms/reports, in runtime expressions, and by way of [import()](../functions_variables_interprocess_transfer/import.md) and [export()](../functions_variables_interprocess_transfer/export.md).  |

## Example
```

extern long   i
function void test()
{
        i = 10        | This is the external variable
}
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Functions](functions.md)
