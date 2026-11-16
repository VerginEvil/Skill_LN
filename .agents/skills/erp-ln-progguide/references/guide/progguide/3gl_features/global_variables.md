# Global variables
Variables declared outside any function block are global variables. You can use them in all functions that occur after the variable declaration.
*Declaration, initialization, and scope*
| | |
|---|---|
| Point of declaration | Outside the functions. |
| Syntax of declaration | <type> name |
| Initialization | At program start: numeric set to 0 strings "" |
| Scope (validity and time) | Valid anywhere in the source, throughout the execution. If any arguments or variables within a function are declared with the same name as a global variable, the global variable cannot then be accessed within that function. |

## Example 1
```

function test()
{
        return
}
long glob_var
function long dupl()
{
        return( glob_var * 2 )
}
```
In this example, *glob_var* is a global variable. It is not accessible in the test() function as it was declared after that function block. On the other hand, *glob_var* is accessible in function dupl().

## Example 2
```

long i

function void test()
{
        long i
        i = 10      | This is the local variable
                    | Nothing happens to the global variable 'i'
}
```

## Related topics
- [3GL programming language features: overview](overview.md)

- [Functions](functions.md)
