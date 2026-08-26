# Hints in a distributed environment
If a query is distributed, it is executed using multiple database drivers. In this case a driver may not receive all hints because the client distributes the hints over the database drivers. The client distributes the hints according to the following two simple rules:
1. An index hint is only sent to the driver if it handles the corresponding table.
1. All other hints are sent to all drivers.
```

select tppdm740.cuno, tccom010.cuno
from   tppdm740, tccom010
where  tppdm740.cuno refers to tccom010
hint   use index 1 on tccom010
and    buffer 10 rows
```
Assume for the above query that the table tppdm740 is stored in database 1 and table tccom010 in database 2. In this case the following queries are sent:
To driver 1:
```

select tppdm740.cuno
from   tppdm740
hint   buffer 10 rows
```
To driver 2:
```

select tccom010.cuno
from   tccom010
where  cuno = <variable>
hint   use index 1 on tccom010
and    buffer 10 rows
```
The buffer hint is sent to both drivers but the index hint is only sent to driver 2. As a result of this driver 1 does not receive any execution plan hints and generates default hints. If you do not want driver 1 to generate default hints you can add the hint 'no hints':
```

select tppdm740.cuno, tccom010.cuno
from   tppdm740, tccom010
where  tppdm740.cuno refers to tccom010
hint   use index 1 on tccom010
and    buffer 10 rows
and    no hints
```
The hint 'no hints' is sent to both drivers. For driver 2 this makes no difference. The index hint takes precedence over the 'no hints' hint and therefore the 'no hints' hint is ignored. Driver 1 receives the following query:
```

select tppdm740.cuno
from   tppdm740
hint   buffer 10 rows
and    no hints
```
Driver 1 will not generate default hints.

## Related topics
- [Hint types](hint_types.md)
- [Query hints overview](overview.md)
