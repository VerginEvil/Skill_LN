# JobShopRouting.StartMultiMain

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopRouting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 667-667

```baan
DLL:   tiextrouapi
This function is available from 2020.03 (KB2111387).
Syntax: long JobShopRouting.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tirou.rouc       iJobShopRouting,
domain  tirou.revi       iJobShopRoutingRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Job Shop Routing
(tirou4600m000).
Note that the session can only be started if the parameter
'Job Shop by Site' is 'In Preparation' or 'Active'.
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
iQueryExtend            A specific query to be used when zooming
to this session.
Primary Key fields:
iSite                 Site (Mandatory)
iProduct              Product (Mandatory)
iJobShopRouting       Job Shop Routing (Mandatory)
iJobShopRoutingRevision
Job Shop Routing Revision (Mandatory)
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
