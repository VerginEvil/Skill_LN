# WorkOrder.Complete

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1501-1504

```baan
DLL:   tsextwcsapi
This function is available from 2020.12 (KB2162018).
Syntax: long WorkOrder.Complete(
domain  tcorno           iWorkOrder,
domain  tsmdm.acln       iWorkOrderActivityLine,
domain  tsmdm.qmat       iActualQuantity,
domain  tscfg.cfst       iNewSerialStatus,
domain  tcyesno          iCreateFollowupWorkOrderForRemainingQuantity,
domain  tcyesno          iCopyEstimatesToActuals,
domain  tcyesno
iContinueIfNoReplacementForRemovedOutgoingSubassembly,
domain  tcyesno          iUpdateActualQuantityOnWorkOrderActivity,
domain  tcyesno
iSetWorkOrderToCompleteWhenLastActivityIsCompleted,
domain  tscfg.upd.ista   iActionOnPendingInspections,
domain  tcyesno
iContinueCloseWorkOrderIfPurchaseOrderNotApprovedYet,
domain  tcyesno          iClosePhysicalBreakdownChange,
ref     domain  tcyesno          oWorkOrderSignedOff,
ref     domain  tcyesno          oWorkOrderClosed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles setting a work order to completed.
When iWorkOrderActivityLine is filled, this specific work
order activity line will be set to completed. When all other
work order activities are already completed and
iSetWorkOrderToCompleteWhenLastActivityIsCompleted is set to
yes, the work order header will be set to completed as well.
When the work order is set to completed successfully, the
warehouse procedure steps that are set to automatic execution,
are started. Next, based on WCS parameters/office settings, the
work order can be signed-off and closed automatically.
Note:
- When an Electronic Signature is required for completing a
work order, this public interface can only be used when called
in an LN UI component. Only in that case the signature request
dialog can be started.
- When interactive counter reading reset rules are defined for
any of the work order activities, the session for resetting
the counters is not started when this public interface is
used. Resetting these counters can be done using LN UI.
Pre:    None.
Post:   This function sets a retry-point and will commit and/or abort
the transaction.
Input:  iWorkOrder
Work Order. (mandatory)
iWorkOrderActivityLine
Work Order Activity Line. (optional)
iActualQuantity
The actual maintained quantity to be set on the work
order. Must be >= 0.
An actual maintained quantity of zero implies that the
serialized item is not repaired and will not be
returned.
Note that when setting an individual activity line
to Completed, this quantity is not set on the work order
activity line.
When the actual quantity on the work order activity line
is zero and iUpdateActualQuantityOnWorkOrderActivity is
passed as 'yes', the planned quantity set on the work
order will be set on the work order activity line.
When passed as 'no' the actual quantity on the activity
line is not updated.
iNewSerialStatus
If the main item on the work order is serialized
controlled, this status will be assigned to it.
(mandatory)
If the work order item is serialized controlled and the
actual quantity is set to 1, only the following
statusses are valid:
- active
- working condition
- defective
- to be recycled
An actual maintained quantity of zero, implies that the
serialized item is not repaired and will not be
returned. Its status is set to Removed.
iCreateFollowupWorkOrderForRemainingQuantity
Create Follow-up Work Order for remaining quantity.
(mandatory Yes/No)
Only applicable for non-serialized controlled items.
iCopyEstimatesToActuals
Copy Estimates to Actuals. (mandatory Yes/No)
The required quantity of work order other resource lines
and of material resource lines with delivery type 'From
Service Inventory', is assigned to the actual quantity.
iContinueIfNoReplacementForRemovedOutgoingSubassembly
Continue if no replacement material line is defined for
a removed Outgoing Subassembly.
(mandatory Yes/No)
iUpdateActualQuantityOnWorkOrderActivity
Set the actual maintained quantity on the work order
activity. When the activity is derived from a master
routing and a previous activity is present with status
Completed, Singed-off or Closed, the actual quantity of
the previous activity is taken and set on the current
work order activity line.
When no master routing is used the planned quantity as
set on the work order will be set on the current
work order activity line.
(mandatory Yes/No)
iSetWorkOrderToCompleteWhenLastActivityIsCompleted
Set the work order header status to complete when the
given work order activity line is completed successfully
and all other work order activity lines are already
completed. (mandatory Yes/No)
iActionOnPendingInspections
When the work order is set to completed and there are
open/pending inspections present, this variable can be
used to indicate what to do with these inspections.
Possible values are:
- change status
inspection status is set to Not Measured
- delete inspection
the inspections are deleted.
- cancel
the inspections remain as is.
iContinueCloseWorkOrderIfPurchaseOrderNotApprovedYet
When the work order is set to completed and next
automatically processed to status closed, based on WCS
parameters/office settings, and a purchase invoice is
present for a purchase order linked to the work order,
which is not approved yet, this argument determines to
continue closing the work order.
(mandatory Yes/No)
iClosePhysicalBreakdownChange
When the work order is set to completed and next
automatically processed to status closed, based on WCS
parameters/office settings, open physical breakdown
changes can be set to closed.
(mandatory Yes/No)
Output: oWorkOrderSignedOff
Indicates if the work order is set to Signed-Off.
oWorkOrderClosed
Indicates if the work order is set to Closed.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - work order set to completed succesfull
<> 0    - Error during completing work order occurred
```
