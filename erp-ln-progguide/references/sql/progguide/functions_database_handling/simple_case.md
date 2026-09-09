# CASE expression (simple)
The simple CASE expression specifies a conditional value.

## Syntax
```

<simple case expression>
    ::= CASE <case operand>
        { WHEN <value expression> THEN <result> }...
        [ ELSE <result> ]
        END

<case operand>
    ::= <value expression>

<result>
    ::= <value expression>
      | NULL
```

## Semantics
The simple CASE expression evaluates the *<**case operand**>*. If the value of the *<**case operand**>* equals the value of the first *<**value expression**>* then the result is the value of the first *<**result**>*. Otherwise, if the value of the *<**case operand**>* equals the value of the second *<**value expression**>* then the result is the value of the second *<**result**>*. And so on. If the value of every *<**value expression**>* does not equal the value of the *<**case operand**>*, then the result is the value of the *<**result**>* specified in the ELSE clause. If the ELSE clause is missing then the result is the NULL value.
The simple CASE expression is defined using the following equivalence:
```

      CASE a                                      CASE
      WHEN v1 THEN r1                             WHEN a = v1 THEN r1
      WHEN v2 THEN r2                             WHEN a = v2 THEN r2
      ...                         ⟺              ...
      WHEN vn THEN rn                             WHEN a = vn THEN rn
      ELSE e                                      ELSE e
      END                                         END
```
See [CASE expression (searched)](searched_case.md) for the exact semantics.

## Examples
The following simple CASE expression returns 'yes':
```

CASE 1 WHEN 1 THEN 'yes' END
```
The following simple CASE expression results in 'Male' if the column `sex` equals `dbsex.male`; it results in 'Female' if column `sex` equals `dbsex.female`; otherwise it results in the NULL value.
```

CASE sex
WHEN dbsex.male THEN 'Male'
WHEN dbsex.female THEN 'Female'
END
```

## Related topics
- [COALESCE](coalesce.md)

- [CASE expression (searched)](searched_case.md)

- [Infor Enterprise Server SQL](baan_sql.md)
