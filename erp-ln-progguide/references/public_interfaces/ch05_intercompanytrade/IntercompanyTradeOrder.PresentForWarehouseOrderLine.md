# IntercompanyTradeOrder.PresentForWarehouseOrderLine

> Chapter: Chapter 5 Public Interfaces for IntercompanyTrade
>
> Group: Public Interfaces for IntercompanyTradeOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 160-163

```baan
DLL:   tcextitrapi
This function is available from     2024.03 (KB2321477  ).
Syntax: long IntercompanyTradeOrder.PresentForWarehouseOrderLine(
domain  tcncmp           iWarehouseOrderCompany,
domain  tckoor           iWarehouseKindOfOrder,
domain  tcorno           iWarehouseOrder,
domain  tcpono           iWarehouseOrderLine,
domain  tcpono           iWarehouseOrderSequence,
domain  tcyesno          iMultiCompanyTransfer,
domain  tcncmp           iShipFromCompany,
domain  tcyesno          iSalesTrade,
domain  tcyesno          iPurchaseTrade,
boolean          iCheckSecurity,
domain  tcyesno          iExcludeCancelled,
domain  tcmcs.str132     i.calling.api,
ref             boolean          oIntercompanyTradeOrderPresent,
ref     domain  tcncmp           oTradeOrderCompany,
ref     domain  tcorno           oTradeOrder,
ref     domain  tcpono           oTradeOrderLine,
ref     domain  tcyesno          oTradeTransactions,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function checks if a intercompany trade order is present
for the Warehouse Order Line.
Pre:    N.A.
Post:   N.A.
Input:  iWarehouseOrderCompany                - Warehouse Order Company (Mandatory)
iWarehouseKindOfOrder                         - Warehouse Kind of Order (Mandatory)
iWarehouseOrder                               - Warehouse Order (Mandatory)
iWarehouseOrderLine                           - Warehouse Order Line
iWarehouseOrderSequence                       - Warehouse Order Sequence
iMultiCompanyTransfer                         - Multi Company Transfer (Mandatory)
iShipFromCompany                              - ShipFromCompany
(Mandatory when iMultiCompanyTransfer
has value Yes)
iSalesTrade                                   - Sales Trade (Mandatory)
iPurchaseTrade                                - Purchase Trade (Mandatory)
iCheckSecurity                                - Check Security (Mandatory)
iExcludeCancelled                             - Exclude Cancelled (Mandatory)
Output: oIntercompanyTradeOrderPresent
-                                               Intercompany Trade Order Present
oTradeOrderCompany                            - Trade Order Company
oTradeOrder                                   - Trade Order
oTradeOrderLine                               - Trade Order Line
oTradeTransactions                            - Trade Transactions
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
Return: 0: OK, <> 0: Error
```

## Chapter 6 Public Interfaces for Item

## Public Interfaces for Item

The following functions are available: Item.ChangeOutboundMethod Item.ConvertItemToPlanItem Item.ConvertPlanItemToItem Item.Copy Item.CopySiteData Item.CreateSerialNumber Item.GetCostingData Item.GetData Item.GetLotSerialRegistration Item.GetOrderingData Item.GetPlanningTimeFenceDate Item.GetProductionData Item.GetPurchaseData Item.GetRevision Item.GetSalesData Item.GetServiceData Item.GetSupplier Item.GetWarehousingData Item.InsertSerialNumber Item.ProjectPegAllowed Item.StartCopy Item.StartDetail Item.StartMultiMain Item.StartOverview Item.StartWhereUsedComponent
