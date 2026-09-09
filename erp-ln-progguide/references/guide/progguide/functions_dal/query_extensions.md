# Query extensions
Query extensions define conditions that the [4GL engine](../glossary/glossary.md#fourgl_engine) adds to the SELECT, FROM, and/or WHERE clauses of a database query in order to minimize the number of fields read from the main table and in order to retrieve all reference table fields required by the UI and/or DAL scripts.
Infor Enterprise Server provides the following functions for constructing query extensions:

- [query.extend.select()](../functions_sql_query_extensions/query.extend.select.md)

- [query.extend.select.in.zoom()](../functions_sql_query_extensions/query.extend.select.in.zoom.md)

- [query.extend.from()](../functions_sql_query_extensions/query.extend.from.md)

- [query.extend.from.in.zoom()](../functions_sql_query_extensions/query.extend.from.in.zoom.md)

- [query.extend.where()](../functions_sql_query_extensions/query.extend.where.md)

- [query.extend.where.in.zoom()](../functions_sql_query_extensions/query.extend.where.in.zoom.md)

You can program query extensions in the UI script and/or the DAL script. In the UI script, you program the extensions in the *before.program* or *before.zoom* sections. In the DAL script, you program the extensions in the [before.open.object.set()](before.open.object.set.md) hook.
For a full discussion of query extensions, see [SQL query extensions overview](../functions_sql_query_extensions/overview.md)
Note  Using query extensions with [Extended DAL (DAL2)](dal2_overview.md) is strongly discouraged. The main reason is that this may interfere with the handling of field dependencies.

## Related topics
- [Data Access Layer](overview.md)
