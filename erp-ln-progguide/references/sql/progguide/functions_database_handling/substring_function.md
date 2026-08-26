# SUBSTRING function
The SUBSTRING function returns a portion of a string argument.

## Syntax
```

<substring function>
    ::= SUBSTRING ( <substring source> FROM <start position> [ FOR <string length> ] )

<substring source>
    ::= Value expression

<start position>
    ::= Value expression

<string length>
    ::= Value expression
```

## Syntactical restrictions
The type of *<substring source>* shall be *string*. The type of *<start position>* and *<string length>* shall be *integer*.

## Semantics
If the value of the *<substring source>* is NULL, then the result of the SUBSTRING function is also NULL.
The data type of the result of the SUBSTRING function is *string*.
The value of the SUBSTRING function is the string that starts at position *<start position>* and is *<string length>* characters long. A *<start position>* with value 1 will return a string starting at the first character of *<substring source>*.
If *<string length>* is omitted then the value of the SUBSTRING function is the entire string from position *<start position>* onwards.

## Examples
The following SUBSTRING function returns the string `'cd'`.
```

SUBSTRING( 'abcdef' FROM 3 FOR 2 )
```
The following SUBSTRING function returns the string `'cdef'`.
```

SUBSTRING( 'abcdef' FROM 3 )
```
The following SUBSTRING function returns the string `'abcdef'`.
```

SUBSTRING( 'abcdef' FROM 1 )
```

## Related topics
- [Value expression](value_expression.md)
- [Infor Enterprise Server SQL](baan_sql.md)
