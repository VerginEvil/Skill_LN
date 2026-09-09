# PurchaseOrder.InitiateChangeRequest

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 444-445

```baan
DLL:   tdextpurapi
This function is available from 2024.04 (KB2323365).
Syntax: long PurchaseOrder.InitiateChangeRequest(
domain  tcorno           iPurchaseOrder,
domain  tdpur.corg       iChangeRequestOrigin,
ref     domain  tcorno           oChangeRequest,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function initiates a new change request for the given
purchase order. If the status of the given purchase order is
'Closed', then it will first be re-opened.
The initiation consists of two parts:
1. Determine if initiate change request is allowed.
2. Initiate the change request.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder          - Purchase Order (mandatory)
iChangeRequestOrigin    - Origin of the Change Request (mandatory)
Output: oChangeRequest          - New Change Request
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       -> The change request has been initiated
<> 0    -> An error occurred
```
