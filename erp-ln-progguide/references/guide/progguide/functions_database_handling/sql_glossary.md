# SQL glossary
Cardinality (of a collection)   The number of objects in that collection. Those objects need not necessarily be distinct values.
Correlated subquery   A correlated sub query is a sub query that contains an outer column reference.
For example, the sub query "select * from dbtst120 where emnpo = employee.empno" is correlated because it constains the outer column reference "employee.empno".
Degree   The degree of a table is the number of columns that table has. In this an array column counts as 1 column. The _compnr column also counts as a column. Other pseudo columns (e.g. _index1) expand to there underlying column(s), each counting for 1 column.
Grouped query   A grouped query is a query that has an explicit GROUP BY clause or that has a set function specification (aggregate function) in the SELECT clause.
Grouped table   A grouped table is a set of groups derived during evaluation of the [GROUP BY clause](group_by.md). A group of the grouped table is a multiset of rows. If for any two rows of the grouped table, the values of the grouping columns are identical or are both NULL, then the rows are in the same group. Otherwise, the rows are in different groups.
Grouping column   A column reference specified in the [GROUP BY clause](group_by.md).
Implementation defined   Possibly differing between SQL-implementations, but specified by the implementor for each particular SQL-implementation.
Outer column reference   An *outer column reference* is a column reference that references a table that is defined outside the current sub query.
For example, in the sub query "select * from dbtst120 where emnpo = employee.empno" the column reference "employee.empno" is an outer column reference.
Qualified column name   A qualified column name is a column name with a qualifier. The qualifier is either a table name or an alias (correlation name). A column name without a qualifier is called an *unqualified* column name.
For example, "dbtst120.empno" and "a.firstnme" are qualified column names, with qualifiers "dbtst120" and "a" respectively.
Redundant duplicates   All except one of any multiset of duplicate values.
Select target   A select target is the program variable that is used to store the result value of a column of a SQL statement.
For example, in the query "select empno, firstnme :my.name from dbtst120", the select targets are "dbtst120.empno" and "my.name".
Undefined   Really means *undefined*. No assumption can be made about what is being undefined. For example, if the documentation says "the order of the rows if *undefined* ", then really no assumption can be made about the actual order in which the rows are.
