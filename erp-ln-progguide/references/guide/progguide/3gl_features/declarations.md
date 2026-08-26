# Declarations
You can declare variables either within a function block or at the start of the program. Variables declared in a function block can be used within that function block only. Variables declared at the start of the program can be used in each function described below the declaration.

## General syntax
You declare variables with the following syntax. The parts between square brackets [ ] are optional.
```

declaration:    [ <specials> ] <type> <variables>

specials:       <special> [ <specials> ]            | List of <special> items.

special:        EXTERN                              | Not in function blocks.
                STATIC                              | Only for local variables in a function block.
                CONST                               | Only for function arguments and for BASED variables.
                REF                                 | Only for function arguments.

type:           LONG
                DOUBLE
                BOOLEAN
                STRING
                TABLE
                DOMAIN <domain_name>                | <domain_name> is the name of a domain
                                                    | as defined in the data dictionary.

variables:      <variable> [ , <variables> ]        | Comma-separated list of <variable> items.

variable:       <name> [ ( <dimensions> ) ] [ <options> ]

dimensions:     <dimension> [ , <dimensions> ]      | Comma-separated list of <dimension> items.
                                                    | Only for strings and arrays.

options:        <option> [ <options> ]              | List of <option> items.

option:         BASED                               | Only for strings and arrays; not in function arguments.
                FIXED                               | Only for one-dimensional strings.
                MB                                  | Multibyte - only for strings.
```
The comma-separated variables in a declaration (each variable with its own name and optionally with its own dimensions and options) share the specified specials and type.
If a variable is to be accessed by its symbolic name from outside the program, it must be declared with the keyword EXTERN, so that the variable name is stored in the symbol table of the object.
You must declare a variable with the keyword EXTERN if that variable is used within other programs, within forms (field names and variables within expressions), or within the function [expr.compile()](../functions_expressions_runtime/expr.compile.md). If the functions [get.var()](../functions_variables_interprocess_transfer/get.var.md) and [put.var()](../functions_variables_interprocess_transfer/put.var.md) are used within the program, the variables in the other program must be declared as EXTERN.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Variables](variables.md)
