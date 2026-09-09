# Logging
You can use the logging information of the driver to see if the hints you added have taken effect. Logging information differs between level-1 drivers and the Oracle level-2 driver. All logging is done in the dbs.log file.

## Buffer hint
Set TT_SQL_TRACE=4000 and DBSLOG=2000. The logfile will contain an entry: RDS_FULL: <buffer size>.

## Array fetching hint
Set DBSLOG=1000 if the array fetching hint is applied to logfile will show one of the entries:
`Hint used: array fetching enabled Hint used: array fetching disabled`

## Array size hint
Set DBSLOG=1000. If the array size hint applies the logfile will show the entry:
`Hint used: array size set to <array size>`

## Index, row mode, string, ordered and 'no hints' hint
For the Oracle level-2 driver the hints index, row mode, string, ordered and 'no hints' all effect the Oracle native hint that is added to SQL query that is sent to the Oracle RDBMS. If you set DBSLOG=400 the driver will log the SQL query that is sent to the Oracle RDBMS, this includes the hints.
On a level-1 driver only the index hint and ordered hint are applicable, the row mode, string and 'no hints' hint are ignored.
To see the effect of the ordered hint on a level-1 driver set TT_SQL_TRACE=4000 and DBSLOG=2000. The driver will log the generated query execution tree. For the main query and each subquery the execution tree shows a section 'Tables'. This section lists the tables in the order in which they are processed. For example:
```

select a.bpid, b.bpid
from   tccom100 b, tfgld106 a
where  a.bpid = b.bpid
hint   ordered
```
For this query the dbs.log file will show in the query execution tree a section that looks as follows:
```

Query 4006e078 flag 0100000
Tables
         tccom100 (a) dep 1 flag 014
      Used columns
      tccom100(a).bpid
tfgld106 (b) dep 2 flag 014
      Used columns
      tfgld106(b).bpid
```
The effect of index hints can be read in the log file from the generated query execution tree. The tree is logged when TT_SQL_TRACE=4000 and DBSLOG=2000. The information that states which indexes are used to scan the tables can be read from the section "view expression".
For example take the following query:
```

select  iscn, bpid
from    tccom100
where   (iscn = 570 or cadr = 'J10000001') and bpid = 'NAVEEN'
hint    use index 4,5 on tccom100 desc
```
In the log file the execution tree starts with the entry "Generated Query Execution Tree:", the section "view expression" is logged below this. For the above query the view expression section looks as follows:
```

View expression
[4] flag 011 cost 0 next_eval 9 next 9
   Table View on 'tccom100'
   Expression:
      [1] (hinted) flag 041 cost 5 next_eval -1 next 0
         [2] (hinted) flag 044 cost 5 next_eval 0 next 3
            [2] (hinted) flag 051 cost 5 next_eval -1 next -1
SrchOper for tccom100 compnr logic:111 physic:111,
index 4 (mode 0)
                  Field cadr:
                     Equal: [=] Bind (Col cadr) Value: 'J10000001'
                  Field bpid:
                     Equal: [=] Bind (Col bpid) Value: 'NAVEEN'
         UNION (04)
         [3] (hinted) flag 044 cost 5 next_eval 0 next -1
            [3] (hinted) flag 051 cost 5 next_eval -1 next -1
SrchOper for tccom100 compnr logic:111 physic:111,
index 5 (mode 0)
                  Field iscn:
                     Equal: [=] Bind (Col iscn) Value: '570'
                  Field bpid:
                     Equal: [=] Bind (Col bpid) Value: 'NAVEEN'
      AND (011)
      [0] flag 011 cost 3 next_eval 8 next 8
         Operand1: Index Col key 1 mode 1 equal 1 order 0
               tccom100(a).bpid
         Operator: =
         Operand2: Bind (Col bpid) Value: 'NAVEEN'
```
Each "SrchOper" section in the view expression describes an index scan. Here there are two such "SrchOper" sections for the table tccom100. This indicates the table is accessed using two index scans. The first is on index 4, the second on index 5 exactly according to specified hint. The log output also shows the word "hinted" for both "SrchOper" sections. This means the query processor has indeed applied the index hint and that it is not a coincidence that indexes 4 and 5 are used to scan the table.

## Related topics
- [Hint types](hint_types.md)

- [Query hints overview](overview.md)
