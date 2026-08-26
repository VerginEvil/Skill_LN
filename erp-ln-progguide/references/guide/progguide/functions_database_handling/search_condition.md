# Search condition
The search condition is a condition (expression) that evaluates to True, Unknown or False. The condition is comparable with an expression in an ordinary programming language: it has constants, variables, relational operators and logical operators.
The search condition is used to restrict a row set to those rows that fulfill the search condition. A row fulfills a search condition if and only if, for that row, the search condition evaluates to True.

## Syntax
```

<search condition>
    ::= <search condition> AND <search condition>
    | <search condition> OR <search condition>
    | NOT <search condition>
    | ( <search condition> )
    | <comparison predicate>
    | <row value constructor> [NOT] BETWEEN <row value constructor> AND <row value constructor>
    | <row value constructor> [NOT] INRANGE <row value constructor> AND <row value constructor>
    | <value expression> IS NULL predicate
    | <like predicate>
    | <in predicate>
    | EXISTS ( <sub query> )
```
```

    | <refers to predicate>
    | <_compnr predicate>
```
```

<row value constructor>
    ::= <value expression>
      | { <value expression> [ { , <value expression> }... ] }
```

## Syntactical restrictions

## sub query
The sub query shall be of degree 1.

## _compnr predicate
If a search condition is of the form "SC1 OR SC2" or "NOT SC" then it shall not contain a _compnr predicate, unless there is an intervening subquery.
Examples of *incorrect* usage:
```

_compnr = 0 OR empno = 10
```
```

NOT ( _compnr = 0 AND empno = 10 )
```
Examples of correct usage. The second example shows that a _compnr predicate is used in a search condition of the form "SC1 OR SC2" but there is an intervening subquery. Within the search condition of the subquery the usage of the _compnr predicate is correct.
```

_compnr = 0 AND empno = 10
```
```

empno = 10 OR EXISTS (
    SELECT * FROM dbtst190 WHERE _compnr = 0 )
```

## REFERS TO predicate
If a search condition is of the form "SC1 OR SC2" or "NOT SC" then it shall not contain a REFERS TO predicate, unless there is an intervening subquery.
Examples of *incorrect* usage:
```

a.empno REFERS TO b.empno OR b.empno = 10
```
```

NOT ( a.empno REFERS TO b.empno )
```
Examples of correct usage. The second example shows that a REFERS TO predicate is used in a search condition of the form "SC1 OR SC2" but there is an intervening subquery.
```

_compnr = 0 AND a.empno REFERS TO b
```
```

empno = 10 OR EXISTS (
    SELECT * FROM dbtst190 a, dbtst120 b WHERE a.empno REFERS TO b )
```

## Examples
*Example 1*: The following search condition is True if edlevel is larger than 10 and hiredate is before January 16, 1999.
```

{ edlevel } > 10  AND  hiredate < DATE '1999-1-16'
```
*Example 2*: The following search condition is True if the employees salary is larger than 10000 and there does not exist another employee with a larger salary.
```

{ emp.salary > 10000 }
    AND NOT EXISTS( SELECT * FROM dbtst120 where salary > emp.salary )
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
