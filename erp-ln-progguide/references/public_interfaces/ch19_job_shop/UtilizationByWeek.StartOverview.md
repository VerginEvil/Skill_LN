# UtilizationByWeek.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for UtilizationByWeek
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 812-814

```baan
DLL:   tiextsfcapi
This function is available from     2024.01 (KB2300431  ).
Syntax: long UtilizationByWeek.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwoc           iWorkCenter,
domain  tcyrno           iProductionYear,
domain  tcweek           iProductionWeek,
domain  tcutcs           iSetupStartDate,
domain  tirou.mcno       iMachine,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Utilization by Week
(tisfc1502m000) in overview mode.
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
iSessionIndex           Optional. The index that will be used.
Supported values:
2: sort by Production Year, Production
Week, Setup Start Date, Work Center,
Machine, Production Order and
Operation.
5: sort by Production Year, Production
Week, Setup Start Date, Machine,
Production Order and Operation.
iQueryExtend            A specific query to be used when zooming
to this session. Optional.
iWorkCenter             Work Center                       - Optional
iProductionYear         Production Year                       - Optional
iProductionWeek         Production Week                       - Optional
iSetupStartDate         Setup Start Date                       - Optional
iMachine                Machine                       - Optional
iProductionOrder        Production Order                       - Optional
iOperation              Operation                       - Optional
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```

## Public Interfaces for SubcontractedOperation

The following functions are available: SubcontractedOperations.StartDetail SubcontractedOperations.StartOverview
