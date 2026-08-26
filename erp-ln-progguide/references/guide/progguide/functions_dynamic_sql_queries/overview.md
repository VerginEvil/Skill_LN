# Dynamic SQL queries overview
Dynamic SQL enables programs to compose and execute SQL statements at runtime. This is necessary, for example, when SQL statements are composed in response to user input.
You use the functions described in this section to handle dynamic SQL queries. Use [sql.parse()](sql.parse.md) to define the query. Once the query has been defined, use the other functions to bind variables in the SQL statement to BAAN 4GL variables, to execute the query, to fetch the results, and to end and delete the query. Note that there is no need to bind external variables. Once you have defined a query using [sql.parse()](sql.parse.md), you can execute it any number of times, using different variables, without redefining it.
The sequence in which you use the functions is as follows:
```

sql.parse()
	sql.select.bind()
	sql.where.bind()
		sql.exec()
		sql.fetch()
		sql.fetch()
		...
		sql.break()

	sql.select.bind()
	sql.where.bind()
		sql.exec()
		sql.fetch()
		sql.fetch()
		...
		sql.break()
sql.close
```
For a general discussion of database handling, and embedded and dynamic SQL, see [Database handling overview](../functions_database_handling/overview.md).

## Related topics
- [Dynamic SQL queries synopsis](synopsis.md)
