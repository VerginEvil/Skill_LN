# Conditional compilation (preprocessor)

## Directives
The preprocessor provides the following directives to enable you to compile parts of the source depending on certain conditions:
```

#if <constant expression>
...
#else
#if <constant expression>
...
#else
...
#endif
#endif
This is equivalent to the following:
#if <constant expression>
...
#elif <constant expression>
...
#else
...
#endif
```
| | |
|---|---|
| `#ifdef <macro>` | The source after #ifdef up to #else/#elif/#endif is compiled if <macro> is defined. Otherwise this source is ignored.  |
| `#ifndef <macro>` | The source after #ifndef up to #else/#elif/#endif is compiled if <macro> is not defined. Otherwise this source is ignored.  |
| `#if <constant expression>` |  The source after #if up to #else/#elif/#endif is compiled if <constant expression> evaluates to TRUE. Otherwise this source is ignored. The <constant expression> is in fact a runtime expression with the same features as described for the function [expr.compile()](../functions_expressions_runtime/expr.compile.md). Variable names in the expression refer to macro definitions. Variable names for which no macro definition exists, evaluate to 0. If the macro substitution text is the string "0" or can be implicitly converted to a non-zero integer value, then the variable is evaluated to the indicated integer value. Assignment expressions are not allowed.  |
| `#else` | If the condition belonging to #if/#ifdef/#ifndef/#elif is FALSE, the source after #else up to #endif is compiled. If the condition belonging to #if/#ifdef/#ifndef/#elif is TRUE, the source after #else up to #endif is ignored.  |
| `#elif <constant expression>` |  '#elif' is a combination of #else and #if. For example:  |
| `#endif` | To finish a part of the source started with #ifdef/#ifndef/#if.  |
| `#undef <macro>` | To delete a macro definition. The macro is not known on the next #ifdef call.  |
Notes on using the directives
- It is possible to use nested #if structures.
- It is possible to define a macro when starting the compiler. You use the D option to do this. For example:
```

bic6.2 -D<macro>                  | no value means default 1
bic6.2 -D<macro>=<value>
bic6.2 -D<macro>='any token string'
```
- These macros can also be used in the #if conditions. For example:
```

bic6.2 -DDEBUG -DMYTEST <source>

|source
#if DEBUG and MYTEST
        message("Some debug information")
        ...
#endif

bic6.2 -DCUSTOMER_X -DCUSTOMER_Y <source>
bic6.2 -DSTANDARD <source>

#if STANDARD
        ...
#elif ( CUSTOMER_X and (not CUSTOMER_Y) )
        ...
#endif
```
- You can use #ifdef to make a part of the file inactive. For example: Example:
```

#ifdef OLD
        ...
        ...
        ...
#endif
```
- The preprocessor works only during compilation of a 3GL source, as the standard generator std_gen6.2 does not have a preprocessor pass. So it is not possible to use 4GL events in #if, #ifdef or #ifndef.
- It is not possible to use a #ifdef statement within an embedded SQL query. So, the following construction is not allowed:
```

select  *
#ifdef STANDARD
        ...
        from x
#else
        ...
        from y
#endif
        where ...
selectdo
        ...
endselect
```
But the following construction is possible:
```

#ifdef STANDARD
        select * from x where ...
        selectdo
                ...
        endselect
#else
        select * from y where ...
        selectdo
                ...
        endselect
#endif
```
- The following keywords provide debug information in 3GL sources:
```

__FILE__         : contains the name of the current source
__LINE__         : contains the line number of the current source
__FUNCTION__     : contains the lower case name of the current function
__FUNCTION_CP__  : contains the name of the current function; the case is preserved
__OBJECT__       : contains the name of the current object
```
For example:
```

message("This is at line %d in the source %s", __LINE__, __FILE__)
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Preprocessor](preprocessor.md)
