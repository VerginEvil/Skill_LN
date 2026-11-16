# SalesOrder.InitiateChangeRequest

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 326-327

```baan
DLL:   tdextslsapi
This function is available from 2023.06 (KB2290338).
Syntax: long SalesOrder.InitiateChangeRequest(
domain  tcorno           iSalesOrder,
domain  tdsls.corg       iChangeRequestOrigin,
ref     domain  tcorno           oChangeRequest,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function initiates a new change request for the given sales order.
The initiation consists of two parts:
1. Determine if initiate change request is allowed.
2. Initiate the change request.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales Order (mandatory)
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
Return: 0       -> No error
<> 0    -> Error occurred
```
