# HandlingUnit.RejectRemaining

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1058-1059

```baan
DLL:   whextwmdapi
This function is available from 2021.09 (KB2202105).
Syntax: long HandlingUnit.RejectRemaining(
domain  whhuid           iHandlingUnit,
domain  tccdis           iRejectReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function Rejects the (remaining) quantity of the given
handling unit that is not yet approved, rejected, or
(inbound only) destroyed. If no inspection results have been
specified for the handling unit yet, all items are rejected.
The Warehouse Inspection should have status Open or In Process
and not reside in a WMS-controlled warehouse.
This function does not process the inspection results.
For processing, use WarehouseInspection.Process
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iHandlingUnit           - Handling Unit (mandatory)
iRejectReason           - Reject Reason (mandatory)
Reason must be of type 'Rejection of Goods'.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
