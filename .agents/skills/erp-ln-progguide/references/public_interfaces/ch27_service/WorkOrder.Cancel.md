# WorkOrder.Cancel

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1498-1500

```baan
DLL:   tsextwcsapi
This function is available from 2022.04 (KB2235599).
Syntax: long WorkOrder.Cancel(
domain  tcorno           iWorkOrder,
domain  tsmdm.acln       iWorkOrderActivityLine,
domain  tsspc.stat       iNewPlannedActivityStatus,
domain  tcyesno          iSetLinkedCallToSolved,
domain  tcyesno          iCancelPurchaseMaterialLines,
domain  tccdis           iCancelReason,
domain  tsmdm.utct       iCancelTime,
domain  tsmdm.text       iCancelText,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the cancellation of a work order or
single activity.
If iWorkOrderActivityLine is zero the whole work order
will be cancelled. If iWorkOrderActivityLine is not zero
the specific work order activity line will be cancelled.
If the work order or activity has follow-up work orders,
these will be cancelled as well.
This function has the same options as session
'Cancel Work Order' (tswcs2260m000) when cancelling a
work order or work order activity. These are options available
as input field and conditional options asked by questions.
- iNewPlannedActivityStatus
In case the order or activity is originating from
a planned activity this input argument can be used to
set the status of the originating planned activity
after cancelling.
- iSetLinkedCallToSolved
In case the order or activity is originating from
a call and this argument has value 'Yes' the call
status is set to 'Solved'.
- iCancelPurchaseMaterialLines
If purchase orders are created for work order material lines,
this option can be used to cancel or delete these.
When the purchase order status is Planned, the purchase order
is deleted. If the purchase order is already processed,
the link in the service order related orders is removed.
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Input:  iWorkOrder
Work Order (mandatory)
iWorkOrderActivityLine
Work Order Activity Line (optional)
iNewPlannedActivityStatus (mandatory, Free/Released/Cancelled)
In case the order or activity is originating from
a planned activity this input argument can be used to
set the status of the originating planned activity
after cancelling.
Allowed values are:
- Free
- Released
- Cancelled
iSetLinkedCallToSolved  (mandatory, Yes/No)
In case the order or activity is originating from
a call and this argument has value 'Yes' the call
status is set to 'Solved'.
iCancelPurchaseMaterialLines (mandatory, Yes/No)
If this option has value 'Yes' purchase orders
created for work order material lines are cancelled
or deleted. When the purchase order status is Planned,
the purchase order is deleted. If the purchase order
is already processed, the link in the service order
related orders is removed.
iCancelReason (mandatory)
Must be of type 'Cancellation' and date effective
when cancelling.
iCancelTime (mandatory)
The cancel time.
iCancelText (optional)
Cancellation text.
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - Work order or activity set to cancelled succesfull
<> 0    - Error during cancelling the work order or activity
occurred
```
