# REFERS TO predicate
A REFERS TO predicate determines how the tables in the FROM clause are joined.
*Note:* In [ANSI mode](../functions_dynamic_sql_queries/sql.parse.md) the REFERS TO predicate is not allowed. Rather than that, use an [OUTER JOIN](from.md).

## Syntax
```

<refers to predicate>
    ::= <row value constructor> REFERS TO <to> [ PATH <ref path> ] [ UNREF <unref mode> ]

<to>
    ::= <table name>
      | <correlation name>
      | !! qualified column name

<ref path>
    ::= <path element> { , <path element> }...

<path element>
    ::= <table name>.<column name>

<table name>
    ::= !! a valid table name

<column name>
    ::= !! a valid column name

<correlation name>
    ::= <identifier>

<unref mode>
    ::= CLEAR | SETUNREF | CLEARUNREF | SKIP
```

## Syntactical restrictions
The REFERS TO predicate generates a [syntax error](../sql_states_and_messages/42I82.md) when the *PARSE.ANSI* flag is set in the optional *mode* argument of the [sql.parse()](../functions_dynamic_sql_queries/sql.parse.md) function.
*I.* The *<**row value constructor**>* shall either directly contain column references of one table only or directly contain constants or parameters only.
In the following example the *<**row value constructor**>* contains both a constant and a column reference, which is not allowed.
```

{ 10, dbtst120.deptno } REFERS TO dbtst180
```
In the following example the *<**row value constructor**>* contains column references of two tables, which is not allowed.
```

{ a.empno, b.deptno } REFERS TO dbtst180
```
In the following example the *<**row value constructor**>* contains an expression, which is not allowed.
```

{ 10+3 } REFERS TO dbtst120
```
*II.* A SELECT statement shall not contain a series of REFERS TO predicates that together define a cyclic relationship between the tables that refer to each other.
The following example shows two REFERS TO predicates that define a cyclic dependency between tables a and b.
```

a.empno REFERS TO b AND b.deptno REFERS TO a.workdept
```
*III.* Within a SELECT statement, there shall be no two REFERS TO predicates referring to the same table and of which the *<**row value constructor**>**s* contain column references of different tables.
```

a.empno REFERS TO c AND b.empno REFERS TO c
```

## Examples
The following statement gives all departments and for each department it gives all last names of the employees working in that department. If there are no employees working in a certain department then it still gives the department name, but it gives a NULL value for the lastname.
```

SELECT workdepts.deptname, employees.lastname
FROM dbtst100 workdepts, dbtst120 employees
WHERE workdepts.deptno REFERS TO employees.workdept
```
The following statement gives all project names and for each project it gives the last names of the employees working on that project.
```

SELECT projects.projname, employees.lastname
FROM dbtst180 projemp, dbtst160 projects, dbtst120 employees
WHERE projemp.projno REFERS TO projects
  AND projemp.empno REFERS TO employees
ORDER BY projname
```

## Semantics
The REFERS TO predicate always evaluates to True.
The REFERS TO predicate defines an outer join with a join condition between two tables in the FROM clause. If the REFERS TO predicate is as follows:
```

<row value constructor> REFERS TO <column reference>
```
then the following join condition is defined:
```

<row value constructor> = <column reference>
```
Suppose the *<**row value constructor**>* contains column references to table A and the column reference identifies table B.
The result of the (inner) join of the tables A and B is the Cartesian product of the two tables with each row that does not satisfy the join condition filtered out.
The REFERS TO predicate extends this result by adding each row of table A that does not occur in the result of the (inner) join. For each row of table A that is added, NULL values are generated on table B.
For example, suppose table A has one column AC and table B has two columns BC1 and BC2. See table A and table B below. Suppose that the REFERS TO predicate is "A.AC REFERS TO B.BC1". Then the Cartesian product (table A × B) contains each row of A combined with each row of B. The inner join (table A = B) filters any row from the Cartesian product that does not satisfy the condition "A.AC = B.BC1". The REFERS TO predicate (table A → B) adds those rows from A that are not in the inner join result and generates NULLs for B.
| |
|---|
| A |
| AC |
| 1 |
| 2 |
| 3 |
| | |
|---|---|
| B |  |
| BC1 | BC2 |
| 1 | a |
| 2 | b |
| 2 | c |
| | | |
|---|---|---|
| A × B |  |  |
| AC | BC1 | BC2 |
| 1 | 1 | a |
| 1 | 2 | b |
| 1 | 2 | c |
| 2 | 1 | a |
| 2 | 2 | b |
| 2 | 2 | c |
| 3 | 1 | a |
| 3 | 2 | b |
| 3 | 2 | c |
| | | |
|---|---|---|
| A = B |  |  |
| AC | BC1 | BC2 |
| 1 | 1 | a |
| 2 | 2 | b |
| 2 | 2 | c |
| | | |
|---|---|---|
| A → B |  |  |
| AC | BC1 | BC2 |
| 1 | 1 | a |
| 2 | 2 | b |
| 2 | 2 | c |
| 3 | NULL | NULL |

## Equivalences
The following equivalence states that the part "._index1" is optional in the <to> part.
```

T1.f1 REFERS TO T2   ⟺   T1.f1 REFERS TO T2._index1
```
The following equivalence holds for a REFERS TO predicate with the PATH clause. It states that we can rewrite a REFERS TO predicate with a PATH clause into multiple REFERS TO predicates without PATH clauses. Each table in the PATH clause is effectively added to the FROM clause, getting a unique alias.
```

FROM   T1, Tn
WHERE  T1.f1 REFERS TO Tn PATH T2.f2, ...
               ⟺
FROM   T1, Tn, T2 <alias T2>
WHERE  T1 REFERS TO <alias T2>  AND  <alias T2>.f2 REFERS TO Tn PATH ...
```
If a REFERS TO predicate with a PATH clause also contains an UNREF mode, then this UNREF mode holds for each of the REFERS TO predicates without the PATH clause.
*Note:* tables mentioned in the PATH clause of a REFERS TO predicate do not necessarily need to appear in the FROM clause of a SELECT statement. The following fragment is syntactically correct, even though table T2 does not appear in the FROM clause.
```

FROM T1, T3
WHERE T1.f1 REFERS TO T3 PATH T2.f2
```
It is equivalent to the following fragment.
```

FROM T1, T3, T2 alias_T2
WHERE T1.f1 REFERS TO alias_T2 AND alias_T2.f2 REFERS TO T3
```
The following fragment is syntactically correct too, but is semantically different from the previous fragments.
```

FROM T1, T2, T3
WHERE T1.f1 REFERS TO T3 PATH T2.f2
```
It is equivalent to the following fragment. Note that table T2 appears twice now in the FROM clause.
```

FROM T1, T2, T3, T2 alias_T2
WHERE T1.f1 REFERS TO alias_T2 AND alias_T2.f2 REFERS TO T3
```

## Implicit UNREF mode
If a REFERS TO predicate does not contain an UNREF mode, then the query processor defines an implicit UNREF mode for the predicate. If there exists a reference in the data dictionary that "matches" with the REFERS TO predicate then the following table is used to determine the implicit UNREF mode. If there is no such reference then the implicit UNREF mode becomes SETUNREF.
| | |
|---|---|
| Mode in data dictionary | Implicit Unref mode |
| Compulsory | SETUNREF |
| Compulsory unless empty | CLEARUNREF |
| Not compulsory | CLEAR |

## Related topics
- [FROM clause](from.md)

- [Infor Enterprise Server SQL](baan_sql.md)
