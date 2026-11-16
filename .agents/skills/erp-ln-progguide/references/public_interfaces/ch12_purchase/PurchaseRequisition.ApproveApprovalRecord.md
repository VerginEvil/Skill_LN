# PurchaseRequisition.ApproveApprovalRecord

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseRequisition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 418-418

```baan
DLL:   tdextpurapi
This function is available from 2021.05 (KB2185794).
Syntax: long PurchaseRequisition.ApproveApprovalRecord(
domain  tcrqno           iPurchaseRequisition,
domain  tcsern           iSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to approve the given Requisition Approval
Progress record. Approval is only allowed if all previous records
have already been approved. This function checks whether the
current user is allowed to perform the approval. The purchase
requisition parameter/setting 'Approval Authorizations'
(tdpur000.apau.2/tdpur082.apau) is taken into account for this.
This function cannot be used if approval of requisitions is
done through Workflow.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseRequisition    - Purchase Requisition; Mandatory.
iSequenceNumber         - Sequence number of the Approval Progress
record; Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The Approval Progress record is approved.
<> 0                    - An error occurred
```
