# WorkOrderIncomingSubassembly.Confirm

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrderIncomingSubassembly
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1506-1507

```baan
DLL:   tsextwcsapi
This function is available from     2026.06 (KB3671831  ).
Syntax: long WorkOrderIncomingSubassembly.Confirm(
domain  tcorno           iWorkOrder,
domain  tcpono           iSubassemblyLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to confirm the given Incoming Subassembly.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Input:  iWorkOrder
Work Order number: Mandatory
iSubassemblyLine
Subassembly Line number: Mandatory
iProcessingOptionSet
This argument is currently unused and must be 0.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - Subassembly was confirmed successfully
<> 0                          - Error during confirming the Incoming Subassembly
```

## Public Interfaces for PlannedActivity

The following functions are available: PlannedActivity.CreateMaintenancePlan PlannedActivity.StartOverview PlannedActivity.SwitchStatus PlannedActivity.TransferToFieldService
