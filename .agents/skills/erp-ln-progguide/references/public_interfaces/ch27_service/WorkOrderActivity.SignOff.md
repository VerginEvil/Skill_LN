# WorkOrderActivity.SignOff

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1516-1518

```baan
DLL:   tsextwcsapi
This function is available from 2025.09 (KB3610664).
Syntax: long WorkOrderActivity.SignOff(
domain  tcorno           iWorkOrder,
domain  tsmdm.acln       iActivityLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to sign-off a Work Order Activity.
Note that transaction handling is done within this public
interface.
Pre:    Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iWorkOrder
Work Order
Mandatory.
iActivityLine
Work Order Activity Line
Mandatory.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
SignOffWorkOrderWhenAllActivitiesAreSignedOff
domain  tsyesno         tsyesno.no
If this option is set to 'Yes', and all Work Order
Activities are signed off, the Work Order is signed off.
CloseWorkOrderWhenAllActivitiesAreClosed
domain  tsyesno         tsyesno.no
If this option is set to 'Yes', and all Work Order
Activities are closed, the Work Order is closed.
Note:
The Work Order Activity is only closed automatically
when the option 'Automatically Close Work Order' is
turned on in the parameters or settings
by Operations Department.
AlwaysIgnoreEmptyActualProblemOrSolution
domain  tcyesno         tcyesno.no
If this option is set to 'Yes', signing off the Work Order
Activity is not cancelled when the actual problem or actual
solution is not filled.
Otherwise when the actual problem or actual solution is
empty, the signing off is cancelled if all of the below
are true:
- The Work Order did not originate from a call;
- The Problem Solution handling on the
service type is 'Warning';
- Parameter 'Diagnostics' is not implemented;
- There is no next department transfer
work order present.
ActionForNonExecutedInspections
domain  tscfg.upd.ista
tscfg.upd.ista.change.status
If this option is set to 'Change Status', the status of
every non-executed inspection is set to 'Not Measured'.
If this option is set to 'Delete Inspections', every
non-executed inspection is deleted.
If this option is set to 'Cancel', and non-executed
inspections are present, then signing off the
Work Order Activity is cancelled.
IgnoreUnapprovedSubcontractedPurchaseOrders
domain  tcyesno         tcyesno.no
If this option is set to 'No', and the Work Order is
internal and there are related subcontracted Purchase
Orders that are not approved, then the Work Order
Activity is not closed.
CloseAllOpenPhysicalBreakdownChanges
domain  tcyesno         tcyesno.no
If this option is set to 'Yes' and the Work Order
Activity is closed, then all related
open Physical Breakdown Changes are closed.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       No errors occurred. Depending on the options in the
processing option set, signing off or closing may still
have been cancelled without any message given.
<> 0    Error(s) occurred.
```
