# Functions with variable number of arguments: overview
In the BAAN 3GL programming language, you can define a function with a variable number of arguments. For example:
```

function long change.attributes( long id, ... )
{
    |
    | some code
    |
}
```
The ellipsis [...] in the function definition indicates that the number of function arguments is variable, up to a maximum of 255. The function call determines how many and which arguments the function uses.
The functions described in this section enable programs to check how many arguments a function uses, to retrieve their types and values, and to assign values to them.
The arguments cannot be arrays.

## Related topics
- [Functions with variable number of arguments: synopsis](synopsis.md)

- [Functions with variable number of arguments: sample program](example.md)
