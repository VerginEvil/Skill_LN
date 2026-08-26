# Array fetching hint
Some RDBMSs offer the possibility to fetch, with a single fetch call, an array of rows in stead of just one row. This can be beneficial for queries that select many rows because it reduces network traffic between the driver and the RDBMS. You can enable array fetching for a single query as follows:
```

select a.bpid
from   tfgld106 a, tccom100 b
where  a.bpid refers to b
hint   array fetching
```
**Just as buffering many rows, array fetching is not advantageous in all cases. You can disable array fetching for a single query as follows:
```

select a.bpid
from   tfgld106 a, tccom100 b
where  a.bpid refers to b
hint   no array fetching
```
**The array hint overrides the default behavior of the driver. If by default the driver uses array fetching you can override this with the disable hint and if by default the driver does not use array fetching you can enable it.
If the RDBMS does not support array fetching at all then the array hint is simply ignored. The array hint does not affect the actual size of the array, see [Array size hint](array_size_hint.md).

## Related topics
- [Hint types](hint_types.md)
- [Array size hint](array_size_hint.md)
- [Query hints overview](overview.md)
