# Common variables
Unlike other variables, which can be used only within the program in which they are declared, common variables can be used in more than one program. Only string variables can be declared as COMMON.
Common variables are automatically based on a common memory part that can be used by several programs. For this reason they must be declared as BASED. The fact that they are common must be indicated with the reserved word COMMON.
Declaration of common variables must be located outside every function. So they must be declared as global variables.

## Example
In program 1 and program 2, the same memory space is used for variables com_1 and com_2.
```

Within program 1:
        STRING      com_1(10) BASED, com_2(15) BASED
        COMMON      com_1, com_2
  <functions which use com_1 and com_2>

Within program 2:
        STRING      com_1(10) BASED, com_2(15) BASED
        COMMON      com_1, com_2
  <functions which use com_1 and com_2>
```
As an alternative to using common variables, you can use [import()](../functions_variables_interprocess_transfer/import.md), [export()](../functions_variables_interprocess_transfer/export.md), [get.var()](../functions_variables_interprocess_transfer/get.var.md) and [put.var()](../functions_variables_interprocess_transfer/put.var.md) to transport the values of variables between processes.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Variables](variables.md)
