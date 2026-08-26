# Index hint
An index hint advises the query processor to scan a table with the specified index. For example:
```

select bpid, nama
from   tccom100
where  bpid > '  1000' and nama >= 'Z'
hint   use index 2 on tccom100
```
This index hint suggests to the query processor to scan table tccom100 using index 2. Optionally, you can specify the mode, ascending or descending, of the index. For example:
```

select bpid, nama
from   tccom100
where  bpid > '  1000' and nama >= 'Z'
hint   use index 2 on tccom100 desc
```
Table tccom100 must be accessed using index 2 in descending order. With one index hint you can hint more than 1 index for the table. There is a maximum of 10 indexes you can specify per index hint. If you specify more than one index hint the query processor may use one of these indexes to scan the table or it may use a combination of the indexes. Consider for example the following query:
```

select  iscn, bpid
from    tccom100
where   (iscn = 570 or cadr = 'J10000001') and nama >= 'A'
hint    use index 1,2 on tccom100
```
Assume index 1 is on column iscn and index 2 is on column cadr, furthermore assume there is an index 3 on column nama. By hinting on both index 1 and index 2 this query can be solved by firing two index scans.
Index scan 1 on index 1:
```

select  iscn, bpid
from    tccom100
where   iscn = 570 and nama >= 'A'
```
Index scan 2 on index 2:
```

select  iscn, bpid
from    tccom100
where   cadr = 'J10000001' and nama >= 'A'
```
Performing these two index scans may be faster than executing one index scan on index 3.

## Related topics
- [Hint types](hint_types.md)
- [Query hints overview](overview.md)
