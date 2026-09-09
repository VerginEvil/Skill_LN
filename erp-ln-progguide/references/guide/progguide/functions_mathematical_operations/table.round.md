# table.round()

## Syntax:
`function void table.round( [ void field [, field]..., string table [, table]... ] )`

## Description
This rounds the values in certain tables and table fields according to parameters defined in the domain definition in the data dictionary.

## Arguments
| | | |
|---|---|---|
| `[ void` | `field [, field]... ]` |  The names of one or more table fields. The function rounds the values in all specified fields.  |
| `[ string` | `table [, table]... ]` |  The names of one or more tables. The function rounds all fields in the specified tables. You must specify table names within quotes – for example, " tpctst999".  |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  You can specify any combination of tables and fields, in any order.

## Examples
```

table.round()       | Rounds all fields of main table
table.round(pctst999.price, "tpctst888", pctst999.value)
                    | Rounds the two specified fields and all fields of the
                    | specified table
```
