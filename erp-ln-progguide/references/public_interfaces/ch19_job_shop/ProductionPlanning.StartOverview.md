# ProductionPlanning.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 824-826

```baan
DLL:   tiextsfcapi
This function is available from     2026.09 (KB3664966  ).
Syntax: long ProductionPlanning.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
ref     domain  tcpdno           oProductionOrder,
ref     domain  tcopno           oOperation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Production Planning
(tisfc0110m000) in overview mode. Use this session to display,
define and modify the planning for a specific production order.
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
iSessionIndex           Specifies the table                      -index that is to be
used.
Standard supported values:
1: sort by Production Order, Operation,
Operation Step (default).
iQueryExtend            A specific query to be used when zooming
to this session.
iProductionOrder        Production Order (Mandatory).
iOperation              Operation (Mandatory).
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oProductionOrder        Production Order.
oOperation              Operation.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```

## Public Interfaces for MachineOperation

The following functions are available: MachineOperation.StartDetail MachineOperation.StartOverview
