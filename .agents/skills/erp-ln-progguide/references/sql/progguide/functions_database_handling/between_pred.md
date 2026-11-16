# BETWEEN predicate
The BETWEEN predicate evaluates to True if the value of the first expression lies between the values of the second expression and the third expression.

## Syntax
```

<between predicate>
    ::= <row value constructor> [NOT] BETWEEN <row value constructor> AND <row value constructor>
```

## Syntactical restrictions
No *<**row value constructor**>* shall contain a reference to an array column.

## Semantics
The following equivalences hold.
```

expr NOT BETWEEN lower AND upper  ⟺  NOT ( expr BETWEEN lower AND upper )

expr BETWEEN lower AND upper  ⟺  lower <= expr AND expr <= upper
```
For the exact semantics see the pages about [the comparison operators](comparison_pred.md), [the NOT operator](not_sc.md) and [the AND operator](and_sc.md).

## Examples
The following predicate evaluates to True if *empno* is in the interval [10..20]. It evaluates to Unknown if *empno* is NULL. Otherwise, it evaluates to False.
```

empno BETWEEN 10 AND 20
```
The following predicate evaluates to True if *salary* is in the interval [20000.00.. 50000.00].
```

{ salary } BETWEEN 20000.00 AND 50000.00
```
The following predicate evaluates to True if *lastname* lies between 'HAAS' and 'LUCCHESSI', but if *lastname* equals 'HAAS' then *firstnme* must be larger than or equal to 'CHRISTINE'.
```

{ lastname, firstnme } BETWEEN { 'HAAS', 'CHRISTINE' } and { 'LUCCHESSI' }
```

## Related topics
- [INRANGE predicate](inrange_pred.md)

- [Infor Enterprise Server SQL](baan_sql.md)
