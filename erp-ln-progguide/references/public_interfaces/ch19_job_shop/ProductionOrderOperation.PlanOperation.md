# ProductionOrderOperation.PlanOperation

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 795-796

```baan
DLL:   tiextsfcapi
This function is available from     2024.09 (KB2323309  ).
Syntax: long ProductionOrderOperation.PlanOperation(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcutcs           iStartOrEndDate,
domain  tcsetm           iSetupTime,
domain  tisfc.prtm       iProductionTime,
domain  tisfc.prtm       iRemainingTime,
domain  tcwttm           iQueueTime,
domain  tcwttm           iWaitTime,
domain  tcwttm           iMoveTime,
ref     domain  tcutcs           oTransportDateTo,
ref     domain  tcutcs           oStartDateQueue,
ref     domain  tcutcs           oProductionStartDate,
ref     domain  tcutcs           oRunStartDate,
ref     domain  tcutcs           oRemainingStartDate,
ref     domain  tcutcs           oStartDateWait,
ref     domain  tcutcs           oStartDateMove,
ref     domain  tcutcs           oTransportDateFrom,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to plan a Production Order Operation.
Based on the given input times, the resulting Operation dates
will be returned. Whether the Operation is planned forwards or
backwards is defined on the Production Order by the Planning Method.
Pre:    NA
Post:   NA
Input:  iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory. Must be in
iSite).
iOperation              Production Order Operation (Mandatory).
iStartOrEndDate         The desired Start Date for the Operation
if the planning method is forwards,
or the End Date if the planning method
is backwards.
iSetupTime              The Setup Time for the Operation to be
planned. Mandatory, use tisfc010.sutm,
unless this is one of the times required
to be changed.
iProductionTime         The Production Time for the Operation to
be planned. Mandatory, use tisfc010.prtm,
unless this is one of the times required
to be changed.
iRemainingTime          The Remaining Time for the Operation to
be planned. Mandatory, use tisfc010.retm,
unless this is one of the times required
to be changed.
iQueueTime              The Queue Time for the Operation to be planned.
Mandatory, use tisfc010.qutm, unless this
is one of the times required to be changed.
iWaitTime               The Wait Time for the Operation to be planned.
Mandatory, use tisfc010.trdl, unless this
is one of the times required to be changed.
iMoveTime               The Move Time for the Operation to be planned.
Mandatory, use tisfc010.mvtm, unless this
is one of the times required to be changed.
Output:
oTransportDateTo        The Transport Date To for the planned Operation.
oStartDateQueue         The Start of the Queue Time for the planned
Operation.
oProductionStartDate    The Start Date of the Production for the
planned Operation.
oRunStartDate           The Run Start Date for the planned Operation.
oRemainingStartDate     The Remaining Start Date for the planned
Operation.
oStartDateWait          The Start of the Wait Time for the planned
Operation.
oStartDateMove          The Start of the Move Time for the planned
Operation.
oTransportDateFrom      The Transport Date From for the planned Operation.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0 / <> 0
```
