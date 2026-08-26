# PlannedProductionOrder.Transfer

> Chapter: Chapter 16 Public Interfaces for Planning
>
> Group: Public Interfaces for PlannedProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 563-564

```baan
DLL:   cpextrrpapi
This function is available from     2022.11 (KB2263675  ).
Syntax: long PlannedProductionOrder.Transfer(
domain  cprrp.orno       iPlannedProductionOrder,
domain  tcseri           iOrderSeries,
boolean          iTransferText,
ref     domain  tcorno           oProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface transfers iPlannedProductionOrder, which
must exist in the Actual Scenario. The created Shop Floor
Production Order is returned in oProductionOrder.
Transaction management is handled by this Public Interface.
Pre:                  -
Post:                 -
Input:  iPlannedProductionOrder                       - The Planned Production Order
to be transferred (Mandatory).
iOrderSeries                                          - The first free number to be
used to create the new
Production Order (Optional).
iTransferText                                         - If true, the text of the
Planned Production Order will
be transferred.
Output: oProductionOrder                              - The Order number of the
created Production Order.
Return:    0                            Planned Order successfully
transferred
<> 0                            Otherwise.
```

## Public Interfaces for PlannedPeggingRelations

The following functions are available: PlannedPeggingRelations.FindDemandForOrder PlannedPeggingRelations.FindDemandForOrderV2 PlannedPeggingRelations.FindSupplyForOrder PlannedPeggingRelations.FindSupplyForOrderV2 PlannedPeggingRelations.RetrievePurchaseRelated PlannedPeggingRelations.RetrieveSalesRelated
