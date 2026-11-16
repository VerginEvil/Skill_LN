# Dynamic SQL
Dynamic SQL enables a program to form an SQL statement during execution, so that the contents of the statement can be determined, for example, by user input.

## Functions
To use Dynamic SQL, the following functions are available:
| | |
|---|---|
| Functions | Description |
| [sql.set.select.all.data.languages()](../functions_dynamic_sql_queries/sql.set.select.all.data.languages.md) | This sets the value of the `select.all.data.languages` flag. |
| [sql.get.select.all.data.languages()](../functions_dynamic_sql_queries/sql.get.select.all.data.languages.md) | This retrieves the value of the `select.all.data.languages` flag. |
| [sql.parse()](../functions_dynamic_sql_queries/sql.parse.md) | Query definition and optional annotation with `cSqlAnnotation_SelectAllDataLanguages` |
| [sql.set.rds.full()](../functions_dynamic_sql_queries/sql.set.rds.full.md) | This sets the size of the RDBMS buffer. |
| [sql.select.bind()](../functions_dynamic_sql_queries/sql.select.bind.md) [sql.where.bind()](../functions_dynamic_sql_queries/sql.where.bind.md) | These functions link program variables to the query's pseudo variable. In Dynamic SQL, all non-external program variables used in the query must be linked to a pseudo variable with these functions. |
| [sql.exec()](../functions_dynamic_sql_queries/sql.exec.md) | This function initializes the query. It gives the variables their proper values. |
| [sql.fetch()](../functions_dynamic_sql_queries/sql.fetch.md) | This function executes the query. It reads one result on which operations can be performed. This function must be invoked for each separate record from the selected set. |
| [sql.break()](../functions_dynamic_sql_queries/sql.break.md) | Stops execution of the query. Any interim results are cleared. |
| [sql.close()](../functions_dynamic_sql_queries/sql.close.md) | Deletes (all) internal information belonging to this query. |
See the [Dynamic SQL](dynamic_sql.md) for more information and a description of the syntax of these functions.

## Sequence of actions
By using these functions a query, once defined, can be reused optimally. The sequence of the actions is then:
```

sql.parse, sql.bind, sql.exec, sql.fetch, sql.fetch, ..., sql.break
           sql.bind, sql.exec, sql.fetch, sql.fetch, ..., sql.break, sql.close
```
In this way you can prevent expensive *sql.parse()* calls, while still working with new arguments.
This flow is automatically generated from an embedded SQL program by bic6.2. Usually, the programmer will therefore opt for embedded SQL, the more so, since it automatically binds 4GL variables.

## Example
```

table           tppmod090
long            sql
long            total, m_val
m_val = 25
if ( not sql ) then
        sql = sql.parse(
                "select ppmod090.fld1, count(*):1 " &
                "from ppmod090, ppmod091 " &
                "where ppmod090.fld2 = ppmod091.fld5 AND " &
                                        "ppmod091.fld3 > :2 " &
                "group by ppmod090.fld1 " &
                "order by 2")
	if (sql = 0) then
		| handle error here
	endif
	sql.select.bind(sql, 1, total)
	sql.where.bind(sql, 2, m_val)
endif
sql.exec(sql)
while ( true )
        on case ( sql.fetch(sql) )
                case eendfile:
                        break
                case 0:
                        print_info(ppmod090.fld1, total)
                        continue
                default:                                | error
                        message("Error %d occurred", db.error)
                endcase
                break
endwhile
sql.break(sql)
sql.close(sql)          | After sql.close, a new sql.parse must be
sql  = 0                | executed to give sql a correct value. If the
                        | last two lines are skipped, sql retains a
                        | correct value.
```
See [Embedded SQL](embedded_sql.md) for an example of the same query executed using embedded SQL.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
