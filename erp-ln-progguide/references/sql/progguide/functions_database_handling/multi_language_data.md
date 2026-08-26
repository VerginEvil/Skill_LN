# Multi Language Data
Infor Enterprise Server provides support to store multibyte strings - like descriptions - in multiple languages. For columns that are defined to be MLF (Multi Language Field) the database contains values in each defined data language.
A process that performs SQL has a 'current data language'. All SQL operations (such as MAX, MIN, GROUP BY, ORDER BY, ...) work with the current data language, including selection of columns.

## function ml_one_lang
If you want to select the value in a different data language than the 'current data language', then the function [ml_one_lang( )](ml_one_lang_function.md) can be used.
Note  If you use this function and the selected data is later inserted into a database table, then the data will be inserted in the language that was selected only (other translations are lost).

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
