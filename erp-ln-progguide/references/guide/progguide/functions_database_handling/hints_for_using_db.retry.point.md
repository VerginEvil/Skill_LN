# Hints for using db.retry.point
For programs of type 1, 2 or 3, this is generally the retry.point of the 4GL engine which has a retry just after 'before choice' of update.db and in the read section where also the references are read.
To have clearly structured sources, never use more than one level *db.retry.point()*. Only one above the first level of select. Use retry in the following situations:
| | | |
|---|---|---|
| Situation for Select | Commit per fetch | Commit over multiple fetch |
| db.update/db.insert/db.delete | 1 | 2 |
| Collecting | 3 | 3 |
| Combination | 4 | 5 |
A skip back to a retry point can be indicated by a problem in:
- db.update(), db.delete() or db.insert() with argument db.retry
- commit.transaction()

## Situation 1: Only update actions, commit per fetch
The function 'with retry' can be used here. For example:
```

db.retry.point()
select  tisfc001.*
from    tisfc001 for update
where   tisfc001.pdno inrange :pdno.f and :pdno.t
order by tisfc001._index1 with retry
selectdo
        tisfc001.proc = tcyesno.yes
        db.update(ttisfc001,db.retry)
        commit.transaction()
endselect
```
In this case REPEAT LAST ROW is not used, because when retry is done, the value that was present at the stage of *commit.transaction()* has certainly been saved.

## Situation 2: Only update actions, commits over fetches
In this case we can also use the 'with retry' option. For example:(commit per order and not per fetch !):
```

save.pdno = 0
db.retry.point()
select  ticst001.*
from    ticst001 for update
where   ticst001.pdno inrange :pdno.f and :pdno.t
order by ticst001._index1 with retry repeat last row
selectdo
        if ticst001.pdno <> save.pdno then
                if save.pdno <> 0 then
                        commit.transaction()
                endif
                save.pdno = ticst001.pdno
        endif
        ticst001.proc = tcyesno.yes
        db.update(ticst001,db.retry)
selecteos
        commit.transaction()
endselect
```
Both *db.update()* and *commit.transaction()* can result in a retry. So selecteos is used. Notice that REPEAT LAST ROW is used because the present value at the time of doing the save is already the value of the next order.

## Situation 3: only print / collect actions (no commit)
There is no transaction or dependency between records / fetches. For example:
```

total.quant = 0
select  ticst001.*
from        ticst001
where   ticst001.pdno inrange :pdno.f and :pdno.t
order by ticst001._index1
selectdo
        total.quant = total.quant + ticst001.quan
        print.row(1)
endselect
```

## Situation 4: Update actions plus print/collect with commit per fetch
For example, update of print status plus print and collect:
```

db.retry.point()
select  ticst001.*
from    ticst001 for update
where   ticst001.pdno inrange :pdno.f and :pdno.t
order by ticst001._index1 with retry
selectdo
                ticst001.proc = tcyesno.yes
                db.update(ticst001,db.retry)
                commit.transaction()
                total.quant = total.quant + ticst001.quan
                print.row()
endselect
```
Notice that this works only when the *db.update()* and *commit.transaction()* are done before the print and the collect statement. An alternative to this solution is described in situation 5.

## Situation 5: Update actions plus print/collect with commit over fetches
For example, update of print status plus print and collect per order:
```

save.pdno = 0
save.pono = 0
total.select.quan = 0
db.retry.point()
total.order.quan = 0
select  ticst001.*
from    ticst001 for update
where   ticst001.pdno inrange :pdno.f and :pdno.t
order by ticst001._index1 with retry repeat last row
selectdo
        if ticst001.pdno <> save.pdno then
                if save.pdno <> 0 then
                        total.order.quan = 0
                        commit.transaction()
                endif
                save.pdno = ticst001.pdno
    endif
    if ticst001.pdno > lsp.pdno or
                        (ticst001.pdno = lsp.pdno and
                        ticst001.pono > lsp.pono ) then
                print.row()
                total.select.quan = total.select.quan + ticst001.quan
                lsp.pdno = ticst001.pdno
                lsp.pono = ticst001.pono
        endif
        total.order.quan = total.order.quan + ticst001.quan
        ticst001.proc = tcyesno.yes
        db.update(ticst001,db.retry)
selecteos
        commit.transaction()
endselect
```
*lsp* stands for last processed. pdno and pono are together the index of cst001. The 'lsp.' variables should always be used for this kind of saving within selects. These variables save which record has already been printed/collected. The total.order.quan can always be added because setting to zero is done for each retry again.
*NOTE:* This may give problems (i.e. skip some records for printing) if the sorting order in the database is different from the sorting order in the bshell. A possible solution is to use the database for doing the comparison `ticst001.pdno > lsp.pdno or (ticst001.pdno = lsp.pdno and ticst001.pono > lsp.pono)`, using a separate SQL select statement. The pattern, as shown here, is in use, and is known to give problems with MSQL in Unicode mode, when strings contain dashes.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
