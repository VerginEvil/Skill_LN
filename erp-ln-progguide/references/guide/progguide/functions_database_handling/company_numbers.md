# Company numbers
The company number used during execution of a BAAN 4GL query is the current company number. The current company number is always inherited from the parent session. The root session (Worktop/WebUI/LN UI) reads the company number from the default company number ( defined in the session "Maintain User Data" ). This company number can be changed by calling the function [compnr.check()](../functions_company_operations/compnr.check.md)

## The <table>._compnr field
The <table>._compnr field enables the use of different company numbers. This field specifies the actual company number of the table. When this field is undefined, the current company number is taken as the default. 'Undefined' is denoted by the value -1.
When a record is selected with 'select <table>.*', the field <table>._compnr in the record contains the company number of the table. When inserting a record in a table with a specific company number, you must fill <table>._compnr with the corresponding company number. The function [db.insert()](../functions_db_operations/db.insert.md) takes care of this and writes the record in the correct (physical) table. No special file pointers are necessary (for example, by using [db.bind()](../functions_db_operations/db.bind.md)).

## Example
```

The record where the field ttadv100._compnr = 000 belongs to the
(physical) table ttadv100000
The record where the field ttadv100._compnr = 200 belongs to the
(physical) table ttadv100200
```

## Using <table>._compnr in the WHERE clause
You can also use <table>._compnr in the WHERE clause of a Infor Enterprise Server SQL statement. In this case it is used as a search condition. For example:
```

SELECT  ttadv100.*
FROM    ttadv100
WHERE   ttadv100._compnr = 200 AND ttadv100.cpac = 'tt'
```
This query lists all records from table ttadv100200 where ttadv100.cpac has the value 'tt'.
You can use <table>._compnr in the following ways:
- <table>._compnr = <number> or <number> = <table>._compnr where <number> specifies an integer number. The value of <number> is taken as the company number. It must be a 3-digit number.
- <table>._compnr = <bind variable> or <bind variable> = <table>._compnr where <bind variable> specifies an integer number. When the query is executed the value of <bind variable> is taken as the company number. It must be a 3-digit number.

## Combining <table>._compnr conditions
-  A list of AND conditions can contain only one condition that includes <table>._compnr. So, the following construction is possible:
`WHERE <table>._compnr = 100 AND <condition>`
but the following is not possible:
`WHERE <table>._compnr = 100 AND <table>._compnr = 200`
It is possible to include multiple <table>._compnr._compnr conditions that specify the company number of different table references. For example, the following construction is possible:
`WHERE <table1>._compnr = 100 AND <table2>._compnr = 200`
- In a list of OR conditions, none of the conditions may contain a condition on <table>._compnr.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
