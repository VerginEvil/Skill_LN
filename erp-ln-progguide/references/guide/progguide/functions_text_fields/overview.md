# Text fields overview
Use these functions for handling database text fields.

## Text numbers
Every text stored in the database has a text number. A text field that is included in a database table is referenced in the table by its text number. The text itself, its key words, and so on, are stored in a separate table.

## Text field names
The *text_field*, *text_field_from*, and *text_field_to* arguments must always contain a text field name. This name can be the name of a database field of type DB.TEXT, or it can be the name of a variable of type long. In both cases, the name must be enclosed by quote marks. When using a variable, this must be declared as EXTERN because the functions use the *text_field* argument indirectly to store the text number of the specified text. Database text field names are automatically declared as external.

## Committing transactions
In the case of all text field transactions, you must commit the transaction yourself.

## Related topics
- [Text fields synopsis](synopsis.md)
