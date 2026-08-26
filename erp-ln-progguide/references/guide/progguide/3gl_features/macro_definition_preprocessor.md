# Macro definition (preprocessor)
Use the following statement to define a macro:
```

#define macroname[(arguments)]
```
Use the following statement to undefine a macro:
```

#undef macroname[(arguments)]
```

## Defining macros
The macro names in the source are expanded to the macro definition. If a macro definition does not fit on one line, it is possible to continue the definition on the next line(s) by using the caret symbol '^' at the beginning of each line. It is possible to use arguments in the macro. For example:
```

#define a(x, y, z)      for i = x to y
^                               z()
^                       endfor              | The definition

a(1, 100, func)                             | The invocation
```
Macro definitions with the same name but with different numbers of arguments are regarded as different. For example:
```

#define x              definition without arguments
#define x()            definition with 0 arguments
#define x(arg1)        definition with 1 argument
#define x(arg1,arg2)   definition with 2 arguments
#define x(...)         definition with at least one argument
```
Note that there is a difference between a macro without arguments and a macro with zero arguments. In the first case, you must use 'x' in the program script to call the macro. In the second case, you must use 'x()' to call the macro.

## Undefining macros
The '#undef' statement causes the macro definition to be ignored. The number of arguments in the '#undef' call must match the number of arguments in the definition. For example:
```

#define MAXLENGTH   1000
#define INCR        1
#define INCR(i)     i = i + INCR
...
#undef  MAXLENGTH
#define INCR        2       | Redefines INCR
...
#undef  INCR(i)
```
An error occurs if you apply #undef to an unknown macro. To be sure that the macro was defined, use the following construction:
```

#ifdef INCR                 | without arguments
        #undef INCR(i)
#endif
```
See [Conditional compilation (preprocessor)](conditional_compilation_preprocessor.md) for a detailed description of #ifdef and #endif calls.

## Variable macro arguments
You can use the ellipsis notation ( , ... ) to define the macro with a varying number of arguments. For example:
```

#define fillbuf(buf1, format, ...)  buf1 = sprintf$(format, ...)

| macro call
string buffer(100)
long l_val
double d_val

fillbuf(buffer, "%d. %s = %d %5.2f", 1, "Value", l_val, d_val)
```
The macro definition can contain a number of arguments, but the ellipsis notation must be the last argument.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Preprocessor](preprocessor.md)
