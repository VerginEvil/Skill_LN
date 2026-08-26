# Sub query
A sub query defines a row set within an SQL statement.

## Syntax
```

<sub query>
    ::= Query expression
```

## Syntactical restrictions
- *No select targets* The SELECT clause of a sub query shall not contain a select target.
- *Not FOR UPDATE* The SELECT clause or FROM clause of a sub query shall not contain the FOR UPDATE clause.

## Examples
*Example 1*: The following query calculates the maximum salary of all employees.
```

SELECT MAX( salary )
FROM dbtst120
```
*Example 2*: The following query calculates the average salary of all employees with the same education level as the 'current' employee. Because the sub query contains an outer column reference it is called a correlated subquery.
```

SELECT AVG( salary )
FROM dbtst120
WHERE edlevel = employee.edlevel
```

## Related topics
- [SELECT statement](select_statement.md)
- [Infor Enterprise Server SQL](baan_sql.md)
