# ItemCosting.StartDetail

> Chapter: Chapter 17 Public Interfaces for Standard Costs
>
> Group: Public Interfaces for ItemCosting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 618-619

```baan
DLL:   tiextcprapi
This function is available from     2026.02 (KB3606237  ).
Syntax: long ItemCosting.StartDetail(
long             iStartMode,
domain  tcitem           iItem,
domain  tcemm.grid       iEnterpriseUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Item - Costing in detail
mode (ticpr0107m000).
Input:  iStartMode              Specifies the start mode for the
session. Possible values are:
MODAL                                               - The parent session is blocked
until the child session exits.
The session will be started as
a zoom session.
MODELESS                                               - Parent and child are parallel
sessions that can be manipulated
simultaneously.
iItem                   Item
iEnterpriseUnit         Enterprise Unit
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    Otherwise.
```
