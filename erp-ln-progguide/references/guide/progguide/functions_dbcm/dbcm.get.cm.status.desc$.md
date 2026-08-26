# dbcm.get.cm.status.desc$()

## Syntax:
`function string dbcm.get.cm.status.desc$( const string toid$, enum prev_stat, enum curr_stat )`

## Description
Retrieves the Change Management status description of the Business Object that is identified by the given Typed Object Id.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id; this is a string of 34 characters identifying a business object.  |
| `enum` | `prev_stat` |  The checked-in value of the application status field, can be retrieved by function [dbcm.get.rcd.prst()](dbcm.get.rcd.prst.md).  |
| `enum` | `curr_stat` |  The checked-out value of the application status field, can be retrieved by function [dbcm.get.cm.status()](dbcm.get.cm.status.md).  |

## Return values
In case the object is checked-in: the approval status description
In case the object is checked-out: The workflow application status information description, if not found, the Change Management status description.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Example
```

    select  tfgld018.*
    from    tfgld018
    where   tfgld018._index1 = {
                  :i.transaction.type,
                  :i.document.number }
    and     tfgld018._compnr = :i.financial.compnr
    as set with 1 rows
    selectdo
            l.workflow.status = dbcm.get.cm.status.desc$(
                            dbcm.get.rcd.toid$(ttfgld018),
                            dbcm.get.rcd.prst(l.table.id),
                            tfgld018.subm)
    endselect
```

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
