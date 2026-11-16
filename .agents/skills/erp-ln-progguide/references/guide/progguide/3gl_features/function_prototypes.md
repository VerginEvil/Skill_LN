# Function prototypes
A function consists of three parts:

- Function prototype

- Function definition (function block)

- Function call

The function prototype must be exactly the same as the function header in the function definition. The prototype of a function is not always necessary. For example, it is not necessary in the following situations:

- if the function is of type void and has no arguments

- if the definition of the function occurs before any call of that function

In all other situations the prototype of the function must occur before the function call. For example:
```

prototype
        FUNCTION LONG compnr_check( LONG new_compnr )

function call
        IF compnr_check( 999 ) THEN
                . . . .
        ELSE
                mess("pcgen00016", 999)
                    | Comp. number %d not present
        ENDIF

definition
        FUNCTION LONG compnr_check( LONG new_compnr )
        {
                TABLE tpctst999

                SELECT pctst999.*
                FROM pctst999
                WHERE pctst999.compnr = :new_compnr
                ORDER BY pctst999.compnr
                SELECTDO
                        compnr = pctst999.compnr
                SELECTEMPTY
                        RETURN(FALSE)
                ENDSELECT
                RETURN(TRUE)
        }
```
From compiler version bic6.1 onwards, it is not necessary to use function prototypes within the same source as the function definition.

## Related topics
- [3GL programming language features: overview](overview.md)

- [Functions](functions.md)
