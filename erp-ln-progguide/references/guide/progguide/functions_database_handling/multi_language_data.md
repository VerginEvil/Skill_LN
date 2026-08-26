# Multi Language Data
Infor Enterprise Server provides support to store multibyte strings - like descriptions - in multiple languages. For columns that are defined to be MLF (Multi Language Field) the database contains values in each defined data language.
A process that performs SQL has a 'current data language'. All SQL operations (such as MAX, MIN, GROUP BY, ORDER BY, ...) work with the current data language, except selection of columns. When a column is selected from the database the value is retrieved in all data languages.

## function ml_one_lang
If you want to select the value in the current data language only (this may occur in situations that are known to be very performance-critical) or if you want to select the value in a different data language than the 'current data language', then the function [ml_one_lang( )](ml_one_lang_function.md) can be used.
Note  If you use this function and the selected data is later inserted into a database table, then the data will be inserted in the language that was selected only (other translations are lost).

## The resource mle_all_data_languages
The [resource](../misc/bshell_resources.md) *mle_all_data_languages* can be used (by setting it to the value 0) to change the behavior such that by default the value is selected in the current data language only.
In such a configuration, the annotation `cSqlAnnotation_SelectAllDataLanguages` can be used to override the default behavior and enforce that the value of multi language fields is retrieved in all data languages. This annotation can be applied to individual queries, both in [embedded SQL](embedded_sql.md) and in [dynamic SQL](dynamic_sql.md).
Alternatively, the [select.all.data.languages](../functions_dynamic_sql_queries/sql.set.select.all.data.languages.md) flag can be used for the same purpose.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
- [Multi Language Data overview](../functions_mle/overview.md)
