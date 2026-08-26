# SubcontractingProcurementOrder.Approve

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for SubcontractingProcurementOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 485-486

```baan
DLL:   tdextpurapi
This function is available from     2025.01 (KB3545450  ).
Syntax: long SubcontractingProcurementOrder.Approve(
domain  tcorno           iSubcontractingProcurementOrder,
ref             boolean          oOrderIsBlocked,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to approve the given Subcontracting
Procurement Order.
Notes:
-                       This function has its own transaction management
-                       Variation Requests cannot be processed with this function
-                       If ION Workflow Document Approval is used, then the following
applies:
* if the order is waiting for Approval in ION, then updating
the status is not allowed
* After executing this function, the status update must be
approved in ION Workflow Document Approval
-                       This function does not start the execution of automatic
order steps. A separate Public Interface can be used to
start automatic order steps if necessary:
'SubcontractingProcurementOrder.StartAutomaticProcessing'
Pre:    There should be no pending transactions before calling this
function.
Post:   No need to commit or abort the process, that is handled within
this function.
Input:  iSubcontractingProcurementOrder
Subcontracting Procurement Order (Mandatory)
Output: oOrderIsBlocked         Indicates if the order is set to Blocked
during the approval process due to invalid
Documents that are linked to the order.
If true, the return value of the function
is 0.
For an order without linked Documents
that is blocked manually, the variable
oOrderIsBlocked is not set to true and
the function returns an error.
If the order is blocked, it cannot be
approved.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Approval successful or the order is
set to Blocked because of invalid
Documents (check argument oOrderIsBlocked)
<> 0                                          - An error occurred
```
