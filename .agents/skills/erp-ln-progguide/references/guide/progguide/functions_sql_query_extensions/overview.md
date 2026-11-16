# SQL query extensions overview
By default, the [4GL engine](../glossary/glossary.md#fourgl_engine) reads the entire main table when retrieving data for a particular form, even though some records and fields may not be required. By default also, the [4GL engine](../glossary/glossary.md#fourgl_engine) reads only those reference table fields that are included on the form, even though the UI script and/or the DAL script may require other reference table fields.
Query extensions define conditions that the [4GL engine](../glossary/glossary.md#fourgl_engine) adds to the SELECT, FROM, and WHERE clauses of a database query in order to filter out unwanted records and fields of the main table and in order to include in the query all reference fields required by the form, UI script, and DAL script.
In the UI script, you program query extensions for 2 purposes:

- to minimize the number of records and fields of the main table read by the query

- to retrieve any reference table fields that are required by the UI script but which cannot be retrieved by the [4GL engine](../glossary/glossary.md#fourgl_engine) automatically. Note that these fields should occur on the form.

In the DAL (not DAL2, DAL2 does not support query extensions!) script, you program query extensions to retrieve reference table fields that are required by the DAL script.
When the [4GL engine](../glossary/glossary.md#fourgl_engine) executes a database query, it automatically adds the query extensions defined in UI and DAL scripts. So, in the case of main table fields, the [4GL engine](../glossary/glossary.md#fourgl_engine) reads only those fields and records that meet the conditions set in the query extension in the UI script. In the case of reference tables, the [4GL engine](../glossary/glossary.md#fourgl_engine) reads those fields included on the main table and also those mentioned in the UI and DAL scripts.

## Building DAL (not DAL2) query extensions
The purpose of DAL query extensions is to read data of other tables, at the moment the functions dal.new(), dal.update() and dal.destroy() functions are executed. This will ensure that the data is available in the property hooks.

- Identify the reference table fields required for [method.is.allowed()](../functions_dal/method.is.allowed.md).

- Identify the reference table fields required for executing checks in property and object hooks.

- Extend the DAL query in the most efficient way possible (for example, avoid using table.*). For example, define a normal query that specifies all the referenced fields/tables and then filter out unwanted fields/tables. Check the joins carefully to ensure that multiple records are not selected. Then split the query into strings appropriate for input to the *query.extend.** functions.

- Because the query must return the most recent values for reference table fields, you must use the buffered values for the fields. To do this, append a colon [:] to properties of the current class that are used in the *query.extend.where()* function.

- Normally, you specify EXTEND_OVERWRITE as the mode for the *query.extend.** functions. Use EXTEND_APPEND only when you want to further extend a query that has already been extended.

## Building UI query extensions
The purpose of UI query extensions is twofold: to read data of other tables in order to be able to display this data on the form and to filter data that is been displayed on the form.

- Identify the reference table fields that are used in the UI script but which cannot be retrieved by the [4GL engine](../glossary/glossary.md#fourgl_engine) automatically.

- Eliminate any fields that have been included in the DAL query extension of the main table.

- Identify the conditions required for filtering the data.

- Identify the form fields and external variables that require table values and bind the form fields to the table fields.

- Construct the query extension in the most efficient way possible. When dealing with non-zoom sessions, program the query extension in the *before.program* section. When dealing with zoom sessions, program the query extension in the *selection.filter* section. Note that, for zoom sessions, you use query extensions only for filtering out unwanted data from the main table.

- Normally, you specify EXTEND_OVERWRITE as the mode for the *query.extend.** functions. Use EXTEND_APPEND only when you want to extend further a query that has already been extended.

Note  When you use the EXTEND_OVERWRITE or EXTEND_APPEND options, be aware that these options only apply to query extensions that are defined in the script in which they are used. It is not possible to overwrite the query extension defined in the DAL by a query extension in the UI script.
To make this clear:

- EXTEND_OVERWRITE in DAL: this will define a new query extension for the DAL which overwrites any previous DAL query extension.

- EXTEND_APPEND in DAL: this will append a query extension to the already existing query extension in the DAL.

- EXTEND_OVERWRITE in UI: this will define a new query extension for the UI, and will not overwrite any extension defined in the DAL.

- EXTEND_APPEND in UI: this will append a query extension to the already existing query extension in the UI.

The [4GL engine](../glossary/glossary.md#fourgl_engine) will always append the query extensions defined in the DAL and UI scripts to the main table query.

## Related topics
- [SQL query extensions synopsis](synopsis.md)

- [Column filtering](column_filtering.md)

- [Query extensions sample program](example.md)

- [quoted.string()](../functions_string_operations/quoted.string.md)
