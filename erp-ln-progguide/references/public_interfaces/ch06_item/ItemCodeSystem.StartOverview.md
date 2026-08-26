# ItemCodeSystem.StartOverview

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for ItemCodeSystem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 195-196

```baan
DLL:   tcextibdapi
This function is available from     2025.08 (KB3611238  ).
Syntax: long ItemCodeSystem.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccitt           iItemCodeSystem,
ref     domain  tccitt           oItemCodeSystem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Starts the session Item Code Systems (tcibd0106m000) in overview
mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used.
iSessionIndex
Not used.
iQueryExtend
A specific query to be used when zooming to the session.
Using the query extend may lead to a "data not found,
session not started" situation. (Optional)
iItemCodeSystem
optional
Output: When Start Mode is MODAL, and one row is selected on exit:
oItemCodeSystem                               - Item code system of the selected row
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```

## Public Interfaces for ItemByItemCodeSystem

The following functions are available: ItemByItemCodeSystem.StartOverview
