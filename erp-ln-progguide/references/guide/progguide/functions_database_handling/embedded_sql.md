# Embedded SQL

## Syntax
The following loop structure enables the use of SQL as part of the language:
```

[ @sql.statement(cSqlAnnotation_SelectAllDataLanguages) ]
SELECT < set definition (= actual query, see SELECT statement) >
[ SELECTBIND ( number, var) ] ...
[ WHEREBIND (number, expression) ] ...
[ SELECTDO
                < operation(s) on all selected records > ]
[ SELECTEOS
                < operation(s) after last selected record > ]
[ SELECTEMPTY
                < operation(s) if nothing has been selected > ]
[ SELECTERROR
                < operation(s) in case of an error condition > ]
ENDSELECT
```

## Description
Data is selected on the basis of the condition specified in the SELECT statement. The operations between SELECTDO and ENDSELECT are performed on each record from the selected set. The loop ends either when the program has handled the entire set or the program encounters a BREAK command.
In the case of an error, the program executes the SELECTERROR part. A CONTINUE statement in the SELECTERROR part causes the next record to be processed. If there is no SELECTERROR section, the program generates a BREAK as the default action. Note that errors are returned only if the shell variable ERROR.BYPASS = 1 by calling [db.set.error.bypass.on()](../functions_db_operations/db.set.error.bypass.on.md).
The SELECTEOS part is executed after the SELECTDO of the last selected record. The intention of the SELECTEOS part is that before the program encounters a 'break' from the loop you can give a [commit.transaction()](../functions_db_operations/commit.transaction.md), while a *commit.transaction()* may cause a retry. If a *commit.transaction()*, given after the ENDSELECT part, causes a retry, then the whole query must be regenerated.
If the SELECTDO part is suppressed, the program encounters a 'break' from the loop after the first selected record. If the SELECTDO part is suppressed but the SELECTEOS part occurs, the program will select the whole set of records.
In order to bind pseudo variables, the functions SELECTBIND and WHEREBIND have been added. Pseudo variables have the form ':<number>'. A special bind function is then used to link a program variable to the pseudo variable. For example:
```

SELECT ppmod123.field1:5, ppmod123.field2:6
SELECTBIND(5, my_val1)
SELECTBIND(6, my_val2)
SELECTDO
                ....
ENDSELECT
```
This is equal to 'SELECT ppmod123.field1:my_val1', but using a bind function.
It is also possible to use a pseudo variable in the WHERE clause. The WHEREBIND function is then used to link a value to the pseudo variable. For example:
```

SELECT ....
WHERE ppmod123.field1 = :1
WHEREBIND(1, 10 + sqrt(a+b))
SELECTDO
       ....
ENDSELECT
```
Used BAAN 4GL variables (with ':') are 'bound' automatically.
The optional annotation `@sql.statement(cSqlAnnotation_SelectAllDataLanguages)` enforces for the annotated query that the value of multi language fields is retrieved in all data languages, independent of the setting of [resource](../misc/bshell_resources.md) *mle_all_data_languages*. This annotation is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2140](../tiv/tiv_2140.md).

## Multi Language Data
By default, for multi language columns, execution of the embedded query retrieves all data languages from the database.
If the [resource](../misc/bshell_resources.md) *mle_all_data_languages* has the value 0, then the default behavior is to retrieve only the current data language.
The [select.all.data.languages](../functions_dynamic_sql_queries/sql.set.select.all.data.languages.md) flag can be used to enforce that the value of multi language fields is retrieved in all data languages, independent of the setting of [resource](../misc/bshell_resources.md) *mle_all_data_languages*.
Also, the annotation `cSqlAnnotation_SelectAllDataLanguages` enforces that the value of multi language fields is retrieved in all data languages.
For tables which are configured for selection of all languages of its multi language fields (see the *mle_all_data_languages* argument for function [rdi.table()](../functions_runtime_dictionary_information/rdi.table.md)), execution of the query always retrieves all data languages.

## Example
```

table   tppmod090
long    total, m_val
m_val = 25
SELECT ppmod090.fld1, count(*):1
FROM ppmod090, ppmod091
WHERE ppmod090.fld2 = ppmod091.fld5 AND
                ppmod091.fld3 > :m_val
GROUP BY ppmod090.fld1
ORDER BY 2
SELECTBIND(1,total)
SELECTDO
                print_info(ppmod090.fld1, total)
SELECTERROR
                message("Error %d occurred", db.error)
                break
ENDSELECT
```
See [Dynamic SQL](dynamic_sql.md) for an example of the same query executed using dynamic SQL.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
