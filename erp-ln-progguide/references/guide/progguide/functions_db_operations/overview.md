# Database operations overview
Use these functions for handling database input and output.

## New features in Infor Enterprise Server
In Infor Enterprise Server, the functions [db.curr()](db.curr.md), [db.first()](db.first.md), [db.last()](db.last.md), [db.next()](db.next.md), [db.prev()](db.prev.md), [db.gt()](db.gt.md), [db.ge()](db.ge.md), [db.lt()](db.lt.md), and [db.le()](db.le.md) are implemented internally as SELECT statements. They are supported for backward compatibility only. In new applications, use queries instead.
In Infor Enterprise Server, certain 4GL functions have Data Access Layer (DAL) equivalents. The following table lists these functions and their DAL equivalents.
| | |
|---|---|
| 4GL function | DAL function |
| on.main.table() | with.object.set.do() |
| on.old.occ() | with.old.object.values.do() |
| set.input.error() |  dal.set.error.message() return(DALHOOKERROR)  |
| skip.io() |  dal.set.error.message() return(DALHOOKERROR)  |
| abort.io() |  dal.set.error.message() return(DALHOOKERROR)  |
| db.update() | dal.update() |
| db.delete() | dal.destroy() |
| db.insert() | dal.new() |
If a DAL exists for a particular table, it is preferable to use the DAL functions. The older functions access the database directly. When you make changes to the database with these functions, logic integrity checks programmed in the DAL are not executed. When you make changes to the database with the DAL functions, the relevant DAL hooks are executed automatically. This ensures the logic integrity of the database.
For further information about database handling in general and about the Data Access Layer, see [Database handling overview](../functions_database_handling/overview.md) and [Data Access Layer](../functions_dal/overview.md).

## Table names and declarations
The naming syntax for tables, record buffers, and fields is:
```

table tppmmmxxx        | table declaration
rcd.tppmmmxxx          | record buffer of table
ppmmmxxx.ffffffff      | logical field of table
```
where t stands for table, `pp` is the package code, mmm is the module code, `xxx` is the table number, and `ffffffff` is a field name.
If a table is used in a script, it must be declared with the statement: `table tppmmmxxx`
Declaration of a table implies declaration of all its fields and its record buffer. These do not need to be declared separately.
There are no functions for opening or closing a table. A table is automatically opened the first time it is accessed. It is automatically closed when the program ends.

## Multi Language Data
By default, for multi language columns, the functions [db.eq()](db.eq.md), [db.curr()](db.curr.md), [db.first()](db.first.md), [db.last()](db.last.md), [db.next()](db.next.md), [db.prev()](db.prev.md), [db.gt()](db.gt.md), [db.ge()](db.ge.md), [db.lt()](db.lt.md), and [db.le()](db.le.md) retrieve all data languages from the database.
If the [resource](../misc/bshell_resources.md) *mle_all_data_languages* has the value 0, then the default behavior is to retrieve only the current data language.
For tables which are configured for selection of all languages of its multi language fields (see the *mle_all_data_languages* argument for function [rdi.table()](../functions_runtime_dictionary_information/rdi.table.md)), these functions always retrieve all data languages, independent of the setting of [resource](../misc/bshell_resources.md) *mle_all_data_languages*.
Furthermore, when such a function applies a lock to the selected record, also all data languages are retrieved for the multi language columns of the locked record.
Finally, the [select.all.data.languages](../functions_dynamic_sql_queries/sql.set.select.all.data.languages.md) flag can be used to enforce that all data languages are retrieved for multi language columns.
For these functions, there is no way to apply the annotation `cSqlAnnotation_SelectAllDataLanguages` to override the default behavior. Remember: these functions are more or less deprecated and are supported for backward compatibility only. In new applications, use [Infor Enterprise Server SQL](../functions_database_handling/baan_sql.md) instead.

## Error handling
In Infor Enterprise Server, there are two main categories of errors: operating system errors and database system errors. For an explanation of the error codes, consult your operating system or database system documentation, or see [Infor ES errors and messages](../errors/overview.md).
Normally, a program can detect only four of the database errors: EDUPL, EENDFILE, ENOREC, and EROWCHANGED. When other errors occur, an error message is displayed on screen. However, you can call the function [db.set.error.bypass.on()](db.set.error.bypass.on.md) to set the predefined variable *error.bypass* to suppress error messages and enable a program to detect some or all errors instead. This variable can have the following values:
| | |
|---|---|
| false |  This is the default value. The program can detect the following database errors: EDUPL, EENDFILE, ENOREC, and EROWCHANGED. Some fatal errors cause a direct abort of the application. When this happens, the message 'Cannot continue' is displayed. If you attempt to lock a record or table that is already locked by another process, the program returns to the retry point automatically a number of times (by default, 10 times) before stopping the session and displaying the error message.  |
| true | The program can detect all errors, except those listed below. If the error can be detected no database error messages are displayed on screen, and the application must handle the error.  |
A program can detect database errors in the following ways:
- Test return values. For example: `if db.insert( tpctst999 ) = EENDFILE then ...`
- Use [db.error()](db.error.md). For example: `db.insert( tpctst999 ) if db.error( tpctst999 ) = EENDFILE then ...`
- Use the predefined variable *e*. For example: `db.insert( tpctst999 ) if e = EENDFILE then ...`
- The ENDSELECT and SELECTEMPTY statements automatically detect the EENDFILE and ENOREC errors respectively.

## Related topics
- [Database operations synopsis](synopsis.md)
