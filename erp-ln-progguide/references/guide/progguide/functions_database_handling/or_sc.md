# OR boolean operator
The OR boolean operator evaluates to True if the left or the right search condition evaluates to True.

## Syntax
```

<or boolean operator>
    ::= <search condition> OR <search condition>
```

## Semantics
The truth table below shows the semantics of the OR boolean operator.
| | | | |
|---|---|---|---|
| OR | True | Unknown | False |
| True | True | True | True |
| Unknown | True | Unknown | Unknown |
| False | True | Unknown | False |

## Examples
The following search condition evaluates to True if *salary* is larger than 20000 or *bonus* is larger than 1000.
```

salary > 20000 OR bonus > 1000
```

## Related topics
- [AND boolean operator](and_sc.md)

- [NOT boolean operator](not_sc.md)

- [Infor Enterprise Server SQL](baan_sql.md)
