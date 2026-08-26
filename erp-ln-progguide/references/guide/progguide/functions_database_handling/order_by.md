# ORDER BY clause
The ORDER BY clause specifies a table that is ordered by the columns that are specified by the ORDER BY clause. The input table is the table specified by the [SELECT clause](select.md).
ORDER BY sorts the result-set by one or more columns (where sort direction defines ascending or descending order).
ORDER BY is applied after [GROUP BY clause](group_by.md), so it operates on an aggregated set and not on the individual rows.

## Syntax
```

<order by clause>
    ::= ORDER BY <order by item> { , <order by item> }...
                 [ WITH RETRY clause [ REPEAT LAST ROW ] ]

<order by item>
    ::= Column reference [ <sort direction> ]
      | <unsigned integer> [ <sort direction> ]

<unsigned integer>
    ::= Integer constant

<sort direction>
    ::= ASC
      | DESC
```

## Syntactical restrictions
The *<unsigned integer>* shall not start with a minus sign ('–').
The *<column reference>* shall not reference an array column.
In case of a composed query, the *<column reference>* contains the mnemonic, do not include the table name.

## Semantics
If *<sort direction>* is ommited, then *ASC* is implicit.
The result table is first ordered on the first *<order by item>*. If there is a second *<order by item>*, then whenever the values for the first *<order by item>* are the same or are both NULL, then the second *<order by item>* determines the order. And so on.
If for all *<order by item>s* the corresponding column values of two rows are the same or both NULL, then the order of the rows is undefined.
It is implementation defined whether NULL values sort before or after any other value.
Specifying the *WITH RETRY* keywords does not have an impact on the working of the ORDER BY clause. It modifies the result table of the WHERE clause after a jump to a db.retry.point(). See section [WITH RETRY clause](with_retry.md).

## Examples
The following example selects the columns *lastname*, *salary* and *bonus* from table *dbtst120*. The result table is ordered first on column *salary* and then on column *bonus*.
```

SELECT lastname, salary, bonus
FROM dbtst120
ORDER BY salary DESC, bonus DESC
```
The following example groups table *dbtst120* on column *edlevel*, then selects column *edlevel* and the average of column *salary*. The result table is ordered on the average of column *salary*.
```

SELECT edlevel, AVG( salary )
FROM dbtst120
GROUP BY edlevel
ORDER BY 2
```
The following statement produces a list of employees, which is then arranged in groups of employees belonging to the same department. The result-set is collapsed into records that represent departments.
For each group (i.e department) the average salary is calculated (stored in AVG). The result is then ordered using the average salary (which produces a sorted list of departments).
```

SELECT DEPARTMENT, AVG(SALARY) AS AVG
FROM EMPLOYEE
GROUP BY DEPARTMENT
ORDER BY AVG
```

## Related topics
- [SELECT clause](select.md)
- [WITH RETRY clause](with_retry.md)
- [Infor Enterprise Server SQL](baan_sql.md)
