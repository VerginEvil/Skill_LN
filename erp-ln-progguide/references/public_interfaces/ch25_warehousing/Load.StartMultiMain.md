# Load.StartMultiMain

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Load
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1144-1144

```baan
DLL:   whextinhapi
This function is available from 2022.07 (KB2243668).
Syntax: long Load.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.load       iLoad,
domain  tccfrw           iCarrier,
domain  tccrte           iRoute,
domain  tcdate           iPlannedDeliveryDate,
domain  tcncmp           iShipToCompany,
domain  tctyps           iShipToType,
domain  tccshp           iShipToCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the multi main table session
Load (whinh4640m000).
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
Not Used.
iSessionIndex
Specifies the table index that is to be used.
iQueryExtend
A specific query to be used when zooming to this session.
iLoad
Optional
iCarrier
Optional
iRoute
Optional
iPlannedDeliveryDate
Optional
iShipToCompany
Optional
iShipToType
Optional
iShipToCode
Optional
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error
```
