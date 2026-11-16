# SQL subqueries
Infor Enterprise Server SQL permits the use of subqueries. These are SELECT statements in the WHERE clause of another SELECT statement.
Defining nested queries can be very difficult. It is best to define the subquery of the lowest level first and the main question last.

## Example 1
Select those prices from the item file that are above average. When calculating the average, the system should not take prices less than or equal to zero into account.
```

SELECT  tiitm001.copr                   | cost price
FROM    tiitm001
WHERE   tiitm001.copr >
                ( SELECT avg(tiitm001.copr)
                WHERE                   tiitm001.copr > 0 )
```
In this case, the subquery should only produce one result (here the average cost price). If the subquery produces more than one result, use the operators IN and EXISTS.

## Example 2
Select the numbers and names of all suppliers who have yet to deliver.
```

SELECT  tccom020.suno, tccom020.nama
FROM    tccom020                    | Suppliers
WHERE   EXISTS
                ( SELECT *
                FROM   timps053     | Purchase orders
                WHERE  timps053.suno = tccom020.suno )
```
The same query, in an alternative form:
```

SELECT  tccom020.suno, tccom020.nama
FROM    tccom020
WHERE   tccom020.suno IN
                ( SELECT   timps053.suno
                FROM     timps053 )
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
