# PurchaseOrderChangeRequest.Process

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderChangeRequest
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 480-480

```baan
DLL:   tdextpurapi
This function is available from     2024.04 (KB2323365  ).
Syntax: long PurchaseOrderChangeRequest.Process(
domain  tcorno           iChangeRequest,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function processes the given purchase order change request.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iChangeRequest                        - Purchase Order Change Request (mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     -> The change request has been processed
<> 0                          -> An error occurred
```

## Public Interfaces for SupplierStagePaymentLine

The following functions are available: SupplierStagePaymentLine.Release SupplierStagePaymentLines.StartDetail SupplierStagePaymentLines.StartOverview
