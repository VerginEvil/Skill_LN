# SELECT statement
A SELECT statement retrieves a row set (or derived table) from the database. The row set can be built up from multiple (database) tables. Rows can be filtered, grouped and ordered. Multiple row sets can be combined into one row set using the UNION operator.

## Syntax
```

<select statement>
    ::= Query expression
                 [ Query hints overview ... ]
        [ ORDER BY clause
          [ WITH RETRY [REPEAT LAST ROW] ] ]
        [ SET specification ]
        [ Query hints overview ... ]
```

## Informal syntax
```

         SELECT clause <select list>
FROM clause <from list>
[ WHERE clause Search condition ]
[ GROUP BY clause <group list>
  [ HAVING clause Search condition ] ]
[ Query hints overview ... ]
[ UNION operator 
SELECT clause <select list>
FROM clause <from list>
  [ WHERE clause Search condition ]
  [ GROUP BY clause <group list>
    [ HAVING clause Search condition ] ]
  [ Query hints overview ... ]
] ...
[ ORDER BY clause <order by list> [ WITH RETRY [REPEAT LAST ROW] ]]
[ SET specification ]
[ Query hints overview ... ]
```
For full details of any of the above clauses of the SELECT statement, simply click on the relevant clause.

## Examples
The following SELECT statement selects all rows from table `dbtst120` (employees) and orders them by descending salary:
```

SELECT *
FROM   dbtst120
ORDER  BY salary DESC
```
The following SELECT statement selects the maximum sum of salary and bonus of all employees that have an education level less than 15:
```

SELECT max( salary + bonus )
FROM   dbtst120
WHERE  edlevel < 15
```
The following SELECT statement selects for each education level the salary and first name of the employee that has the maximum salary of all employees with that education level:
```

SELECT max_salary_by_edlevel.edlevel, salary, firstnme
FROM ( SELECT edlevel, MAX( salary ) AS max_salary
       FROM dbtst120
       GROUP BY edlevel ) max_salary_by_edlevel
     INNER JOIN
       dbtst120 AS employees
     ON max_salary_by_edlevel.max_salary = employees.salary
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
