# ProductionItemBySite.Start360

> Chapter: Chapter 18 Public Interfaces for Manufacturing Master
>
> Group: Public Interfaces for ProductionItemBySite
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 630-631

```baan
DLL:   tiextmfcapi
This function is available from     2024.02 (KB2303494  ).
Syntax: long ProductionItemBySite.Start360(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcsite           iSite,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Production Item by Site 360
(timfc1500m100).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used.
iSessionIndex           Not used.
iQueryExtend            A specific query to be used when zooming
to this session. Optional.
iSite                   Site                       - Optional.
iItem                   Item                       - Optional.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Error Occurred.
```

## Public Interfaces for AsBuilt

The following functions are available: AsBuilt.StartMultiMain AsBuilt.StartOverview
