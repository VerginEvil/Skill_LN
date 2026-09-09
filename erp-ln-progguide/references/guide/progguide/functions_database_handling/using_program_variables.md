# Using program variables
To use SQL statements in the Baan programming language it is needed to transfer data from program variables to SQL statement variables and to transfer output of SQL statements to program variables.
The transfer of data to SQL statement variables takes place before or during *execution* time (if you use dynamic SQL this is before or during the sql.exec() call). The *execution* of the SQL statement freezes all statement variables. So, a call to sql.where.bind() after a call to sql.exec() will not take effect until the next call to sql.exec().
Each time a row is fetched from the SQL statement, the values of the columns are copied to the corresponding *select targets*. The *select targets* are explicitly defined using sql.select.bind() calls or SELECTBIND() statements or are implicitly defined during *execution* time.

## Binding of input values to SQL statement variables
To evaluate a SQL statement containing variables, the query processor must retrieve the values of these variables from the application.
There are two ways to bind values to the variables of a SQL statement:

- *Using pseudo variables* Pseudo variables take the form ": *<**number**>* ". The value of a pseudo variable must be *explicitly* defined by either using the [sql.where.bind()](../functions_dynamic_sql_queries/sql.where.bind.md) call or by using the WHEREBIND() statement (see [Embedded SQL](embedded_sql.md)). If a pseudo variable is not bound before *execution* of the statement the following runtime error is given: SQLState HYL03: Pseudo variable '<number>' not bound before sql_exec.

- *Using program variables* Program variables take the form ": *<**program variable name**>* ". The values of the program variable are automatically loaded into the query processor.When using *dynamic SQL* the program variable must be declared *extern*. If a program variable does not exist then the following runtime error is given: SQLState HYL04: External variable '<program variable name>' not found. When using *embedded SQL* the program can be declared local to the function in which the SQL statement is defined. If a program variable does not exist then the following compile time error is given: SQL host variable ':<program variable name>' not declared.

*Note*: Binding of input values is *by value*, not *by reference*. When using dynamic SQL this means that a SQL statement variable keeps its value until another `sql.where.bind()` call is done.

## Binding of output columns to program variables
The query processor stores the result of a query into program variables. In order to do so, it must know the relation between each output column of the query and a program variable. Each program variable that is used to store a result is called a *select target*.
There are three ways to define the *select target* of an output column:

- *Using pseudo variables* *Syntax*: `select firstnme:<number>` The pseudo variable must be *explicitly* bound to a *select target* by either using the [sql.select.bind()](../functions_dynamic_sql_queries/sql.select.bind.md) call or by using the SELECTBIND() statement (see [Embedded SQL](embedded_sql.md)).If a pseudo variable is not bound before *execution* of the statement the following runtime error is given: SQLState HYL03: Pseudo variable '<number>' not bound before sql_exec.

- *Using program variables* *Syntax*: `select firstnme:<program variable name>` The output column is automatically bound to the program variable.When using *dynamic SQL* the program variable must be declared *extern*. If a program variable does not exist then the following runtime error is given: SQLState HYL04: External variable '<program variable name>' not found. When using *embedded SQL* the program can be declared local to the function in which the SQL statement is defined. If a program variable does not exist then the following compile time error is given: SQL host variable ':<name>' not declared.

- *Using the implicitly derived select target* *Syntax*: `select firstnme` This case behaves the same as the "Using program variables" case above, except for the fact that the <program variable name> is derived from the SQL statement by the query processor (see below).

For each row that is fetched from the SQL statement, all values of the output columns are copied into the *select targets*.

## Implicitly derived select targets
If an output column of a SQL statement is not explicitly bound to a select target, then the query processor uses the derived select target. If there is no derived select target then the following error is given:
SQLState HYL06: select item <number> must be bound explicitly.
The query processor defines a derived select target for an output column, if it is a column name. The name of the select target is the qualified column name of the column in the related table.
*Example*: The following query defines "dbtst120.empno" as the select target for the first column, and "dbtst120.firstnme" for the second column. It does *not* define " *alias*.empno" as a select target.
```

SELECT alias.empno, firstnme FROM dbtst120 alias
```
For all other output columns, such as aggregate functions, no select target is defined.
*Example*: The following query defines *no* select target for the second column.
```

SELECT edlevel, avg(salary) FROM dbtst120 alias
```
In case of a UNION, the SELECT in the first branch of the UNION defines the name of the select target.
*Example*: The following query defines "dbtst120.empno" as the select target for the first column, and "dbtst120.bonus" for the second column.
```

SELECT empno, bonus
FROM dbtst120 alias

UNION ALL

SELECT edlevel, avg(salary)
FROM dbtst120
```
*Example*: The following query defines "dbtst120.empno" as the select target. Note that "dbtst180.empno" is *not* a select target.
```

SELECT empno
FROM dbtst120

UNION ALL

SELECT empno
FROM dbtst180
```
A subquery does not define any select targets.
*Example*: The following query defines "dbtst120.empno" as the select target. Note that "dbtst180.empno" is *not* a select target.
```

SELECT empno
FROM dbtst120 a
WHERE EXISTS (
     SELECT projno
     FROM dbtst180 s
     WHERE s.empno = a.empno
      )
```
Note  A table field can be a program variable as well as a query variable. Note that the following query:
```

SELECT tccom010.*
WHERE tccom010.cuno = tccom010.cuno
```
has a different result from:
```

SELECT tccom010.*
WHERE tccom010.cuno = :tccom010.cuno
```
The latter selects one record; the former selects all records from the table tccom010, as tccom010.cuno by definition equals tccom010.cuno for each row.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
