# WorkOrder.Close

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1485-1487

```baan
DLL:   tsextwcsapi
This function is available from     2025.09 (KB3610861  ).
Syntax: long WorkOrder.Close(
domain  tcorno           iWorkOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to close a Work Order.
This function has the same options as reference form command
"Close Order" in the Work Order Session tswcs2100m100.
Pre:    Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
A db.retry.point() must have been specified.
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
An abort.transaction() or commit.transaction() must be
executed.
Input:  iWorkOrder
Work Order
Mandatory.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
IgnoreUnapprovedSubcontractedPurchaseOrders
domain  tcyesno         tcyesno.no
If this option is set to 'No', and the Work Order is
internal and there are related subcontracted Purchase
Orders that are not approved, then the Work Order
is not closed.
CloseAllOpenPhysicalBreakdownChanges
domain  tcyesno         tcyesno.no
If this option is set to 'Yes' and the Work Order is
closed, then all related open Physical Breakdown Changes
are closed.
ActionForNonExecutedInspections
domain  tscfg.upd.ista  tscfg.upd.ista.cancel
If this option is set to 'Change Status', the status of
every non                              -executed inspection is set to 'Not Measured'.
If this option is set to 'Delete Inspections', every
non                              -executed inspection is deleted.
If this option is set to 'Cancel', and non                              -executed
inspections are present, then closing the Work Order is
canceled.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       No errors occurred. Depending on the options in the
processing option set, closing may still
have been canceled.
<> 0    Error(s) occurred.
```
