# Column filtering

## Columnfilter introduction
With LN-UI easy filtering is introduced.
Easy filtering is present on an overview screen.
At the top of a column filter fields are shown.
Column filtering is possible when easy filtering is allowed (see tools parameters) and the filter above the column is enabled.
With input of a value in the filter field or by defining an advanced filter, column-filtering is activated.

## Functionality columnfiltering
Column filtering is based on the supported SQL of the database.
With tools version 12.0 of tools shipped by Enterprise Server 10.5, a column filter on most fields is or can be made possible.
Limited support for column filtering in tools version 11.2.
1. Support multiple references to same table by introducing an alias for duplicate occurrence in the engine
2. Expression of calculated CDF is used in filter expression
Note: on error evaluating the expression of a CDF, all filters of calculated CDF’s are not taken in account.
3. Query extend field functionality is added. ( must be adopted in the application to make filter possible)
4. Extension scripts are supported.

## Columnfilter in overview
| | | | | | | | |
|---|---|---|---|---|---|---|---|
| easy filter on column |  | old behavior before application version 10.x | new behavior application version 10.x and higher |  |  |  |  |
|  |  | main table | unique reference | multiple reference | main table | unique reference | multiple reference |
| on form of session | table-field | yes | yes | no | yes | yes | yes |
| form-field | no | no*) |  |  |  |  |  |
| custom defined field | standaard CDF | yes | yes | no | yes | yes | yes |
| calculated CDF | no | yes**) |  |  |  |  |  |
| query.extend.fld… function | table-field | no | no | no | yes | yes | yes |
| form-field | no | yes |  |  |  |  |  |
| extension script fields | table field | no | no | no | yes | yes | yes |
| calculated field by script function | no | no |  |  |  |  |  |
*) often can be replaced in the application by SQL expression through query.extend.fld… functions.
**) must be a valid sql expression

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
- [quoted.string()](../functions_string_operations/quoted.string.md)
