# UPPER LOWER function
With the UPPER and LOWER functions you can convert string expressions to upper and lower case.

## Syntax
```

<upper lower function>
    ::= UPPER ( Value expression )
      | LOWER ( Value expression )
```

## Syntactical restrictions
The type of *<value expression>* shall be *string*.

## Semantics
If the *<value expression>* is NULL, then the result of the UPPER and LOWER functions is also NULL.
The data type of the result of the UPPER and LOWER functions is a string.
Note  Note: folding extended ASCII characters may give unexpected results. In particular converting the β (scharf-s, iso88591 code point 0xdf) to upper case, leaves the character as it is (while Unicode specifies that it should be replaced by “SS”). Converting the ÿ (iso88591 code point 0xff) to upper case on Microsoft SQL server results in Ÿ (code point 0x9f), but in iso88591 this character is unused.

## Examples
The following UPPER function returns the *lastname* string value in upper case characters.
```

UPPER ( lastname )
```
The following LOWER function returns the string `'abc'`.
```

LOWER ( 'ABC' )
```

## Related topics
- [Value expression](value_expression.md)
- [Infor Enterprise Server SQL](baan_sql.md)
