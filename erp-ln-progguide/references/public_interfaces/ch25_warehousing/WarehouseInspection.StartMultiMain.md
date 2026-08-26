# WarehouseInspection.StartMultiMain

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1267-1268

```baan
DLL:   whextinhapi
This function is available from     2025.08 (KB3615530  ).
Syntax: long WarehouseInspection.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the multi main table session
Warehouse Inspection (whinh3622m000).
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
Not Used.
iSessionIndex
Not Used.
iQueryExtend
Optional.
A specific query to be used when starting the session.
Use this to specify a filter, e.g.
"whinh211.apst = whinh.apst.in.process"
Using the query extend may lead to a
"data not found, session not started" situation.
Primary Key Fields:
iInspection
iInspectionSequence                           - Primary Keys must refer to an existing
Warehouse Inspection.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```
