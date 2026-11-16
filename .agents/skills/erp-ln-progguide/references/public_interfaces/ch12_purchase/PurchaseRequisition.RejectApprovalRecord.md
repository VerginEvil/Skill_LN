# PurchaseRequisition.RejectApprovalRecord

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseRequisition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 419-419

```baan
DLL:   tdextpurapi
This function is available from 2025.11 (KB3632205).
Syntax: long PurchaseRequisition.RejectApprovalRecord(
domain  tcrqno           iPurchaseRequisition,
domain  tcsern           iSerialNumber,
domain  tccdis           iReasonForRejection,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to reject the given Requisition Approval
Progress record. Rejection of a record is only allowed if the previous
records have been approved. This function checks whether the
current user is allowed to perform the rejection. The purchase
requisition parameter/setting 'Approval Authorizations'
(tdpur000.apau.2/tdpur082.apau) is taken into account for this.
This function cannot be used if rejection of requisitions is
done through Workflow.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseRequisition    - Purchase requisition (mandatory)
iSerialNumber           - Serial number of the Approval Progress
record (mandatory)
iReasonForRejection     - Reason for rejection of the approval record;
this input argument overwrites any existing
reason for rejection.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The Approval Progress record is rejected.
<> 0                    - An error occurred
```
