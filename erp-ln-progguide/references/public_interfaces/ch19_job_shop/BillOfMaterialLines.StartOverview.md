# BillOfMaterialLines.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for BillOfMaterialLines
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 634-635

```baan
DLL:   tiextbomapi
This function is available from     2020.06 (KB2127704  ).
Syntax: long BillOfMaterialLines.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iMainItem,
domain  tcpono           iPosition,
domain  tcsern           iSequence,
ref     domain  tcitem           oMainItem,
ref     domain  tcpono           oPosition,
ref     domain  tcsern           oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Bill of Material (tibom1110m000)
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
Specifies the start filter that is to be applied to the
started session. Optional.
Possible values are:
"showAll": All BOM lines are displayed
"showEffective": Only effective lines are shown (default)
When empty: "showEffective" is applied
iSessionIndex
Not used.
iQueryExtend
A specific query to be used when zooming to this session.
Optional
iMainItem
Mandatory.
iPosition
Optional
iSequence
Optional
Output: for iStartMode MODAL:
oMainItem                                     - main item of selected line
(= iMainItem)
oPosition                                     - position of selected line
oSequence                                     - Sequence number of selected line
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

## Public Interfaces for ItemRoutingOperations

The following functions are available: ItemRoutingOperations.StartOverview
