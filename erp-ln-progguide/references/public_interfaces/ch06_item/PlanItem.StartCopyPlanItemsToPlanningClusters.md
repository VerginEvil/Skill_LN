# PlanItem.StartCopyPlanItemsToPlanningClusters

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 221-222

```baan
DLL:   cpextrpdapi
This function is available from     2024.10 (KB3501609  ).
Syntax: long PlanItem.StartCopyPlanItemsToPlanningClusters(
long             iStartMode,
domain  cpitem           iSourceFromPlanItem,
domain  cpitem           iSourceToPlanItem,
ref     domain  tcemm.clus       iTargetPlanningCluster() fixed,
ref     domain  tccwar           iTargetWarehouse() fixed,
domain  tcyesno          iProcessReport,
domain  tcyesno          iErrorReport,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface can be used to start Process session
Copy Plan Items to Planning Clusters (cprpd1210m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iSourceFromPlanItem
From Plan Item. Minimum value of domain is taken
as default value. Optional.
iSourceToPlanItem
To Plan Item. Maximum value of domain is taken
as default value. Optional.
iTargetPlanningCluster
The Planning Cluster to which each plan item in the
specified range of items must be copied.
A fixed array of length five.Optional.
iTargetWarehouse
The warehouse to be used for the plan item(s) that will
be created for thespecified planning cluster.
A fixed array of length five. If the Planning Cluster is
filled, then specifying the Warehouse becomes mandatory,
otherwise it is Optional.
iProcessReport
Control to print process report. Optional.
iErrorReport
Control to print error report. Optional.
Output:
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

## Public Interfaces for ItemSerial

The following functions are available: ItemSerial.CreateOrUpdate ItemSerial.SetStatus
