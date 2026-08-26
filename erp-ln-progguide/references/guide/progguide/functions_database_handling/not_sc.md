# NOT boolean operator
The NOT boolean operator evaluates to True if the search condition evaluates to Unknown or False.

## Syntax
```

<not boolean operator>
    ::= NOT Search condition
```

## Semantics
The truth table below shows the semantics of the NOT boolean operator.
| | | | |
|---|---|---|---|
| NOT | True | Unknown | False |
|  | False | Unknown | True |

## Examples
The following search condition evaluates to True if *firstnme* is anything but 'CHRISTINE'. If *firstnme* is NULL it evaluates to Unknown.
```

NOT ( firstnme = 'CHRISTINE' )
```
The following search condition evaluates to True if there is no employee with a salary larger than 50000.
```

NOT EXISTS( select * from dbtst120 where salary > 50000 )
```

## Related topics
- [AND boolean operator](and_sc.md)
- [OR boolean operator](or_sc.md)
- [Infor Enterprise Server SQL](baan_sql.md)
