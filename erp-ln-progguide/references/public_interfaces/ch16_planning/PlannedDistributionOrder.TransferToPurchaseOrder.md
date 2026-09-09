# PlannedDistributionOrder.TransferToPurchaseOrder

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedDistributionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 584-585

```baan
DLL:   cpextrrpapi
This function is available from 2024.06 (KB2328640).
Syntax: long PlannedDistributionOrder.TransferToPurchaseOrder(
domain  cpcom.plnc       iScenario,
domain  cporno           iDistributionOrder,
domain  tcseri           iPurchaseOrderSeries,
domain  tccotp           iPurchaseOrderType,
boolean          iTransferText,
boolean          iRequestForQuotation,
ref     domain  cporno           oCreatedOrderFrom,
ref     domain  cporno           oCreatedOrderTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, a Planned Distribution Order can be
transferred to a Purchase Order. In the Supplying company,
a Sales Order is created, in the Receiving company,
a Purchase Order is created.
Pre:    A db.retry.point should be set.
Post:   Commit or abort the transaction.
Input:  iScenario               The Planning Scenario (Mandatory).
iDistributionOrder      The Planned Distribution Order (Mandatory).
iPurchaseOrderSeries    The Order Series of the to be created
Purchase Order (Mandatory).
iPurchaseOrderType      The Purchase Order Type (Mandatory).
iTransferText           If true, the text of the Planned
Distribution Order is also transferred.
iRequestForQuotation    If true, a request for quotation
may be generated.
Output:
oCreatedOrderFrom       The Supplying Order created.
oCreatedOrderTo         The Receiving Order created.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The Order was successfully transferred.
<> 0                    Errors occurred.
```
