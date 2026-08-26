# IS NULL predicate
The IS NULL predicate evaluates to True if the value expression evaluates to NULL.

## Syntax
```

<is null predicate>
    ::= Value expression IS [NOT] NULL
      | Column reference IS [NOT] NULL
```

## Semantics
If the *<value expression>* is NULL, then the result of the IS NULL predicate is True and the result of the IS NOT NULL predicate is False. Otherwise, the result of the IS NULL predicate is False and the result of the IS NOT NULL predicate is True.
An array value is never NULL. So, the expression "phoneno IS NULL" always evaluates to False, because the column *phoneno* is an array column. The individual values of an array value may be NULL. So, the expression "phoneno(1) IS NULL" can evaluate to False or True.

## Examples
The following predicate evaluates to True if *firstnme* is NULL. Otherwise, it evaluates to False.
```

firstnme IS NULL
```
The following predicate evaluates to True if *firstnme* is NULL. Otherwise, it evaluates to False.
```

firstnme & 'abc' IS NULL
```
The following predicate evaluates to True if both *salary* and *bonus* are NOT NULL.
```

salary + bonus IS NOT NULL
```
The above predicate is equivalent with the following predicate.
```

salary IS NOT NULL  AND  bonus IS NOT NULL
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
