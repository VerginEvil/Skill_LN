# db.restore.record()

## Syntax:
`function void db.restore.record( long table_id )`

## Description
This restores the record of the given table that was stored previously with [db.store.record()](db.store.record.md). Also the table's field values will be restored.
Note  Note that, because of performance reasons, `db.record.changed()` is implemented as a macro. This is the actual implementation:
```

#define db.restore.record(tbl)
^       not.curr(rcd.##tbl)
^       db.record.to.columns(tbl)
```

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID in the format `tppmmmxxx`. E.g. `twhinh200`  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Restoring the value is considered a value change. So if you call [db.record.changed()](db.record.changed.md) after this function, that function will return `true`.

## Example
```

db.store.record(twhinh200)

select  whinh200.*
from    whinh200
where   whinh200._index1 = {:...}
selectdo
        ...
endselect

db.restore.record(twhinh200)
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
- [Storing, restoring record buffers - Examples](store.restore.examples.md)
