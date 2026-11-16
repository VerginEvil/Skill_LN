# GROUP BY clause
The GROUP BY clause specifies a [grouped table](sql_glossary.md#GroupedTable). It operates on the table that is specified by the FROM clause and possibly the WHERE clause of the SELECT statement.
GROUP BY takes the result-set and arranges its rows into groups using one or more columns that have duplicate values. Typically used in conjunction with aggregate functions (MIN, MAX, AVG, etc).

## Syntax
```

<group by clause>
    ::= GROUP BY <column reference> [ { , <column reference> }... ]
```

## Semantics
The columns of the grouped table have the same names and descriptors as the table the GROUP BY clause operates on.
For any two rows of the input table, if the values on the grouping columns are identical or both NULL, then the rows are in the same group of the grouped table. Otherwise, they are in different groups.

## Examples
In the following example, the GROUP BY clause groups the rows of table *dbtst120* that satisfy the condition *sex = dbsex.female* by the column *edlevel*.
```

SELECT edlevel, MIN( salary ), MAX( salary )
FROM dbtst120
WHERE sex = dbsex.female
GROUP BY edlevel
```
The result of applying the GROUP BY clause is the following grouped table. Column *edlevel* is a (the) grouping column of the grouped table.
```

edlevel    salary            firstnme            ...
-------------------------------------------------------------
12         15900.00000000000 MAUDE
-------------------------------------------------------------
15         27380.00000000000 MARIA
-------------------------------------------------------------
16         36170.00000000000 EVA
16         29750.00000000000 EILEEN
16         23800.00000000000 DOLORES
16         17250.00000000000 SYBIL
-------------------------------------------------------------
17         22250.00000000000 ELIZABETH
17         21340.00000000000 MARILYN
17         26250.00000000000 ETHEL
-------------------------------------------------------------
18         52750.00000000000 CHRISTINE
18         28420.00000000000 HEATHER
18         29840.00000000000 JENNIFER
-------------------------------------------------------------
20         38250.00000000000 SALLY
-------------------------------------------------------------
```
The following example does not actually contain a GROUP BY clause, but because the SELECT clause contains a [Set function specification](set_function_specification.md) the statement may be viewed as one that contains an implicit GROUP BY clause, containing no *<**column reference**>**s*.
```

SELECT AVG( salary )
FROM dbtst120
WHERE edleval > 17
```
The result of applying the implicit GROUP BY clause is the following grouped table. Note that the table consists of a single group and that it does not have any grouping columns.
```

edlevel    salary            firstnme            ...
-------------------------------------------------------------
18         52750.00000000000 CHRISTINE
18         28420.00000000000 HEATHER
18         29840.00000000000 JENNIFER
20         38250.00000000000 SALLY
-------------------------------------------------------------
```

## Related topics
- [FROM clause](from.md)

- [HAVING clause](having.md)

- [SELECT clause](select.md)

- [Infor Enterprise Server SQL](baan_sql.md)
