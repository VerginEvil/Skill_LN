# SalesOrderChangeRequest.Process

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderChangeRequest
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 371-371

```baan
DLL:   tdextslsapi
This function is available from 2023.06 (KB2290338).
Syntax: long SalesOrderChangeRequest.Process(
domain  tcorno           iChangeRequest,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function processes an approved sales order change request
to the original sales order.
Pre:    Caller must set retry-point
Post:   Caller must set commit/abort transaction
Input:  iChangeRequest          - Sales Order Change Request (mandatory)
Output: oExceptionMessage       - The last message if any message is
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
