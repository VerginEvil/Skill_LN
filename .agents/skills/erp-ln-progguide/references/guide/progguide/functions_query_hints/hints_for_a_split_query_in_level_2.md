# Hints for a split query in level-2
To evaluate a query the Oracle level-2 driver may split up a query in several smaller ones (child queries). When this happens the hints of the main query are distributed over these smaller queries. This is done according to the same rules as when the query was truly distributed:

- An index hint is only added to a child query if it contains the corresponding table in its from clause.

- All other hints are added to all child queries.

## Example
```

select a.cuno, b.cuno
from   tppdm740 a, tccom010 b
where  a.cuno refers to b
and    a._compnr = 812
hint   use index 1 on b
and    array fetching
and    array size 100
```
The Oracle level-2 driver will split this query into the following to child queries:
Query 1:
```

select a.cuno
from   tppdm740 a
and    array fetching
and    array size 100
```
Query 2:
```

select b.cuno
from   tccom010 b
where  b.cuno = <variable>
hint   use index 1 on b
and    array fetching
and    array size 100
```
Query 1 does not have any execution plan hints and therefore the driver will generate default hints for this query. Just like with distributed queries you can prevent the driver from generating default hints for query 1 by adding the hint 'no hints' to the main query. Adding this hint will have no effect for query 2.

## Related topics
- [Hint types](hint_types.md)

- [Query hints overview](overview.md)
