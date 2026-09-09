# LIKE predicate
The LIKE predicate matches a value with a pattern.

## Syntax
```

<like predicate>
    ::= <value expression> [NOT] LIKE <string constant> [ ESCAPE <string constant> ]
```

## Syntactical restrictions
The type of the *<**value expression**>* shall be *string*.

## Semantics
If the value of the *<**value expression**>* is NULL, then the result of the LIKE predicate is Unknown.
The LIKE predicate evaluates to True if the *<**value expression**>* matches the *<**string contant**>* pattern. Within this *<**string contant**>*, the character *%* matches any string of zero or more characters. The character *_* matches any single character. A wildcard character will be treated as literal if preceded by the escape character as defined by the optional ESCAPE keyword.

## Examples
The following predicate evaluates to True if *firstnme* is 'CHRISTINE'. Note: no space-padding is applied! So, if *firstnme* is 'CHRISTINE␣' (where ␣ represents a space), the predicate evaluates to False.
```

firstnme LIKE 'CHRISTINE'
```
The following predicate evaluates to True if *firstnme* starts with an 'A'.
```

firstnme LIKE 'A%'
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
