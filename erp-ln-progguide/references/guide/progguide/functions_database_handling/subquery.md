# Subquery
A subquery defines a row set within an SQL statement.

## Syntax
```

<subquery>
    ::= <query expression>
```

## Syntactical restrictions
- *No select targets* The SELECT clause of a subquery shall not contain a select target.

- *Not FOR UPDATE* The SELECT clause or FROM clause of a subquery shall not contain the FOR UPDATE clause.

## Examples
*Example 1*: The following query calculates the maximum salary of all employees.
```

SELECT MAX( salary )
FROM dbtst120
```
*Example 2*: The following query calculates the average salary of all employees with the same education level as the 'current' employee. Because the subquery contains an [outer column reference](sql_glossary.md#OuterColumnReference) it is called a [correlated subquery](sql_glossary.md#CorrelatedSubquery).
```

SELECT AVG( salary )
FROM dbtst120
WHERE edlevel = employee.edlevel
```

## Related topics
- [SELECT statement](select_statement.md)

- [Infor Enterprise Server SQL](baan_sql.md)
