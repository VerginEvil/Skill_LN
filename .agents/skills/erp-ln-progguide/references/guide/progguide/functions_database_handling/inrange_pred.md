# INRANGE predicate
The INRANGE predicate evaluates to True if the *individual* value expressions of the first row value constructor lie between the *individual* value expression of the second and the third value expression.

## Syntax
```

<inrange predicate>
    ::= <row value constructor> [NOT] INRANGE <row value constructor> AND <row value constructor>
```

## Syntactical restrictions
No *<**row value constructor**>* shall contain a reference to an array column.

## Semantics
The following equivalences hold.
```

expr NOT INRANGE lower AND upper  ⟺  NOT ( expr INRANGE lower AND upper )

expr INRANGE lower AND upper  ⟺  lower #<= expr AND expr #<= upper
```
For the exact semantics see the pages about [the comparison operators](comparison_pred.md), [the NOT operator](not_sc.md) and [the AND operator](and_sc.md).

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
