# ProjectContractDeliverable.StartMonitor

> Chapter: Chapter 33 Public Interfaces for Project
>
> Group: Public Interfaces for ProjectContractDeliverable
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1693-1696

```baan
DLL:   tpextpdmapi
This function is available from     2025.07 (KB3556268  ).
Syntax: long ProjectContractDeliverable.StartMonitor(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcemno           iContractManager,
domain  tcemno           iInternalSalesRepresentative,
domain  tpctm.cdmf       iFilterbyContractOrPlannedDeliveryDate,
domain  tcdate2          iContractDeliveryDateFrom,
domain  tcdate2          iContractDeliveryDateTo,
domain  tcdate2          iPlannedDeliveryDateFrom,
domain  tcdate2          iPlannedDeliveryDateTo,
domain  tcyesno          iExpectedOnTime,
domain  tcyesno          iDeliveredOnTime,
domain  tcyesno          iDeliveredLate,
domain  tcyesno          iPastDue,
domain  tcyesno          iAtRisk,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface starts session 'Contract Deliverables
Monitor'(tppdm7100m400)
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
started session.
Possible values are:
"AllDeliverables":All deliverables are displayed
"PlannedDeliverables":Only planned deliverables are
displayed
"OpenDeliverables":Only open deliverables are displayed
iSessionIndex           Specifies the session index that is to
be used.
iQueryExtend            A specific query to be used when zooming
to this session.
Following input variables form the filtering fields, these
fields are not mandatory.
iContractManager
In the grid the data for this Contract Manager
will be shown.
iInternalSalesRepresentative
In the grid the data for this Internal Sales
Representative will be shown.
iFilterbyContractOrPlannedDeliveryDate
In the grid the data is filtered by Contract or
Planned Delivery Date.
Allowed Values for TargetStatus are:
tpctm.cdmf.ctdd                               - Contract Delivery Date; Default Value
tpctm.cdmf.pldd                               - Planned Delivery Date
iContractDeliveryDateFrom
In the grid the data from this
Contract Delivery Date will be considered if
iFilterbyContractOrPlannedDeliveryDate
is by Contract Delivery Date.
iContractDeliveryDateTo
In the grid the data upto this
Contract Delivery Date will be considered if
iFilterbyContractOrPlannedDeliveryDate
is by Contract Delivery Date.
iPlannedDeliveryDateFrom
In the grid the data from this
Planned Delivery Date will be considered if
iFilterbyContractOrPlannedDeliveryDate
is by Planned Delivery Date.
iPlannedDeliveryDateTo
In the grid the data upto this
Planned Delivery Date will be considered if
iFilterbyContractOrPlannedDeliveryDate
is by Planned Delivery Date.
iExpectedOnTime
In the grid the data for the status which are
Expected on Time will be shown.
iDeliveredOnTime
In the grid the data for the status which are
Delivered on Time will be shown.
iDeliveredLate
In the grid the data for the status which are
Delivered Late will be shown.
iPastDue
In the grid the data for the status which are
Past Due will be shown.
iAtRisk
In the grid the data for the status which are
At Risk will be shown.
Output:
oExceptionMessage                             - The last message if any message is
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

## Public Interfaces for ProjectActivityBudget

The following functions are available: ProjectActivityBudget.AddCPQConfiguration
