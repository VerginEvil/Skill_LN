# WorkOrder.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1499-1501

```baan
DLL:   tsextwcsapi
This function is available from     2025.01 (KB3543185  ).
Syntax: long WorkOrder.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iWorkOrder,
long             iViewFieldSet,
ref     domain  tcorno           oWorkOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Work Orders
(tswcs2100m000).
Before calling WorkOrder.StartOverview(), call
ProcessingOptionSet.Create() and assign the value to
iViewFieldSet.
After the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the table                              -index that is to be used. (Optional)
Supported values:
1: sort by Work Order
2: sort by (Serialized) Item
3: sort by Service Type
4: sort by Department, Latest Finish Time
5: sort by Department, Planned Finish Time
6: sort by Status
7: sort by Top Work Order, Initiating Work Order
8: sort by Sold                               -to Business Partner, Project
iQueryExtend
A specific query to be used when zooming to this
session. Note that only extensions on main
table tswcs200 are supported. (Optional)
iWorkOrder
The Work Order to display at the top of the grid if
present in the chosen view. (Optional)
iViewFieldSet
Processing Option Set to set the view fields
when the index used is not index 1. (Optional)
INDEX   NAME                    TYPE                    DEFAULT
================================================================
2       Item                    domain  tcitem          empty
2       SerialNumber            domain  tcibd.sern      empty
3       ServiceType             domain  tsmdm.cstp      empty
4*      OperationsDepartment    domain  tccwoc          empty
4       LatestFinishTime        domain  tsmdm.pldt      0
5*      OperationsDepartment    domain  tccwoc          empty
5       PlannedFinishTime       domain  tsmdm.pldt      0
6       Status                  domain  tswcs.stat      tswcs.stat.free
7       MaintenanceSalesOrder   domain  tcorno          empty
7       PartMaintenanceLine     domain  tcpono          0
7       TopWorkOrder            domain  tcorno          empty
7       ReferenceA              domain  tcrefa          empty
7       InitiatingWorkOrder     domain  tcorno          empty
8       SoldToBusinessPartner   domain  tccom.bpid      empty
8       Project                 domain  tccprj          empty
* The OperationsDepartment property is used for indices 4 and 5.
Output:
oWorkOrder
The selected Work Order if iStartMode is MODAL and the
session is closed by a single selection.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    An error occurred
```

## Public Interfaces for WorkOrderActivity

The following functions are available: WorkOrderActivity.ProcessReturnDeliveries WorkOrderActivity.SignOff
