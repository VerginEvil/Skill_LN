# WorkCenters.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for WorkCenter
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 809-810

```baan
DLL:   tiextrouapi
This function is available from 2023.04 (KB2274111).
Syntax: long WorkCenters.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tccwoc           iWorkCenter,
ref     domain  tcsite           oSite,
ref     domain  tccwoc           oWorkCenter,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Work Centers
in overview mode (tirou0101m000).
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
iSessionIndex           1 - The session will start with the
first session index:
Work Center
2 - The session will start with the
second session index:
Site, Work Center
Second session index is only possible
when Job Shop by Site is active.
iQueryExtend            A specific query to be used when zooming
to this session.
Primary Key fields:
iSite                 Site (Mandatory if iSessionIndex = 2)
iWorkCenter           Work Center
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oSite                 Site
oWorkCenter           Work Center
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
