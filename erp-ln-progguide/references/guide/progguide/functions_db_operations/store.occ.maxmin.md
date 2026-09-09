# store.occ.max(), store.occ.min()

## Syntax:
`function void store.occ.max( )`
`function void store.occ.min( )`

## Description
Normally, standard commands that access records of the main table can access all records of that table. You can use these functions to limit the records that can be accessed to those whose key values are within a specified range. Use *store.occ.max()* to define the upper limit of the range. Use *store.occ.min()* to define the lower limit of the range. If you wish, you can define only a maximum or only a minimum limit.
Before you call either of these functions, you must fill the key value with the required maximum or minimum value. If you set a limit that has previously been defined, the new value of the limit overwrites the previous value of the limit.
Use [set.limits.off()](set.limits.off.md) to switch off the limits defined with these functions.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
Note  For performance reasons, it is preferable to use [query.extend.where()](../functions_sql_query_extensions/query.extend.where.md) instead of these functions.

## Examples
```

| Suppose that on the
      first form you can access the entire main
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
