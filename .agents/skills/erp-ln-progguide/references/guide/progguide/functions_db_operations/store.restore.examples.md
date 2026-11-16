# Storing, restoring record buffers - Examples

## Code Example 1
Storing and restoring the record buffer can be used e.g. for accessing the same table for another record.
Before reading, you call [db.store.record()](db.store.record.md) to store the current record buffer. After such an action you can restore the record buffer with [db.restore.record()](db.restore.record.md) and continue with that data.
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

## Code Example 2
You can use [db.store.record()](db.store.record.md) and [db.record.changed()](db.record.changed.md) for optimizing reading data from a table.
```

function read.item.data(domain tcitem i.item)
{
        tcibd001.item = i.item
        tcibd001._compnr = get.compnr()

        if not db.record.changed(ttcibd001) then
                return
        endif

        select  tcibd001.*
        from    tcibd001
        where   tcibd001.item = :tcibd001.item
        as set with 1 rows
        selectdo
        selectempty
                db.set.to.default(ttcibd001)
        endselect

        db.store.record(ttcibd001)
}
```

## Explanation
The first time `read.item.data()` is executed, [db.store.record()](db.store.record.md) has not yet been called, therefore [db.record.changed()](db.record.changed.md) returns `true`, and the query will be executed. After the query is executed, the contents of the record buffer is stored with [db.store.record()](db.store.record.md).
The second time this function is called, one of the following situations can occur:

- The record buffers are the same, so the function returns.

- The record buffers are not the same, the query is done again etc.

The record buffer can be changed due to:

- another item has been read the last time (key fields differ)

- another function has read some fields of another item

- another function has updated this item in the database

In all these cases the item will be read again. So this implementation ensures that you will always have access to the most recent data. Note however, that it is not possible to see changes made by other users.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
