# db.store.record()

## Syntax:
`function void db.store.record( long table_id, [ long size ] )`

## Description
Creates a copy of the current value of the record buffer belonging to the given table id. Later on this copied value can be restored by calling [db.restore.record()](db.restore.record.md).
[db.record.changed()](db.record.changed.md) compares the current record buffer values with the copy that is created with `db.store.record()`.
Note  Note that, because of performance reasons, `db.record.changed()` is implemented as a macro. This is the actual implementation:
```

#define db.store.record(tbl)
^       db.columns.to.record(tbl)
^       on.change.check(rcd.##tbl)
```
The optional argument size can be used from TIV level 2120 Usage example
```

|* example of using db.store.record / db.change.record with size argument
long	size
long	ret
long	dummy
table	ttcmcs003

ret = rdi.table("tcmcs003", dummy, dummy, dummy, size)
|Size is the length of a row in the table without the internal data
db.store.record(ttcmcs003, size)
ret = switch.to.company(0)	|This will change tccom003._compnr stored in the internal data
if db.record.changed(ttcmcs003, size) then
	|record is changed (This happens when you call one of the functions without size)
else
	|record is not changed (Using size the internal record data like _compnr is not compared)
endif
```

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID in the format `tppmmmxxx`. E.g. `twhinh200`  |
| `[ long` | `size ]` |  The size of the part that is stored  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
- [Storing, restoring record buffers - Examples](store.restore.examples.md)
