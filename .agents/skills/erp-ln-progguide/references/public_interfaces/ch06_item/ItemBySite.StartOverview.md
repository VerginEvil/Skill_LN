# ItemBySite.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemBySite
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 193-194

```baan
DLL:   tcextibdapi
This function is available from 2020.06 (KB2127551).
Syntax: long ItemBySite.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcitem           iItem,
ref     domain  tcsite           oSite,
ref     domain  tcitem           oItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Items by Site  General (tcibd1550m000)
in overview mode.
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
Value:  1:  Site, Item
2:  Item, Site
iQueryExtend
A specific query to be used when starting the
session. Using the query extend may lead to a
"data not found, session not started" situation.
iSite   Mandatory when iSessionIndex = 1
iItem   Mandatory when iSessionindex = 2
Output: for iStartMode MODAL:
oSite                 - site of the selected row
oItem                 - item of the selected row
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
