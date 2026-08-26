# Multi Table synopsis
Note  Multi Table functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).
Multi Table functionality by table name (i.e. functions sec.*.by.name)is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 2210](../tiv/tiv_2210.md).
- `void [sec.add.set()](sec.add.set.md) ( long id )`
- `void [sec.add.set.by.name()](sec.add.set.by.name.md) ( const string tablename() )`
- `long [sec.add.table()](sec.add.table.md) ( const string tablename(), ... )`
- `long [sec.get.update.status()](sec.get.update.status.md) ( long id, long occ )`
- `long [sec.get.update.status.by.name()](sec.get.update.status.by.name.md) ( const string tablename(), long occ )`
- `void [sec.mark.delete()](sec.mark.delete.md) ( long id )`
- `void [sec.mark.delete.by.name](sec.mark.delete.by.name.md) ( const string tablename() )`
- `boolean [sec.record.exists()](sec.record.exists.md) ( long id, long occ )`
- `boolean [sec.record.exists.by.name()](sec.record.exists.by.name.md) ( const string tablename(), long occ )`

## Related topics
- [Multi Table Overview](overview.md)
