# Buffer hint
The query processor at the driver side fetches records from the RDBMS (e.g. Oracle). It does not directly send these records to the client (BShell) but buffers them in an internal 'RDS' bufffer. When this buffer is full the entire buffer is sent to the client. With a buffer hint you can specify the size of this RDS buffer for this particular query. The size of the buffer is specified in rows. For example:
```

select a.bpid
from   tfgld106 a, tccom100 b
where  a.bpid refers to b
hint   buffer 100 rows
```
Thus in the above example the buffer will be able to hold exactly 100 rows. The size of the buffer must be at least 1. The buffer size only holds for the hinted query.
A buffer hint can be used for a query that selects a large set of records and when we need to process all of these records. In this case a large set of records has to be transferred from the driver to the client. It is more efficient to transfer a few large sets than transferring a large amount of small sets. However using a large buffer may not be beneficial in all cases. If a query selects a large set of records but we actually use only the first few records then buffering many rows may in fact be disadvantageous.
A buffer hint is never ignored when the database driver runs as a separate process ("Standalone"). When the database driver is loaded as a DLL ("Combo",) the hint is ignored and has no impact on performance and memory.

## Related topics
- [Hint types](hint_types.md)
- [Query hints overview](overview.md)
