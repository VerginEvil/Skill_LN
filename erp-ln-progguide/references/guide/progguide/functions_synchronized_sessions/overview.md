# Synchronized sessions overview
Infor Enterprise Server provides several mechanisms for starting one session from another – these are zoom fields, synchronized sessions, and the 4GL [start.session()](../functions_starting_and_stopping_programs/start.session.md) function. This section discusses synchronized sessions and associated functions.
When two sessions are synchronized, actions performed on one session window have a direct effect on the other session window. Infor Enterprise Server implements two synchronization models:

- Dialog synchronization

- Child synchronization

## Dialog synchronization
This synchronizes a multioccurrence parent session with a single-occurrence dialog session. Both sessions act on the same main table. The parent session can be a modeless multioccurrence display form or a modal multioccurrence zoom window.
When the user double-clicks on an occurrence in the parent session, the [4GL engine](../glossary/glossary.md#fourgl_engine) automatically opens the synchronized dialog session (if it is not already open) and updates it with information from the selected record. Whether the dialog opens in edit or display mode depends on user authorization settings. The synchronized dialog is also opened automatically when the user initiates one of the following actions: insert record, edit record, or duplicate record.
When a record is saved in the synchronized dialog, the [4GL engine](../glossary/glossary.md#fourgl_engine) automatically updates the occurrence in the parent window.
Parent and child forms must be of the following types:
| | |
|---|---|
| Multioccurrence form | Dialog form |
| type 2 | type 1 |
| type 3 | type 3 with single occurrence |
Parent and child session settings must be as follows:
| | | |
|---|---|---|
|  | Multioccurrence session | Dialog session |
| Session type | display | maintain |
| Start option | 44 (get defaults) | 0 (no start option) |
| Window type | list window | synchronized dialog |
| Main session | yes | no |

## Child synchronization
Normally, this is used to synchronize sessions that act on different main tables. In this case, the primary key of the parent's main table must be a subset of the primary key of the child's main table.
For example, take an Orders table that lists client orders, and an Order lines table that lists order lines per order. The primary key of the Orders session is orderno. The primary key of the Order lines session is orderlines.orderno. In the Order lines session, orderno is a foreign key that references the Orders table.
With child synchronization, you can synchronize a parent session that uses the Orders table with a child session that uses the Order lines table. The user chooses a form command to open the child session from the parent session. So the user can view the order lines associated with the orders listed in the parent session.

## Related topics
- [Synchronized sessions illustration](synchronized_sessions_illustration.md)

- [Synchronized sessions synopsis](synopsis.md)

- [Child synchronization sample program](example.md)
