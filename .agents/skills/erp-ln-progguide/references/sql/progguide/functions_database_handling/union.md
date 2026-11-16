# UNION operator
The UNION operator joins the result sets of two SELECT statements. If the ALL keyword is *not* specified then all [redundant duplicates](sql_glossary.md#RedundantDuplicates) are removed from the resulting row set. The order in which the rows of the two row sets are joined is [undefined](sql_glossary.md#Undefined). If needed the order of the complete row set can be defined as usual by using an ORDER BY clause in the containing statement.

## Syntax
```

<UNION operator>
    ::= <query expression> UNION [ALL] <query expression>
```

## Syntactical restrictions
*Degree*
The two *<**query expressions**>* must have the same [degree](sql_glossary.md#Degree). If this restriction is not met, the following parse error is given:
```
SQLState 42I71: Queries in UNION have different number of result columns
```
*Comparable data types*
The data types of every corresponding column must be [comparable](comparable_datatypes.md). If this restriction is not met, the following parse error is given:
```
SQLState 42T21: Incompatible types for UNION column <n>
```

## Semantics
*Data type of result columns*
The data type of a result column of a UNION statement is the smallest data type in which fits all values of the data types of the corresponding columns of the two branches.
*Example*: The data type of the output column of the following query is *integer*, because both columns of the SELECT statements have type *integer*. There exists another type that can hold all values of type *integer*: type *real*, but of these two types *integer* is the smallest.
```
SELECT empno FROM dbtst120 a
UNION ALL
SELECT empno FROM dbtst120 b
```
*Example*: The data type of the output column of the following query is *real*, because this is the smallest data type that can hold all values of type *integer* and *real*.
```
SELECT empno FROM dbtst120 a
UNION ALL
SELECT salary FROM dbtst120 b
```
*Example*: The data type of the output column of the following query is *string of length 20*, because this is the smallest data type that can hold all values of type *string of length 6* ( `dbtst120.workdept`) and *string of length 20* ( `dbtst120.firstnme`).
```
SELECT workdept FROM dbtst120 a
UNION ALL
SELECT firstnme FROM dbtst120 b
```
*Note*: To make columns of type *string* of the same length, *space-padding* is used. So, each work department is padded with 14 spaces in the UNION above.
*Note*: To make columns of type *raw* of the same length, *zero-padding* is used.
*Name of result columns*
If the [unqualified column names](sql_glossary.md#QualifiedColumnName) of two corresponding columns are the same, then the name of the result column is this name. Otherwise the name of the result column is an [implementation defined](sql_glossary.md#ImplementationDefined) name, which is not visible outside this UNION.
*Example*: The output column name of the following query is "empno", because both output columns have the unqualified column name "empno". Notice that the qualified column names actually are different.
```
SELECT empno FROM dbtst120 a
UNION ALL
SELECT empno FROM dbtst180 b
```
*Example*: The output column name of the following query is *implementation defined*, because the unqualified column name of the first SELECT statement is "edlevel", while the unqualified column name of the second SELECT statement is "empno".
```
SELECT a.edlevel FROM dbtst120 a
UNION ALL
SELECT b.empno FROM dbtst120 b
```
*Note*: the name and visibility of the columns of a UNION is important when using an ORDER BY clause. If the ORDER BY references columns of the UNION *by name* then the name must match the columns name and the column must be visible.

## Examples
The following example joins the first names of all employees with a salary bigger than 50000 with the first names of all employees with a bonus less than 350.
```

SELECT firstnme FROM dbtst120 WHERE bonus < 350
UNION ALL
SELECT firstnme FROM dbtst120 where salary > 50000
```
The following example joins the department number and the last name of the responsible manager of all departments, with the project number and the last name of the responsible manager of all projects.
```

SELECT deptno, lastname FROM dbtst100, dbtst120
WHERE mgrno REFERS TO dbtst120.empno
UNION ALL
SELECT projno, lastname  FROM dbtst160, dbtst120
WHERE respemp REFERS TO dbtst120.empno
```
The following example joins the employee number and salary of each employee having a bonus bigger than 950, with the education level and average salary of all employees. The result is sorted in descending order on the second column of the UNION.
```

SELECT empno, salary
FROM dbtst120
WHERE bonus > 950

UNION ALL

SELECT edlevel, avg( salary )
FROM dbtst120
GROUP BY edlevel

ORDER BY 2 DESC
```
Note that it is not possible to sort on the column *by name*. This would also be true for the first column of the UNION, because the column names in the individual SELECT statements are different. See the section Semantics above.
The following example joins the names of all employees in companies 000 and 001 having a salary bigger than 40000. The result is sorted by company.
```

SELECT company_nr, firstnme, lastname
FROM   dbtst120
WHERE  salary > 40000
AND    company_nr = 000

UNION ALL

SELECT company_nr, firstnme, lastname
FROM   dbtst120
WHERE  salary > 40000
AND    company_nr = 001

ORDER BY company_nr
```
Note that in this case it is possible to sort *by name*, since both SELECT statements share the column name for the first column.

## Related topics
- [Comparable data types in Infor Enterprise Server SQL](comparable_datatypes.md)

- [Infor Enterprise Server SQL](baan_sql.md)
