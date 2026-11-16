# EngineeringItem.StartDetail

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 268-268

```baan
DLL:   tiextedmapi
This function is available from 2026.03 (KB3609151).
Syntax: long EngineeringItem.StartDetail(
long             iStartMode,
domain  tcitem           iEngineeringItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts the session Engineering Item
(tiedm0110m000). This session can be used to define and modify
engineering items.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a Zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iEngineeringItem        Engineering Item.
Output: oExceptionMessage       The last message, if any message is
found. If more than one message is
given these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
