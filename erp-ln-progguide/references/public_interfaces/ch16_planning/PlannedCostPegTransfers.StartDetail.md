# PlannedCostPegTransfers.StartDetail

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedCostPegTransfers
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 583-583

```baan
DLL:   cpextrrpapi
This function is available from     2024.07 (KB3501669  ).
Syntax: long PlannedCostPegTransfers.StartDetail(
long             iStartMode,
domain  cpcom.plnc       iScenario,
domain  tcorno           iTransfer,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session
Planned Cost Peg Transfers (cprrp0130m000).
Input:  iStartMode              Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iScenario               Planning Scenario.(mandatory, must exist)
iTransfer               Planned Cost Peg Transfer Order.
(mandatory, must exist)
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
