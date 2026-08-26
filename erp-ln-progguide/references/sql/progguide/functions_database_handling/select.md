# SELECT clause
The SELECT clause specifies a table that is the result of applying the expressions in it to the input table. The input table may be a grouped table, but the result table is never a grouped table. The SELECT clause specifies which columns must be selected and which functions must be applied to the columns. It operates on the table that is the result of the FROM clause, after applying the optional WHERE clause, the optional GROUP BY clause and the optional HAVING clause.

## Syntax
```

<select clause>
    ::= SELECT [<set quantifier>] <select list>

<set quantifier>
    ::= DISTINCT | ALL

<select list>
    ::= *
      | <select item> {, <select item> }...

<select item>
    ::= <qualifier>.*
      | Value expression [ [AS] <alias name>]
      | <array column reference> [ [AS] <alias name>]

<array column reference>
    ::= Column reference

<qualifier>
    ::= <table name>
      | <correlation name>

<table name>
    ::= !! a valid table name

<correlation name>
    ::= Identifier

<alias name>
    ::= Identifier
```
**

## Syntactical restrictions
If the SELECT clause operates on a grouped table then any [column reference](column_reference.md) contained in the *<value expression>* shall reference a grouping column, unless the [column reference](column_reference.md) is contained in a [set function specification](set_function_specification.md).
The following example is *not* correct, because *salary* is not a grouping column.
```

SELECT salary
FROM dbtst120
GROUP BY edlevel
```
The following example *is* correct, because *edlevel* is a grouping column.
```

SELECT edlevel, AVG( salary )
FROM dbtst120
GROUP BY edlevel
```
*Note:* if the SELECT clause contains a *set function specification* and the SELECT statement does not contain a GROUP BY clause then the table it operates on is regarded as a grouped table, containing a single group containing all rows of the table.
For example, the following SELECT statement returns the avarage salary of *all* employees.
```

SELECT AVG( salary )
FROM dbtst120
```

## Semantics
If *<set quantifier>* is not specified, then ALL is implicit. If the *<set quantifier>* DISTINCT is specified, then any redundant duplicate rows are eliminated from the result.
The *<select list>* "*" expands to all columns of the table on which the SELECT clause operates, preserving the order of the columns.
In the following example "*" expands to " *a.deptno*, *a.deptname*, *a.mgrno*, *a.location*, *a.admrdept*, *a.company_nr* ", *dbtst120.empno* and all other columns of *dbtst120*.
```

SELECT *
FROM dbtst100 a, dbtst120
```
The *<select item>* "<qualifier>.*" expands to all columns of the table whose qualifier equals *<qualifier>* (see qualified column name). The order of the columns is preserved.
In the following example "a.*" expands to " *a.deptno*, *a.deptname*, *a.mgrno*, *a.location*, *a.admrdept*, *a.company_nr* ", The expansion of "a.*" does *not* include any columns with qualifier *dbtst120*.
```

SELECT a.*
FROM dbtst100 a, dbtst120
```

## Related topics
- [FROM clause](from.md)
- [GROUP BY clause](group_by.md)
- [Value expression](value_expression.md)
- [Infor Enterprise Server SQL](baan_sql.md)
