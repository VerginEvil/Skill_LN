# FROM clause
The FROM clause specifies a table derived from one or more tables. It forms the basis row set for the WHERE clause, GROUP BY clause, HAVING clause and SELECT clause.

## Syntax
```

<from clause>
    ::= FROM <table reference> [ { , <table reference> }... ]

<table reference>
    ::= <table name> [ [AS] <correlation name> ] [FOR UPDATE]
      | <joined table>
      | <derived table>

<joined table>
    ::= <table reference> LEFT [OUTER] JOIN <table reference> ON <search condition>
      | <table reference> RIGHT [OUTER] JOIN <table reference> ON <search condition>
      | <table reference> FULL [OUTER] JOIN <table reference> ON <search condition>
      | <table reference> [INNER] JOIN <table reference> ON <search condition>
      | ( <joined table> )

<table name>
    ::= !! a valid table name

<derived table>
    ::= ( <query expression> ) [AS] <correlation name>

<correlation name>
    ::= <identifier>
```

## Syntactical restrictions
*I.* The *<**correlation name**>* shall not contain a period (.).
The following example is incorrect, because the correlation name *all.employees* contains a period.
```

FROM dbtst120 all.employees
```
*II.* The FROM clause shall not contain duplicate correlation names or table names without correlation names.
The following example is incorrect, because the table name *dbtst120* appears twice in the FROM clause.
```

FROM dbtst120, dbtst120
```
The following example is incorrect, because the correlation name *table* appears twice in the FROM clause.
```

FROM dbtst120 table, dbtst100 table
```
The following example is incorrect, because *dbtst100* is used both as a table name and as a correlation name.
```

FROM dbtst120 dbtst100, dbtst100
```
*III.* If a JOIN is used in the FROM clause, then no [REFERS TO predicate](refers_to_pred.md) is allowed in the [WHERE clause](where.md).

## Semantics
If the containing SELECT statement does not contain a WHERE clause that contains REFERS TO predicates, the FROM clause specifies a table that is the Cartesian product of all tables in the FROM clause. If it does contain a WHERE clause containing REFERS TO predicates, then the tables in the FROM clause are joined as described in the section on the [REFERS TO predicate](refers_to_pred.md).
If a *<**table reference**>* contains the *FOR UPDATE* keywords, then the SELECT clause of the containing SELECT statement is effectively expanded with all columns of the table and, even when the [resource](../misc/bshell_resources.md) *mle_all_data_languages* is set to value 0, the value of multi language columns is retrieved in all data languages. For example, consider the following statement.
```

SELECT edlevel
FROM dbtst120 employees FOR UPDATE
```
The above statement is equivalent with the following statement.
```

SELECT edlevel, employees.*
FROM dbtst120 employees FOR UPDATE
```

## Examples
The following example specifies a table that has the same rows as table dbtst100 and has column names *dbtst100.deptno*, *dbtst100.deptname*, *dbtst100.mgrno*, *dbtst100.location*, *dbtst100.admrdept* and *dbtst100._compnr*.
```

FROM dbtst100
```
The following example specifies a table that has the same rows as table dbtst100 and has column names *depts.deptno*,...
```

FROM dbtst100 depts
```
The following example specifies a table that is the Cartesian product of table dbtst100 with itself (unless the WHERE clause has a REFERS TO predicate on these tables, then it is an outer join) and has column names *depts.deptno*, *depts.deptname*,..., *admin_depts.deptno*, *admin_depts.deptname*,...
```

FROM dbtst100 depts, dbtst100 admin_depts
```
(Note that this is not a violation of restriction II above, since both occurrences of table name dbtst100 are hidden by the correlation names.)
The following example demonstrates the use of a *derived table* and an INNER JOIN.
```

FROM ( SELECT edlevel, MAX( salary ) AS max_salary
       FROM dbtst120
       GROUP BY edlevel
     ) max_salary_by_edlevel
INNER JOIN dbtst120 AS employees
ON max_salary_by_edlevel.max_salary = employees.salary
```

## Related topics
- [SELECT clause](select.md)

- [REFERS TO predicate](refers_to_pred.md)

- [_compnr predicate](compnr_pred.md)

- [SQL and delayed locks](sql_and_delayed_locks.md)

- [Infor Enterprise Server SQL](baan_sql.md)
