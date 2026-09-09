# ItemRoutingOperations.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ItemRoutingOperations
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 638-639

```baan
DLL:   tiextrouapi
This function is available from 2020.03 (KB2111387).
Syntax: long ItemRoutingOperations.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iMainItem,
domain  tirou.opro       iRouting,
domain  tcopno           iOperation,
domain  tirou.sern       iSequenceNumber,
ref     domain  tcitem           oMainItem,
ref     domain  tirou.opro       oRouting,
ref     domain  tcopno           oOperation,
ref     domain  tirou.sern       oSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Routing Operations
in overview mode (tirou1102m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Not Used. The session will always start
with the first session index:
Item, Routing code, Operation, Sequence Number
iQueryExtend            A specific query to be used when zooming
to this session.
Primary Key fields:
iMainItem             Main Item
iRouting              Routing (Mandatory if iSessionIndex = 1
and iStartMode = MODELESS)
iOperation            Operation (Mandatory if iSessionIndex = 1
and iStartMode = MODELESS)
iSequenceNumber       Sequence Number (Mandatory if
iSessionIndex = 1 and iStartMode = MODELESS)
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oMainItem             Main Item
oRouting              Routing
oOperation            Operation
oSequenceNumber       Sequence Number
oExceptionMessage       The last message if any message is
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
