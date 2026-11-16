# sql.parse()

## Syntax:
`function long sql.parse( string query(.), [ long mode, ref string err.msg, ref long err.line, const string annotation,... ] )`

## Description
This defines an SQL query that you can subsequently execute and retrieve the results of by using the other dynamic SQL functions. The query takes the form of a SELECT statement (see [Database handling overview](../functions_database_handling/overview.md)).
The optional argument *mode* can be used to influence the behavior.

## Arguments
| | |
|---|---|
| PARSE.SUPPRESS | When this flag is set, error messages are suppressed. (the predefined variable *e* contains the error number). |
| PARSE.ANSI | When this flag is set: The [LIKE predicate](../functions_database_handling/like_pred.md) defaults to ANSI patterns rather than to regular expressions. No [REFERS TO predicate](../functions_database_handling/refers_to_pred.md) is allowed in a [WHERE clause](../functions_database_handling/where.md). Rather than that, use an [OUTER JOIN](../functions_database_handling/from.md). |

## Return values
| | |
|---|---|
| 0 | Error. |
| > 0 | Query ID; this is used by the other functions to identify the particular query. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Multi Language Data
By default, for multi language columns, execution of the parsed query retrieves all data languages from the database.
If the [resource](../misc/bshell_resources.md) *mle_all_data_languages* has the value 0, then the default behavior is to retrieve only the current data language.
The [select.all.data.languages](sql.set.select.all.data.languages.md) flag can be used to enforce for the parsed query that the value of multi language fields is retrieved in all data languages, independent of the setting of [resource](../misc/bshell_resources.md) *mle_all_data_languages*.
Also, the annotation `cSqlAnnotation_SelectAllDataLanguages` enforces for the parsed query that the value of multi language fields is retrieved in all data languages.
For tables which are configured for selection of all languages of its multi language fields (see the *mle_all_data_languages* argument for function [rdi.table()](../functions_runtime_dictionary_information/rdi.table.md)), execution of the query always retrieves all data languages.

## Example
```

sql_id_1 = sql.parse( "select tccom010.cuno from tccom010" )
```
```

sql_id_2 = sql.parse( "select * from tccom010", PARSE.SUPPRESS+PARSE.ANSI )
```

## Related topics
- [Dynamic SQL queries overview](overview.md)

- [Dynamic SQL queries synopsis](synopsis.md)
