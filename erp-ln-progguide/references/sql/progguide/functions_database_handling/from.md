# FROM clause
The FROM clause specifies a table derived from one or more tables. It forms the basis row set for the WHERE clause, GROUP BY clause, HAVING clause and SELECT clause.

## Syntax
```

<from clause>
    ::= FROM <table reference> [{, <table reference>}...]

<table reference>
    ::= <table name> [[AS] <correlation name>]
      | <joined table>
      | <derived table>

<joined table>
    ::= <table reference> LEFT [OUTER] JOIN <table reference>
           ON Search condition
      | <table reference> RIGHT [OUTER] JOIN <table reference>
           ON Search condition
      | <table reference> FULL [OUTER] JOIN <table reference>
           ON Search condition
      | <table reference> [INNER] JOIN <table reference>
           ON Search condition
      | ( <joined table> )

<table name>
    ::= !! a valid table name

<derived table>
    ::= ( Query expression ) [AS] <correlation name>

<correlation name>
    ::= Identifier
```
**

## Syntactical restrictions
*I.* The *<correlation name>* shall not contain a period (.).
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
The following example is incorrect, because *dbtst100* is used both as a table name and a correlation name.
```

FROM dbtst120 dbtst100, dbtst100
```

## Semantics
The FROM clause specifies a table that is the Cartesian product of all *<table reference>s* in the FROM clause.

## Examples
The following example specifies a table that has the same rows as table dbtst100 and has column names *dbtst100.deptno*, *dbtst100.deptname*, *dbtst100.mgrno*, *dbtst100.location*, *dbtst100.admrdept* and *dbtst100.company_nr*.
```

FROM dbtst100
```
The following example specifies a table that has the same rows as table dbtst100 and has column names *depts.deptno*, ...
```

FROM dbtst100 depts
```
The following example specifies a table that is the Cartesian product of table dbtst100 with itself and has column names *depts.deptno*, *depts.deptname*, ..., *admin_depts.deptno*, *admin_depts.deptname*, ...
```

FROM dbtst100 depts, dbtst100 admin_depts
```
(Note that this is not a violation of restriction II above, since both occurrences of table name dbtst100 are hidden by the correlation names.)
The following example demonstrates the use of a *derived table* and an INNER JOIN.
```
FROM ( SELECT edlevel, MAX( salary ) AS max_salary
       FROM dbtst120
       GROUP BY edlevel ) max_salary_by_edlevel
     INNER JOIN
     dbtst120 AS employees
     ON max_salary_by_edlevel.max_salary = employees.salary
```

## Related topics
- [SELECT clause](select.md)
- [Infor Enterprise Server SQL](baan_sql.md)
