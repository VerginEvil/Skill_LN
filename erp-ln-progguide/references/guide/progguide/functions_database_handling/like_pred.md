# LIKE predicate
The LIKE predicate matches a value with a pattern.
Infor Enterprise Server SQL has two like keywords: LIKE and ALIKE.
The handling of the LIKE keywords depends on the optional *mode* argument of the [sql.parse()](../functions_dynamic_sql_queries/sql.parse.md) function. With the *PARSE.ANSI* flag set, the LIKE keyword is a synonym of the ALIKE keyword.
If this flag is not set, the LIKE predicate evaluates to True if the *value expression* matches the *string* pattern. The matching is based on *Regular Expressions*.

## Syntax
```

<like predicate>
    ::= <ansi-like predicate> | <regexp-like predicate>

<ansi-like predicate>
    ::= Value expression [NOT] ALIKE String constant
            [ESCAPE String constant]

<regexp-like predicate>
    ::= Value expression [NOT] LIKE String constant
```

## Syntactical restrictions
The ALIKE keyword generates a [42I82 - Syntax conflicts with Parse mode](../sql_states_and_messages/42I82.md) when the *PARSE.ANSI* flag is set in the optional *mode* argument of the [sql.parse()](../functions_dynamic_sql_queries/sql.parse.md) function.
The type of the *<value expression>* shall be *string*.

## Semantics
If the value of the *<value expression>* is NULL, then the result of the LIKE predicate is Unknown.
The result of the LIKE predicate (non ansi mode) is equivalent with the following expression using [expr.compile()](../functions_expressions_runtime/expr.compile.md) and using the value of the *value expression* for the optional argument to [l.expr()](../functions_expressions_runtime/l.expr.md).
```

      $$ IN "<string constant>"
```
The ALIKE predicate evaluates to True if the *<value expression>* matches the *<string contant>* pattern. Within this *<string contant>*, the character *%* matches any string of zero or more characters. The character *_* matches any single character. A wildcard character will be treated as literal if preceded by the escape character as defined by the optional ESCAPE keyword.

## Examples
The following predicate evaluates to True if *firstnme* is 'CHRISTINE'. Note: no space-padding is applied! So, if *firstnme* is 'CHRISTINE␣' (where ␣ represents a space), the predicate evaluates to False.
```

firstnme LIKE 'CHRISTINE'
```
The following predicate evaluates to True if *firstnme* starts with an 'A'.
```

firstnme LIKE 'A.*' AND firstnme ALIKE 'A%'
```
The following predicate evaluates to True if *firstnme* starts with a 'C' or an 'H'.
```

firstnme LIKE '[CH].*'
```
The following predicate evaluates to True if *firstnme* does not start with an 'I'.
```

firstnme LIKE '[^I].*'
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
