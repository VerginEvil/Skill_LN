# db.record.changed()

## Syntax:
`function boolean db.record.changed( long table_id, [ long size ] )`

## Description
Tests whether the current value of the record buffer belonging to the given table id has changed since the last call of [db.store.record()](db.store.record.md).
First, a [db.columns.to.record()](db.columns.to.record.md) is done in order to copy the table field values to the record buffer. Then this record buffer is compared to the one stored with [db.store.record()](db.store.record.md).
Note  Note that, because of performance reasons, `db.record.changed()` is implemented as a macro. This is the actual implementation:
```

#define db.record.changed(tbl)
^       (db.columns.to.record(tbl) <> 0 or changed(rcd.##tbl, KEEP.CHANGED.FLAG.RAISED))
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

## Return values
| | |
|---|---|
| true | Record was changed since the last call to [db.store.record()](db.store.record.md) |
| false | Record was not changed |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  If [db.store.record()](db.store.record.md) has not been called before, this function returns TRUE.
After a company switch, _compnr will be set to -1 in the record buffers. This means `db.record.changed` will return `true`, even if the record was not modified otherwise.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)

- [Storing, restoring record buffers - Examples](store.restore.examples.md)
