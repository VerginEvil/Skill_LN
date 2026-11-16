# db.check.row.dlocked()

## Syntax:
`function long db.check.row.dlocked( long table_id )`

## Description
This checks whether the row, identified by its primary key columns is delayed locked or not. If the row is already locked, the function returns the dlock number of the row. This function can result in a considerable performance gain as it eradicates the need for multiple reads of the same record.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |

## Return values
| | |
|---|---|
| 0 | Row is not locked |
| n | The dlock number, implying that row is locked |
| < 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

...
dbtst120.empno = 10

| Lock the row only if it is not locked
if ( db.check.row.dlocked( tdbtst120 ) = 0 ) then
    | row not locked
    select *
    from dbtst120 for update
    where empno=10
    selectdo
    endselect
endif

db.delete( tdbtst120, DB.RETRY )
...
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
