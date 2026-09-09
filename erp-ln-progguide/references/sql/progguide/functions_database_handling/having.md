# HAVING clause
The HAVING clause specifies a [grouped table](sql_glossary.md#GroupedTable). The input table of the HAVING clause is also a grouped table that is the result of applying the [GROUP BY clause](group_by.md). The HAVING clause rejects each group of the grouped table for which the search condition evaluates to False or Unknown.

## Syntax
```

<having clause>
    ::= HAVING <search condition>
```

## Semantics
The columns of the result grouped table have the same names and descriptors as the grouped table the HAVING clause operates on.
A group is in the result grouped table if and only if the *search condition* evaluates to True for that group.

## Examples
In the following example, the GROUP BY clause groups the rows of table *dbtst120* that satisfy the condition *sex = dbsex.female* by the column *edlevel*. The HAVING clause filters out all groups for which the maximum salary is less than or equal to 30000.
```

SELECT edlevel, AVG( salary )
FROM dbtst120
WHERE sex = dbsex.female
GROUP BY edlevel
HAVING MAX( salary ) > 30000
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
Applying the HAVING clause to the grouped table, gives the following grouped table.
```

edlevel    salary            firstnme            ...
-------------------------------------------------------------
16         36170.00000000000 EVA
16         29750.00000000000 EILEEN
16         23800.00000000000 DOLORES
16         17250.00000000000 SYBIL
-------------------------------------------------------------
18         52750.00000000000 CHRISTINE
18         28420.00000000000 HEATHER
18         29840.00000000000 JENNIFER
-------------------------------------------------------------
20         38250.00000000000 SALLY
-------------------------------------------------------------
```

## Related topics
- [GROUP BY clause](group_by.md)

- [SELECT clause](select.md)

- [Infor Enterprise Server SQL](baan_sql.md)
