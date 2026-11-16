# Function calls
The call of a function must have the same number of arguments as declared in the function header. Value arguments can be called using a constant or a variable; reference arguments can only be called using a variable. If the called function is not of type void, the function call must be assigned to a variable or used as value argument in another function call.
It is possible to use recursive function calls. This means that in a function block a call to the same function is used. However, this is currently implemented only for functions without local variables and arguments. In other situations, the following runtime message is generated: "Recursion not yet implemented".

## Related topics
- [3GL programming language features: overview](overview.md)

- [Functions](functions.md)
