# Token pasting (preprocessor)
In the macro, you can enter a part of a variable as a macro argument. The symbol '##' is used to distinguish macro arguments and the rest of the macro. This is omitted in the macro call. You can paste more macro arguments together as one identifier. This principle is called token pasting. It is used to reuse parts of the source code, where using functions is impossible or difficult.

## Example 1
```

#define p(x)            message("%d", var##x)
#define q(x,y)          message("%d", x##y)
#define r(x,y,z)        message("%d", x##y##z)

long var1a, var1b
p(1a)                   | becomes: message("%d", var1a)
p(1b)                   | becomes: message("%d", var1b)
q(var, 1a)              | becomes: message("%d", var1a)
q(var, 1b)              | becomes: message("%d", var1b)
r(var, 1, a)            | becomes: message("%d", var1a)
r(var, 1, b)            | becomes: message("%d", var1b)
```

## Example 2
```

#define VRC(table,v,r,c)
^       tt##table##.vers = v
^       tt##table##.rele = r
^       tt##table##.cust = c

VRC(adv100, "6.2", "a", "")
VRC(adv200, "6.2", "a", "")
VRC(adv300, "6.2", "a", "")
```

## Related topics
- [3GL programming language features: overview](overview.md)
- [Preprocessor](preprocessor.md)
