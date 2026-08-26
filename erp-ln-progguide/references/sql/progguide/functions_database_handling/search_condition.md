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

    | <company_nr predicate>
```
```

<row value constructor>
    ::= <value expression>
      | { <value expression> [ { , <value expression> }... ] }
```

## Syntactical restrictions

## sub query
The sub query shall be of degree 1.

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
