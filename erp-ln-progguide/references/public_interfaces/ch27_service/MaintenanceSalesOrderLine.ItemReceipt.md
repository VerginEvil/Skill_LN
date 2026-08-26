# MaintenanceSalesOrderLine.ItemReceipt

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceSalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1481-1482

```baan
DLL:   tsextmscapi
This function is available from     2025.12 (KB3636915  ).
Syntax: long MaintenanceSalesOrderLine.ItemReceipt(
domain  tcorno           iMaintenanceSalesOrder,
domain  tcpono           iMaintenanceSalesOrderLine,
domain  tsmdm.qmat       iReceivedQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to register the Received Quantity in the
Receipt Location of a released Part Maintenance Line.
On registering, the Received Quantity is updated, including the
Actual Receipt Time. The line status is set to In Process.
Pre:    db.retry.point must have been set.
Post:   Commit/abort the transaction.
Input:  iMaintenanceSalesOrder
The maintenance sales order number
Mandatory input.
iMaintenanceSalesOrderLine
The maintenance sales order part line for which
the actual received quantity must be registered.
Mandatory input.
iReceivedQuantity
The Received Quantity.
Mandatory input when the Part Maintenance Line is for
an anonymous item. When the Part Maintenance Line is for
a serialized item, the received quantity is defaulted
with 1.0.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - No Error
<> 0                          - Error situation
```
