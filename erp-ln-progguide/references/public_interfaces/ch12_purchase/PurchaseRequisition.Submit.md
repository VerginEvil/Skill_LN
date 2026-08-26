# PurchaseRequisition.Submit

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseRequisition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 418-419

```baan
DLL:   tdextpurapi
This function is available from     2025.11 (KB3632205  ).
Syntax: long PurchaseRequisition.Submit(
domain  tcrqno           iPurchaseRequisition,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to submit the given Requisition.
This function checks whether the current user is allowed to perform
the submitting. The purchase requisition parameter/setting 'Approval
Authorizations' (tdpur000.apau.2/tdpur082.apau) is taken into account
for this.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseRequisition                  - Purchase requisition (mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - The Purchase requisition is submitted.
<> 0                                          - An error occurred
```

## Public Interfaces for PurchaseRequisitionLine

The following functions are available: PurchaseRequisitionLine.ConvertToPurchaseOrder PurchaseRequisitionLine.ConvertToPurchaseRFQ PurchaseRequisitionLine.StartDetail
