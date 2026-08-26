# SupplierStagePaymentLine.Release

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for SupplierStagePaymentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 480-481

```baan
DLL:   tdextpurapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long SupplierStagePaymentLine.Release(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iStagePaymentLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to release a supplier stage payment
line that is linked to a purchase order line or purchase order.
If ION Workflow Document Approval is used, then the following
applies:
* After executing this Public Interface, the status
update must be approved in ION Workflow Document Approval.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder          Purchase Order (Mandatory)
This is the Purchase Order number for
which the Supplier Stage Payment Line
must be released.
iOrderLine              Purchase Order Line (Mandatory)
This is the Purchase Order Line for
which the Supplier Stage Payment Line
must be released. When releasing a order
based Supplier Stage Payment Line you
must set this to 0.
iStagePaymentLine       Stage Payment Line (Mandatory)
This is the specific Supplier Stage
Payment Line to be released.
This input field expects a numeric value.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
