# CASE expression (searched)
The searched CASE expression specifies a conditional value.

## Syntax
```

<searched case expression>
    ::= CASE
             WHEN Search condition THEN <result>
             [{ WHEN Search condition THEN <result> }...]
             [ ELSE <result> ]
        END

<result>
    ::= Value expression
      | NULL
```

## Semantics
The searched CASE expression evaluates the first *<search condition>* and if it evaluates to TRUE then the result is the value of the first *<result>*. Otherwise, the searched CASE expression evaluates the second *<search condition>* and if it evaluates to TRUE then the result is the value of the second *<result>*. And so on. If every *<search condition>* evaluates to FALSE or UNKNOWN, then the result is the value of the *<result>* specified in the ELSE clause. If the ELSE clause is missing then the result is the NULL value.

## Examples
The following searched CASE expression returns 'yes':
```

CASE WHEN 2>1 THEN 'yes' END
```
The following searched CASE expression results in 'Male' if the column `sex` equals `dbsex.male`; it results in 'Female' if column `sex` equals `dbsex.female`; otherwise it results in the NULL value.
```

CASE
	WHEN sex = dbsex.male THEN 'Male'
	WHEN sex = dbsex.female THEN 'Female'
END
```

## Related topics
- [COALESCE](coalesce.md)
- [CASE expression (simple)](simple_case.md)
- [Infor Enterprise Server SQL](baan_sql.md)
