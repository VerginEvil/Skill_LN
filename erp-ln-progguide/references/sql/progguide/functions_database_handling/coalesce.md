# COALESCE
The COALESCE expression results in the first non-NULL value amongst the arguments.

## Syntax
```

<coalesce function>
    ::= COALESCE ( Value expression [{,Value expression}...] )
```

## Semantics
The COALESCE expression evaluates the first *<value expression>* and if its value is not NULL then the result is its value. Otherwise, it evaluates the second *<value expression>* and if its value is not NULL then the result is the value of the second *<value expression>*. And so on. If every *<value expression>* evaluates to the NULL value, then the result is the NULL value.
The COALESCE expression is defined using the following equivalences:
```
COALESCE( a,b )     <=> CASE WHEN a IS NOT NULL THEN a ELSE b END
```
```
COALESCE( a,b,... ) <=> CASE WHEN a IS NOT NULL THEN a ELSE COALESCE( b,... ) END
```
See [CASE expression (searched)](searched_case.md) for the exact semantics.

## Examples
The following COALESCE expression results in the integer 1, because it is the first non-NULL value.
```

COALESCE( 1,2,3 )
```

## Related topics
- [CASE expression (searched)](searched_case.md)
- [Infor Enterprise Server SQL](baan_sql.md)
