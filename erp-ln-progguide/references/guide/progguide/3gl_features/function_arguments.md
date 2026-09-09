# Function arguments
The arguments of a function are the variables declared in the function header. Arguments can be accessed only within the function.

## Declaration, initialization, and scope
| | |
|---|---|
| Point of declaration | In the function between the brackets { }. |
| Syntax of declaration | [ref|reference] <type> name Note that array subscripts must be empty for reference arguments. |
| Initialization | At function call. For value arguments (see below), the values of the function call are copied. For reference arguments, the same variable (or the same memory area) is used as occupied by the variable submitted to the function call. |
| Scope (validity and time) | Only during function execution. |

## Value arguments
A value argument gets its value at the time of the function call and has its own memory space. For example:
```

FUNCTION long dupl(long val)        | val is a value argument
{
        RETURN( val * 2 )
}
FUNCTION MAIN()
{
        message("%d", dupl(10))
                | the argument val gets value 10
}
```

## Reference arguments
Reference arguments must be declared in the function header with the keyword REFERENCE or REF.
In the function call a variable (or indexed array variable) must be supplied for each reference argument in the function header. Such a variable must not be declared as CONST.
A reference argument has the same memory space as the variable used in the function call. Consequently, all changes made to a reference argument within the function block are also accessible after the function call in the variable used in the function call.
If the declaration of a reference argument has array subscripts, these must be empty as the contents and size of the call variable are used. If strings or large arrays are used, it is preferable to use reference arguments rather than returning them with the return statement. This avoids copy actions.

## Example 1
Note that in this example, the array subscript in the declaration of the reference argument is empty.
```

FUNCTION LONG read_line( REF STRING buffer() )
{
        IF ... THEN
                buffer = ...
                RETURN( 1 )
        ELSE
                buffer = ""
                RETURN( 0 )
        ENDIF
}

FUNCTION MAIN()
{
        STRING line(100)
        IF read_line(line) THEN
                ...
        ELSE
                message("No present line")
        ENDIF
        ...
}
```

## Example 2
This example uses a multi-dimensional array:
```

FUNCTION VOID fill_array ( REF LONG array(,) )
{
        array(1,1) = 10
        array(1,2) = 20
        ...
}

FUNCTION MAIN()
{
        STRING  a(5,10)
        fill_array(a)
}
```

## Constant arguments
Constant arguments must be declared with the keyword CONST in the function header. These are similar to reference arguments in that the same memory space is used for the constant argument and the value used in the function call. However, with constant arguments, it is possible to use any value within the function call. The value of the argument after the function call is not returned in the calling function.
In the body of a function it is not allowed to modify any of the function's constant arguments. E.g. it is not allowed to use a constant function argument as the left hand side of an [assignment](assignment_operator.md). Also, it is not allowed to use a constant function argument as the call variable for a reference argument in another function call.
The array subscript in the declaration of the constant argument must be empty because the size of the function call value is used. For example:
```

FUNCTION print_mess( CONST STRING mesg )
{
        IF NOT isspace(mesg) THEN
                message("Message: " & mesg)
        ENDIF
}

FUNCTION MAIN()
{
        ...
        print_mess("This is a message")
        ...
}
```

## Varying number of arguments
It is possible to pass an (as yet) unspecified number of arguments to a function definition by replacing the actual arguments with '...'. The function call must contain the actual arguments required to execute the function. This enables you to use different arguments (from 0 to approximately 250) each time you call the function. This feature is useful, for example, if you wish to change some (not all) of the flags of a process, and you do not know beforehand precisely which flags you are going to change. See the [Functions with variable number of arguments: synopsis](../functions_varying_arguments/synopsis.md) functions for information on using this feature.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Functions](functions.md)
