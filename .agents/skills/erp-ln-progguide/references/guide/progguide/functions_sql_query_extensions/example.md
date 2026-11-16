# Query extensions sample program
This is an example of a simple query extension programmed in the DAL for the main table 'qmptc015'. The unit (qmptc021.cual) of the algorithm (qmptc015.algo) must have the same physical quantity as the unit defined in the table (qmptc015.chun).
```

function extern long before.open.object.set()
{
        query.extend.select("qmptc021.cual")
        query.extend.from("qmptc021")
        query.extend.where(":qmptc015.algo refers to qmptc021")
}

function extern long qmptc015.algo.check(long has_changed)
{
        if has_changed then
                tcibd.dll0003.read.mcs001.tccu(qmptc015.chun,
                     qmptc021.cual, basu.tccu, unit.tccu)
                if basu.tccu <> unit.tccu then
                        dal.set.error.message("qmptcs011526")
                        |* Algorithm and characteristic units must have the
                        |* same physical quantity
                        return(DALHOOKERROR)
                endif
        endif
}
```
An example of a simple query extension programmed in the UI script.
```

field.tejzw101.orno:
selection.filter:
    query.extend.where.in.zoom("tejzw100.item = " & quoted.string(tejzw101.item))
    | quoted.string() is used  here, because the value of tejzw101.item might contain (double) quotes.
```
An alias example of query extension the before.program of UI script.
```

before.program:

	| maintable whinr140
	string	sql.where(1024)

	domain	tcitem	filter.item
	domain	tccwar	filter.cwar

	filter.item = "         WHITEM0001-12/10 00:40:08 OWIZZYNHS8AL"
	filter.cwar = "WHWH02"

	sql.where = "whinr140.cwar = "& quoted.string(filter.cwar) &
			" and whinr140.item = "& quoted.string(filter.item)
			&" and whinr140.qhnd - whinr140.qblk - whinr140.qlal>0"

	| Filtering with alias on compulsory reference
	sql.where = sql.where &
		  	" and whinr140.cwar refers to whwmd200flt UNREF setunref"
	| or in other syntax:
	|sql.where = sql.where & " and whwmd200.cwar = whinr140.cwar"

	query.extend.from("whwmd200 whwmd200flt ",EXTEND_OVERWRITE)
	query.extend.where(sql.where,EXTEND_OVERWRITE)
```

## Related topics
- [SQL query extensions overview](overview.md)

- [SQL query extensions synopsis](synopsis.md)

- [Column filtering](column_filtering.md)
