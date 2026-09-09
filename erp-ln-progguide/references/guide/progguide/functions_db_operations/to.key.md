# to.key()

## Syntax:
`function void to.key( long key_number, [ long nr.view.fields ] )`

## Description
Use this to change the key of the main table without user interaction. The *key_number* argument specifies the new key.
When nr.view.fields is specified the session will start with the specified number of viewfields, this is valid only for sessions with dynamic index switching. When in dynamic index switching sessions this parameter is not passed, the default number of viewfields as defined in Sessions - Indices for that index. Note the alignment, labels, and validation when you have sessions with variable number of viewfields.
Using this function with a non existing *key_number* is ignored without a message.
When changing the key of the main table within the [on.main.table()](on.main.table.md) function, you must use [db.change.order()](db.change.order.md) instead. Also, to change the key of a table other than the main table, you must use *db.change.order()*.
You can also use execute(change.order) to change the key of the main table. In this case, the user selects the new key.
Note that during execution of the ADD.SET, MODIFY.SET and MARK.DELETE commands, the current key is saved and the primary key becomes the current key. After the database has been updated, the [4GL engine](../glossary/glossary.md#fourgl_engine) restores the saved key.

## Arguments
| | | |
|---|---|---|
| `long` | `key_number` |  Sequence number of the key to be used. This is the index number of the table definition, not the session index number as found under Session -> Indices.  |
| `[ long` | `nr.view.fields ]` |  specifies the specified number of viewfields the session will start with  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [4GL form sections](../4gl_features/4gl_form_sections.md)

- [4GL choice sections](../4gl_features/4gl_choice_sections.md)

- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
