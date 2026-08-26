# Array size hint
The array size hint specifies the size of the array to be used for array fetching (see also [Array fetching hint](array_fetching_hint.md)).
It specifies the maximum number of records that the array can hold. It only specifies the size, it does not actually enable array fetching. If the driver does not perform array fetching by default then you need to enable it with an array fetching hint. For example:
```

select a.bpid
from   tfgld106 a, tccom100 b
where  a.bpid refers to b
hint   array fetching
and    array size 1000
```
The size specified will override the default array size (for this particular query). The size must be at least 1. If the database does not support array fetching this hint is simply ignored.

## Related topics
- [Hint types](hint_types.md)
- [Array fetching hint](array_fetching_hint.md)
- [Query hints overview](overview.md)
