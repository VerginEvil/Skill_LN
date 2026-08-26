# Local variables
Variables declared within a function block are local variables. They are accessible only within the function in which they are declared.

## Declaration, initialization, and scope
| | |
|---|---|
| Point of declaration | In the function between the brackets { }. |
| Syntax of declaration | <type> name |
| Initialization | The value of local variables is undefined with each function call. Local variables must always be initialized in the function.  |
| Scope (validity and time) | Only within and during function execution. |

## Example
```

function void test()
{
        long i                  | Local variable
        for i = 1 to 100         | Always to be initialized by user
                ....
        endfor
        return
}
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Functions](functions.md)
