# SQL glossary
The number of objects in that collection. Those objects need not necessarily be distinct values.
A correlated subquery is a subquery that contains an outer column reference.
For example, the subquery "select * from dbtst120 where emnpo = employee.empno" is correlated because it constains the outer column reference "employee.empno".
The degree of a table is the number of columns of that table. An array column counts as one column. The company_nr column also counts as one column.
A grouped query is a query that has an explicit GROUP BY clause or that has a set function specification (aggregate function) in the SELECT clause.
A grouped table is a set of groups derived during evaluation of the [GROUP BY clause](group_by.md). A group of the grouped table is a multiset of rows. If for any two rows of the grouped table, the values of the grouping columns are identical or are both NULL, then the rows are in the same group. Otherwise, the rows are in different groups.
A column reference specified in the [GROUP BY clause](group_by.md).
Possibly differing between SQL-implementations, but specified by the implementor for each particular SQL-implementation.
An *outer column reference* is a column reference that references a table that is defined outside the current subquery.
For example, in the subquery "select * from dbtst120 where emnpo = employee.empno" the column reference "employee.empno" is an outer column reference.
A qualified column name is a column name with a qualifier. The qualifier is either a table name or an alias (correlation name). A column name without a qualifier is called an *unqualified* column name.
For example, "dbtst120.empno" and "a.firstnme" are qualified column names, with qualifiers "dbtst120" and "a" respectively.
All except one of any multiset of duplicate values.
Really means *undefined*. No assumption can be made about what is being undefined. For example, if the documentation says "the order of the rows if *undefined* ", then really no assumption can be made about the actual order in which the rows are.
