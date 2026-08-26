# String hint
With the string hint you can add a native RDBMS hint to the query. The string hint is added to the query 'as is'. Using the string hint you can supply hints that are not directly supported. For example, the Oracle RDBMS supports the hint USE_CONCAT, but this hint is not supported through BaanSQL hints. You can now supply this hint as follows:
```

select nama
from tccom100
where bpid = '1000' or bpid = '2000'
hint "USE_CONCAT"
```
Everything between the double quotes is added to the query as is. It is up to the programmer to verify the correct syntax and semantics of the hint.
The string hint is only applicable to the Oracle level-2 driver. For any other driver this hint is ignored.

## Related topics
- [Hint types](hint_types.md)
- [Query hints overview](overview.md)
