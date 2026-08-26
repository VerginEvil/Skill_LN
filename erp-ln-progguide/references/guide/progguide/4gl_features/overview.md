# Programming a UI Script overview
This section describes how to program a BAAN UI script.
When you create a session, the default behavior of that session is handled by the 4GL engine. If additional functionality is needed or default functionality needs to be by-passed, this should be programmed in a UI script.
In Infor Enterprise Server, user interface actions are programmed in the UI script and application logic for a table, table fields and relations between tables should be programmed in the [Data Access Layer](../functions_dal/overview.md) (DAL). Programmers create a user interface (UI) script to change the default behavior of a session. They create a DAL script to program all the logical integrity rules for a particular table. This section discusses UI scripts.

## 4GL script types
There are two types of UI scripts:
- UI scripts that offer a direct view on a table in the database (previously known as type 1, 2 or 3).
- UI scripts that have no direct view an a table in the database (previously known as type 4 sessions). Typically, this is a session where you enter a selection range for printing or processing data in the database

## Event-driven programming
4GL scripts are event oriented. They consist of one or more event sections in which you program actions to be performed at particular states of execution of the 4GL engine – for example, when a session is started, before a group of fields is activated, when the value of a field changes, and so on. It is not necessary to program all sections, only those for which the 4GL engine does not provide the required functionality.
The statements programmed in a section can be a combination of 3GL/4GL functions and 3GL statements. For information about the 3GL programming language, see [3GL programming language features: overview](../3gl_features/overview.md).

## Related topics
- [4GL event sections](4gl_event_sections.md)
- [Flow of 4GL engine](flow_of_standard_program.md)
- [Guidelines on browsing/zooming](browsing.md)
