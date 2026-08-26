# INRANGE predicate
The INRANGE predicate evaluates to True if the *individual* value expressions of the first row value constructor lie between the *individual* value expression of the second and the third value expression.

## Syntax
```

<inrange predicate>
    ::= Row value constructor [NOT] INRANGE
           Row value constructor AND Row value constructor
```

## Syntactical restrictions
No *<row value constructor>* shall contain a reference to an array column.

## Semantics
The following equivalences hold:
```

      expr NOT INRANGE lower AND upper  <=>  NOT ( expr INRANGE upper AND lower )
```
```

      expr INRANGE lower AND upper  <=>  expr #>= lower AND expr #<= upper
```
For the exact semantics see [Comparison predicate](comparison_pred.md), [NOT boolean operator](not_sc.md) and [AND boolean operator](and_sc.md).

## Examples
The following predicate evaluates to True if *edlevel* lies in the range [10..18].
```

edlevel INRANGE 10 AND 18
```
The following predicate evaluates to True if *salary* lies in the range [20000.00..50000.00] and *bonus* is larger than 1000.00.
```

{ salary, bonus } INRANGE { 20000.00, 1000.00 } AND { 50000.00 }
```

## Related topics
- [BETWEEN predicate](between_pred.md)
- [Infor Enterprise Server SQL](baan_sql.md)
