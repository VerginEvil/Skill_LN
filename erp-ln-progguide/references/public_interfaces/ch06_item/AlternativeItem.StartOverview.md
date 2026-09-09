# AlternativeItem.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for AlternativeItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 232-233

```baan
DLL:   tcextibdapi
This function is available from 2024.07 (KB2303602).
Syntax: long AlternativeItem.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  tcitem           iAlternativeItem,
domain  tccpri           iPriority,
ref     domain  tcitem           oItem,
ref     domain  tcitem           oAlternativeItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Alternative Items (tcibd0505m000) in overview mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used
iSessionIndex
Value:  1:  Item, Alternative Item
2:  Item, Priority, Alternative Item
Determines the sort order in the session.
E.g. if iSessionIndex = 1, then Items are sorted by
Item and Alternative Item.
iQueryExtend
A specific query to be used when starting the
session. Use this to specfiy a filter.
Using the query extend may lead to a
"data not found, session not started" situation.
iItem
optional
iAlternativeItem
optional
iPriority
optional
Output: When Start Mode is MODAL, and one row is selected on exit:
oItem               - selected Item
oAlternativeItem    - selected Alternative Item
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Otherwise.
```
