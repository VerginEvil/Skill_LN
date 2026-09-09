# Search condition
The search condition is a condition (expression) that evaluates to True, Unknown or False. The condition is comparable with an expression in an ordinary programming language: it has constants, variables, relational operators and logical operators.
The search condition is used to restrict a row set to those rows that fulfill the search condition. A row fulfills a search condition if and only if, for that row, the search condition evaluates to True.

## Syntax
```

<search condition>
    ::= <comparison predicate>
      | <between predicate>
      | <inrange predicate>
      | <is null predicate>
      | <like predicate>
      | <in predicate>
      | <exists predicate>
      | <company_nr predicate>
      | <search condition> AND <search condition>
      | <search condition> OR <search condition>
      | NOT <search condition>
      | ( <search condition> )
```

## Examples
*Example 1*: The following search condition is True if edlevel is larger than 10 and hiredate is before January 16, 1999.
```

{ edlevel } > 10  AND  hiredate < DATE '1999-1-16'
```
*Example 2*: The following search condition is True if the employees salary is larger than 10000 and there does not exist another employee with a larger salary.
```

{ emp.salary > 10000 } AND NOT EXISTS( SELECT * FROM dbtst120 WHERE salary > emp.salary )
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
