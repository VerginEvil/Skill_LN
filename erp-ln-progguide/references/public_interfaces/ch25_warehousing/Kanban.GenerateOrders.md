# Kanban.GenerateOrders

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Kanban
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1288-1289

```baan
DLL:   whextinhapi
This function is available from     2026.02 (KB3647754  ).
Syntax: long Kanban.GenerateOrders(
domain  tckbid           iKanbanSignal,
domain  whloca           iLocationTo,
domain  tcqiv1           iQuantity,
domain  tcncmp           iCompanyFrom,
domain  tcsupt           iSupplyTypeFrom,
domain  tcsupc           iSupplyCodeFrom,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcseri           iWarehouseOrderSeries,
domain  tccotp           iWarehouseOrderType,
domain  tcseri           iProductionOrderSeries,
domain  tcseri           iPurchaseOrderSeries,
domain  tccotp           iPurchaseOrderType,
domain  tcseri           iSalesOrderSeries,
domain  tccotp           iSalesOrderType,
domain  tcseri           iWarehouseAdviceSeries,
domain  tcseri           iProductionAdviceSeries,
domain  tcseri           iPurchaseAdviceSeries,
domain  tcyesno          iActivateWarehouseTransfer,
domain  tcyesno          iProcessWarehouseTransfer,
domain  tcyesno          iReleaseProductionOrder,
domain  tcyesno          iCombineOrderAdvice,
domain  tcyesno          iConfirmOrderAdvice,
ref     domain  tcorno           oAdvice,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcorno           oOrderNumber,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a warehouse order, a production order,
a purchase order, a warehouse advice, a production advice or
a purchase advice for a specified kanban signal.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iKanbanSignal                   Mandatory
iLocationTo                     Optional
iQuantity                       Optional
iCompanyFrom                    Optional
iSupplyTypeFrom                 Optional
iSupplyCodeFrom                 Optional
iShipFromBusinessPartner        Optional
iWarehouseOrderSeries           Optional
iWarehouseOrderType             Optional
iProductionOrderSeries          Optional
iPurchaseOrderSeries            Optional
iPurchaseOrderType              Optional
iSalesOrderSeries               Optional
iSalesOrderType                 Optional
iWarehouseAdviceSeries          Optional
iProductionAdviceSeries         Optional
iPurchaseAdviceSeries           Optional
iActivateWarehouseTransfer      Optional
iProcessWarehouseTransfer       Optional
iReleaseProductionOrder         Optional
iCombineOrderAdvice             Optional
iConfirmOrderAdvice             Optional
Output: oAdvice
oOrderOrigin
oOrderNumber
oOrderLine
oOrderSequence
Return: 0               - Advice or Order has been created successfully.
DALHOOKERROR                       - Advice/Order could not be created.
```
