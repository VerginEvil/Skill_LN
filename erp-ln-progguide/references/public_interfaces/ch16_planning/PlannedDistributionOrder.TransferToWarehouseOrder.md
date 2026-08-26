# PlannedDistributionOrder.TransferToWarehouseOrder

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedDistributionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 581-583

```baan
DLL:   cpextrrpapi
This function is available from     2024.06 (KB2328640  ).
Syntax: long PlannedDistributionOrder.TransferToWarehouseOrder(
domain  cpcom.plnc       iScenario,
domain  cporno           iDistributionOrder,
boolean          iTransferText,
domain  tccotp           iWarehouseOrderType,
ref     domain  cporno           oCreatedOrderFrom,
ref     domain  cporno           oCreatedOrderTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, a Planned Distribution Order
can be transferred to a Warehouse Order. In the case of an
inter                      -company transfer, one Order is created.
For an Order between companies, two Orders are created,
one in the Supplying company and one in the Receiving company.
Pre:    A db.retry.point should be set.
Post:   Commit or abort the transaction.
Input:  iScenario               The Planning Scenario (Mandatory).
iDistributionOrder      The Planned Distribution Order (Mandatory).
iWarehouseOrderType     The Warehouse Order Type (Mandatory).
iTransferText           If true, the text of the Planned
Distribution Order is also transferred.
Output:
oCreatedOrderFrom       The Supplying Order created. In case of an
inter                                              -company transfer, this is identical
to oCreatedOrderTo.
oCreatedOrderTo         The Receiving Order created. In case of an
inter                                              -company transfer, this is identical
to oCreatedOrderFrom.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The Order was successfully transferred.
<> 0            Errors occurred.
```

## Public Interfaces for PlannedCostPegTransfers

The following functions are available: PlannedCostPegTransfers.StartDetail PlannedCostPegTransfers.StartOverview
