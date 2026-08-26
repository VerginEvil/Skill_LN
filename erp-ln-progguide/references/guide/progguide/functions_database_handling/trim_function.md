# TRIM function
With the TRIM function you can remove trailing and/or leading characters from a string.

## Syntax
```

<trim function>
    ::= TRIM ( [ [<trim specification>] [<trim character>] FROM ] <trim source> )

<trim source>
    ::= Value expression

<trim character>
    ::= Value expression

<trim specification>
    ::= LEADING | TRAILING | BOTH
```

## Syntactical restrictions
The type of the *<trim source>* and the *<trim character>* shall be *string*. The length of *<trim character>* shall be 1.

## Semantics
If the value of the *<trim source>* is NULL, then the result of the TRIM function is also NULL.
The data type of the result of the TRIM function is *string*.
If *<trim character>* is omitted then the implicit trim character is a space (' '). If *<trim specification>* is omitted then the implicit trim specification is BOTH.

## Examples
The following TRIM function returns the string `'abc'`.
```

TRIM( ' abc    ' )
```
The following TRIM function returns the string `' abc'`.
```

TRIM( TRAILING FROM ' abc    ' )
```
The following TRIM function returns the string `' ab'`.
```

TRIM( 'c' FROM TRIM( TRAILING FROM ' abc    ' ) )
```

## Related topics
- [Value expression](value_expression.md)
- [Infor Enterprise Server SQL](baan_sql.md)
