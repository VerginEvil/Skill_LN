# MaintenanceSalesOrderLine.Cancel

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceSalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1493-1494

```baan
DLL:   tsextmscapi
This function is available from 2026.02 (KB3649711).
Syntax: long MaintenanceSalesOrderLine.Cancel(
domain  tcorno           iMaintenanceSalesOrder,
domain  tcpono           iMaintenanceSalesOrderLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function cancels a Maintenance Sales Order Line. When the
Line is not passed, the Maintenance Sales Order is cancelled.
This function provides the same functionality as session
Cancel Maintenance Sales Order (Line) (tsmsc1210m000).
Pre:    db.retry.point must have been set.
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Commit/abort the transaction.
Process Warehouse order lines.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iMaintenanceSalesOrder          - Maintenance Sales Order;
mandatory
iMaintenanceSalesOrderLine      - Maintenance Sales Order Line;
not mandatory
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
CancelReason            domain  tccdis          empty
Cancel Reason; must have Reason Type Cancellation.
Mandatory.
CancelDate              domain  tsmdm.utct      current date
Date of Cancellation.
CancelTextNumber        domain  tctxtn          0
Text number referring to the Cancel Text.
PlannedActivityStatus   domain  tsspc.stat      free
When Part Line is related to a Planned Activity, on
canceling the line, the Planned Activity Status can be
set to Free, Released, or Canceled.
SolveCall               domain  tcyesno         yes
When this option is Yes, the status of all Calls related
to the Part Lines to be cancelled will be set to solved,
if allowed.
When this option is No, all Calls related to the Part
Lines to be cancelled will be reverted to their previous
status, if allowed.
Note:
This option does not apply to Calls that have been
transferred to multiple Part Lines if one of these Part
Lines still exists and is not (being) cancelled.
- If the other Part Line has status Free, Released or
In Process, the status of that Call will never be
changed.
- If the other Part Line has status Completed, Closed or
Costed, the Call will always be set to solved, even if
this option is No.
CancelOrder             domain  tcyesno         no
When all lines have been canceled, the Maintenance
Sales Order is canceled when this option is Yes.
CancelWhenDispositionOfNonConformingReport
domain  tcyesno         yes
When Part Line is the Disposition of a Non-Conforming
Report, it will not be canceled when this option is No.
CancelWhenDispositionOfFracasDocument
domain  tcyesno         yes
When Part Line is the Disposition of a Fracas Document,
it will not be canceled when this option is No.
CancelWhenFracasDocumentNotClosed
domain  tcyesno         no
When Part Line, or related work order, is linked to an
unclosed Fracas Document, it is canceled when this
option is Yes.
Output  :
ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0                     - No error; however, error messages can
have been set.
<> 0                  - An error occurred
```
