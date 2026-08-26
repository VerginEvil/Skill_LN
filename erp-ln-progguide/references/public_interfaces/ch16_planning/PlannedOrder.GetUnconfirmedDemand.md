# PlannedOrder.GetUnconfirmedDemand

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 557-558

```baan
DLL:   cpextrrpapi
This function is available from     2025.12 (KB3588102  ).
Syntax: long PlannedOrder.GetUnconfirmedDemand(
domain  cpcom.plnc       iPlanningScenario,
domain  tckoor           iOrderType,
domain  cporno           iOrderNumber,
domain  tcpono           iOrderLineFrom,
domain  tcpono           iOrderLineTo,
domain  tcpono           iSequenceFrom,
domain  tcpono           iSequenceTo,
ref     domain  tcqiv1           oUnconfirmedDemand,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Get the unconfirmed demand for a given planned order. Confirmed
Demand is demand coming from Order Types as defined in session
Propagate as Confirmed Demand(cpvmi0101m000). All other demand
is unconfirmed demand.
Pre:    N.A.
Post:   N.A.
Input:  iPlanningScenario       Mandatory. The planning scenario that
was used for creating the pegging
relations.
iOrderType              Mandatory. Type of the supply order
(E.g. tckoor.act.sfc or tckoor.cp.sfc
or tckoor.act.pur or tckoor.cp.pur)
iOrderNumber            Mandatory. The order number of the order
that provides the supply.
iOrderLineFrom          From Order Line/Position, to define the
range of lines/positions in the input
order in scope.
iOrderLineTo            To Order Line/Position, to define the
range of lines/positions in the input
order in scope. If both iOrderLineFrom
and iOrderLineTo are 0, full range is
used.
iSequenceFrom           From Sequence Number, to define the
range of sequence numbers in the input
order in scope.
iSequenceTo             To Sequence Number, to define the range
of sequence numbers in the input order
in scope. If both iSequenceFrom and
iSequenceTo are 0, the full range is
used.
Output: oUnconfirmedDemand      Unconfirmed Demand.
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Public Interface succesfully completed
<> 0                    Otherwise.
```
