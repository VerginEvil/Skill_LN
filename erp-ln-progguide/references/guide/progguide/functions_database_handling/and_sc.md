# AND boolean operator
The AND boolean operator evaluates to True if both left and right search conditions evaluate to True.

## Syntax
```

<and boolean operator>
    ::= Search condition AND Search condition
```

## Semantics
The truth table below shows the semantics of the AND boolean operator.
| | | | |
|---|---|---|---|
| AND | True | Unknown | False |
| True | True | Unknown | False |
| Unknown | Unknown | Unknown | False |
| False | False | False | False |

## Examples
The following search condition evaluates to True if both *salary* is larger than 20000 and *bonus* is larger than 1000.
```

salary > 20000 AND bonus > 1000
```

## Related topics
- [OR boolean operator](or_sc.md)
- [NOT boolean operator](not_sc.md)
- [Infor Enterprise Server SQL](baan_sql.md)
