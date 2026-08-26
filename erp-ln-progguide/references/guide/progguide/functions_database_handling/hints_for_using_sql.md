# Hints for using SQL
1. In the WHERE clause:
- use as few conditions as possible
- use as many conditions with indexes as possible
- use as many conditions with combined fields as possible
- use BETWEEN/INRANGE when an upper and lower boundary are specified for a field.
1. Use REFERS TO if references have been defined in the data dictionary.
1.  Use as few overlapping OR conditions as possible. For the following:
```

cpac&cmod >= 'ttadv' (only if there is no index to cpac&cmod)
```
do not use the following construction:
`WHERE ttadv200.cpac > 'tt' OR ttadv200.cpac >= 'tt' AND ttadv200.cmod >= 'adv'`
instead use the following construction:
`WHERE ttadv200.cpac > 'tt' OR ttadv200.cpac = 'tt' AND ttadv200.cmod >= 'adv'`
1. Only select fields of tables necessary in the flow of the program.
1. It is not necessary to bind external variables and database fields used in the query as substitution variables. In embedded SQL local variables are bound automatically.
1. The program executes the query the first time the function [sql.fetch()](../functions_dynamic_sql_queries/sql.fetch.md) is called. If reading in the entire set is unnecessary (so no order by, group by, and so on), the program only physically retrieves records at each *sql.fetch()*. This avoids an entire set being retrieved when only part of it is used. When the set is no longer necessary call [sql.break()](../functions_dynamic_sql_queries/sql.break.md) to clear the remaining records.
1. Use ORDER BY to ensure that the records are retrieved in the correct sequence. If an index can be used for the ORDER BY, no sort action will take place beforehand.
1. The program will execute a Full Table Scan (FTS) if the operators NOT INRANGE, IN, LIKE are used and if no index (or part of an index) is used. This means that the system checks beforehand whether all records in the table meet the conditions of the query. This precludes optimization. If only the first part of an index (combined or normal field) is used, the system uses that index to search the table. When GROUP BY is used, the system first determines the entire set (prepared set), before producing the first record. The same thing happens if the operator is preceded by an expression –for example, WHERE <table.field1> & <table.field2> = "...........". Note that the various subexpressions separated by AND or OR cannot be combined for optimization.
1. It is possible to have the program carry out commits at certain points in the select loop. If retry points are included, use of ORDER BY is required to ensure that the sequence after return to the retry point is identical to the one used the first time. See also the practical examples.
1. If a transaction adds or processes records, it depends on the database if the same transaction can also process new records without a select being carried out again. To ensure that new records are processed in any case, a commit and a new select are required. To ensure that new records are not processed, define the set at the point of the select (prepared set).
1. When using transactions, the first priority should be that the actions within the transaction constitute a logical unit. For reasons of performance, update, insert, and delete actions can be combined up to a number of 256 (this is an average, not a limit) per transaction. For example, programs processing orders should execute one *commit.transaction()* for each order.
1.  It may be necessary to know how far the program had advanced before it moved back to the retry point. If the key consists of more than one field, it is probably possible to have the program execute a *commit.transaction()* when a particular key field changes. If a key consists of order number and order line, for instance, a commit by order number would be preferable to a commit by order line. Care should be taken in programs that print and process data in one run. An abort transaction restores the database but not the output to the printer. In such cases a commit must be executed for each print line to prevent lines being printed twice. For example:
```

save.orno = start
select for update orderline.orno, orderline.pono
from orderline
where orderline.orno >= :save.orno
selectdo
       if ( save.orno <> orderline.orno ) then
            commit.transaction()
            save.orno = orderline.orno
       endif
       update actions()
endselect
commit.transaction()
```
1. A [db.retry.point()](../functions_db_operations/db.retry.point.md) must be included in each update program.

## Related topics
- [Database handling overview](overview.md)
- [Infor Enterprise Server SQL](baan_sql.md)
