# Ordered hint
The ordered hint advises the query processor to join the tables of the query in the order in which they are listed in the from clause. For example:
```

select a.bpid, b.bpid
from   tccom100 a, tfgld106 b, tfacr200 c
where  b.bpid = a.bpid
and    b = c.bpid
hint   ordered
```
In this query, first table tccom100 should be joined with table tfgld106. The result of this should be joined with table tfacr200.
An ordered hint does not give you the guarantee that the tables are actually joined in that order. In case you are working on the Oracle level-2 driver the hint is simply added to the Oracle query. Its effect depends on how Oracle interprets this hint. In case you are working on a level-1 driver the tables are joined in the specified order if it does not conflict with any other fixed order that may exist due to a 'refers to' expression, a subquery or a company number expression. For example:
```

select tppin020.cmbc
from   tppdm740, tppin020
where  tppin020.cmbc refers to tppdm740
hint   ordered
```
On a level-1 driver the 'refers to' expression already dictates a fixed join order between the tables tppdm740 and tppin020. They cannot be joined in the order of the from clause, therefore the ordered hint has no effect. To make the ordered hint take effect you can substitute the 'refers to' expression with an 'equal' expression:
```

select tppin020.cmbc
from   tppdm740, tppin020
where  tppin020.cmbc = tppdm740
hint   ordered
```
Now the join can be performed in the hinted order. Replacing the 'refers to' expression may however not always be possible.

## Related topics
- [Hint types](hint_types.md)
- [Query hints overview](overview.md)
