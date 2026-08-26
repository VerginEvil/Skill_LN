# sql.parse()

## Syntax:
`function long sql.parse( string query(.), [ long mode, ref string err.msg, ref long err.line, const string annotation, ... ] )`

## Description
This defines an SQL query that you can subsequently execute and retrieve the results of by using the other dynamic SQL functions. The query takes the form of a SELECT statement (see [Database handling overview](../functions_database_handling/overview.md)).
The optional argument *mode* can be used to influence the behavior.

## Arguments
-
-
| | | |
|---|---|---|
| `string` | `query(.)` |  |
| `[ long` | `mode ]` |  Optional parameter with default value 0.  |
| `[ ref string` | `err.msg ]` |  Optional argument which, when there is a parse error, receives the error message. If this optional argument is used, then first the *mode* argument must be supplied. This optional argument can be used as of [TIV level 2100](../tiv/tiv_2100.md).  |
| `[ ref long` | `err.line ]` |  Optional argument which, when there is a parse error, receives the line number in the query where the error is detected. If this optional argument is used, then first the *err.msg* argument must be supplied. This optional argument can be used as of [TIV level 2100](../tiv/tiv_2100.md).  |
| `[ const string` | `annotation, ... ]` |  Optional arguments specifying annotations to be applied when parsing the query. The annotation `cSqlAnnotation_SelectAllDataLanguages` enforces for the parsed query that the value of multi language fields is retrieved in all data languages, independent of the setting of [resource](../misc/bshell_resources.md) *mle_all_data_languages*. This annotation is available as of [TIV level 2140](../tiv/tiv_2140.md). If this optional argument is used, then first the *err.line* argument must be supplied. The optional annotation arguments can be used as of [TIV level 2140](../tiv/tiv_2140.md).  |

## Return values
| | |
|---|---|
| 0 | Error. |
| > 0 | Query ID; this is used by the other functions to identify the particular query.  |

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
