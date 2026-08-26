# Infor Enterprise Server SQL
You use Infor Enterprise Server SQL (Structured Query Language) to retrieve information from the database. With Infor Enterprise Server SQL's SELECT statement, you can retrieve any selection of data from the database, regardless of the number of tables in which the data is stored. The system does search through all records sequentially. It bases its search on a number of conditions defined in the SELECT statement.
The SELECT statement does not modify the data in the database. It is used simply to query the data. Whereas only one user at a time can modify data, any number of users can query or select the data concurrently.
The SELECT statement works at the table level; the output is also a table consisting of 0, 1, or more records. If the query is very specific, the output may consist of only one record. The structure of a SELECT statement is directly derived from the table structure. It takes the following general form:
```

SELECT expressions ...
FROM table reference(s) ...
WHERE each row fulfills the condition(s) ...
```
The following sections provide information on SQL syntax and using SQL:
- [SQL reserved words](sql_reserved_words.md)
- [SQL data types](sql_data_types.md)
- [SELECT statement](select_statement.md)
- [Multi Language Data](multi_language_data.md)
- [SQL states and messages](../sql_states_and_messages/help_sql_states_and_messages.md)
- [SQL glossary](sql_glossary.md)
