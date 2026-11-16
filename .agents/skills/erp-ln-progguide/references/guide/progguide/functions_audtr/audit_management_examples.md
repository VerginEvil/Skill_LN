# Audit management examples
This section contains some examples of the Infor Enterprise Server Audit Management. The examples are given in pseudo code. To keep the examples clear, error handling is not included. Note the examples demonstrate a metaphorical usage of the audit trail functions.
In both examples, the following variables are used:
```

nr.fields = 8
my.fields(1) = "item"
my.fields(2) = "kitm"
my.fields(3) = "citg"
my.fields(4) = "itmt"
my.fields(5) = "dsca"
my.fields(6) = "dscb"
my.fields(7) = "dscc"
my.fields(8) = "dscd"
nr.tables = 1
my.tables(1,1) = "tcibd001"
my.companies(1) = 800
```

## Batch-oriented replication
To obtain the changes on table tcibd001 in company 800 that occurred on 10-10-1998:
```

#include <bic_audhdr.h>
#include <bic_audlib>

range.str = "#COMMITTIME# between 10-10-1998 00:00:00 and
10-10-1998 23:59:59"
| note that the UTC representation actually is different, but it has been
| formatted this way to increase readability of this example
IF aud.select.transactions(nr.tables, my.tables, my.companies, range.str,
                           selection.id, "tcibd001, 800) = AUD_OK
THEN
    WHILE aud.get.next.transaction(selection.id, 0, 0,
				   transaction.id, commit.time,
				   session, user) = AUD_OK
	process.transaction.header(transaction.id,commit.time,session, user)
	WHILE aud.get.next.action(selection.id, table.id, company, table.code,
				  meta.data.changed, action.nr,
				  action.type) = AUD_OK
	    process.action.header(company, table.code, company,
				  action.nr, action.type)
	    IF meta.data.changed THEN
		IF aud.get.field.ids(selection.id, table.id,
				     nr.fields, my.fields, field.ids) = AUD_OK
		THEN
		    process.meta.data(nr.fields, my.fields, field.ids)
		    | This function uses aud.get.field.info()
		ENDIF
	    ENDIF
	    FOR field.nr = 1 to nr.fields
		IF aud.get.field.status(pid, my.fields(i),
		                        selection.id, table.id,
					field.ids(nr.fields)) = "X"
		THEN
		    IF action.type = "D" or action.type = "U" THEN
		       aud.put.old.field.value(pid, my.fields(field.nr),
					       selection.id, table.id,
					       field.ids(field.nr))
		       process.old.value(my.fields(field.nr))
		    ENDIF
		    IF action.type = "I" or action.type = "U" THEN
		        aud.put.new.field.value(pid,my.fields(field.nr), selection.id,
			                        table.id, field.ids(field.nr))
		        process.new.value(my.fields(field.nr))
		    ENDIF
		ENDIF
	    END FOR
	ENDWHILE
    ENDWHILE
    aud.close.selection(selection.id)
ENDIF
```

## Event-driven replication
To react on changes on table tcibd001 in company 800:
```

#include <bic_audhdr.h>
#include <bic_audlib>

StartOfInterval = get.commit.time.of.previously.processed.transaction()
range.str = " #COMMITTIME# > " & StartOfInterval
IF aud.select.transactions(nr.tables, my.tables, my.companies, range.str,
                           selection.id, "tcibd001, 800) = AUD_OK
THEN
    REPEAT
	RetVal = aud.get.next.transaction(selection.id, 100, 10000,
					  transaction.id, commit.time,
					  session, user)
	IF RetVal = AUD_OK
	    process.transaction.header(transaction.id, commit.time,
		                       session, user)
	    WHILE aud.get.next.action(selection.id, table.id, company,
				      table.code, meta.data.changed,
				      action.nr, action.type) = AUD_OK
		    | See previous example on how to process action information
	    ENDWHILE
	ENDIF
    UNTIL RetVal = FAIL or process.stopped.by.user()

    aud.close.selection(selection.id)
    set.commit.time.of.previously.processed.transaction(commit.time)
ENDIF
```

## Related topics
- [Audit management overview](audit_management_overview.md)

- [Audit management synopsis](audit_management_synopsis.md)
