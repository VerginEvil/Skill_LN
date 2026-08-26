# PlannedCostPegTransfers.StartOverview

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedCostPegTransfers
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 583-584

```baan
DLL:   cpextrrpapi
This function is available from     2024.07 (KB3501669  ).
Syntax: long PlannedCostPegTransfers.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  cpcom.plnc       iScenario,
domain  tcorno           iTransfer,
ref     domain  cpcom.plnc       oScenario,
ref     domain  tcorno           oTransfer,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session
Planned Cost Peg Transfers (cprrp0130m000).
Input:  iStartMode              Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Specifies the table                      -index that is to
be used.
Standard supported values:
1: sort by Scenario, Transfer.
iQueryExtend            A specific query to be used when zooming
to this session.
iScenario               Planning Scenario.
iTransfer               Planned Cost Peg Transfer Order
Output: oScenario               Selected Planning Scenario
oTransfer               Selected Planned Cost Peg Transfer Order
oExceptionMessage       The last message if any message is
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

## Public Interfaces for PlannedPurchaseOrder

The following functions are available: PlannedPurchaseOrder.Transfer
