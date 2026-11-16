# CASE expression (searched)
The searched CASE expression specifies a conditional value.

## Syntax
```

<searched case expression>
    ::= CASE
        { WHEN <search condition> THEN <result> }...
        [ ELSE <result> ]
        ENDCASE

<result>
    ::= <value expression>
      | NULL
```

## Semantics
The searched CASE expression evaluates the first *<**search condition**>* and if it evaluates to TRUE then the result is the value of the first *<**result**>*. Otherwise, the searched CASE expression evaluates the second *<**search condition**>* and if it evaluates to TRUE then the result is the value of the second *<**result**>*. And so on. If every *<**search condition**>* evaluates to FALSE or UNKNOWN, then the result is the value of the *<**result**>* specified in the ELSE clause. If the ELSE clause is missing then the result is the NULL value.
Instead of [SQL reserved word](sql_reserved_words.md) ENDCASE, also SQL reserved word END can be used to terminate the searched case expression. For porting sets with [TIV level](../tiv/tiv_overview.md) less than [2120](../tiv/tiv_2120.md), SQL reserved word END must be used and SQL reserved word ENDCASE cannot be used.

## Examples
The following searched CASE expression returns 'yes':
```

CASE WHEN 1 < 2 THEN 'yes' ENDCASE
```
The following searched CASE expression results in 'Male' if the column `sex` equals `dbsex.male`; it results in 'Female' if column `sex` equals `dbsex.female`; otherwise it results in the NULL value.
```

CASE
WHEN sex = dbsex.male THEN 'Male'
WHEN sex = dbsex.female THEN 'Female'
ENDCASE
```

## Related topics
- [CASE expression (simple)](simple_case.md)

- [Infor Enterprise Server SQL](baan_sql.md)
