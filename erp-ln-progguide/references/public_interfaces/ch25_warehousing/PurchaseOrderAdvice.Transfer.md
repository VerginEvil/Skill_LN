# PurchaseOrderAdvice.Transfer

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PurchaseOrderAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1295-1296

```baan
DLL:   whextinaapi
This function is available from     2023.01 (KB2271572  ).
Syntax: long PurchaseOrderAdvice.Transfer(
domain  tcorno           iPurchaseOrderAdvice,
domain  tcseri           iOrderSeries,
domain  tcseri           iDirectDeliverySeries,
domain  tccotp           iOrderType,
domain  tccotp           iDirectDeliveryOrderType,
domain  tccotp           iDirectDeliveryReturnOrderType,
ref     domain  tcorno           oPurchaseOrderOrSchedule,
ref     domain  tcpur.otyp       oOrderType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will transfer a purchase advice to a
purchase order or purchase schedule. This depends on the set                      -up
in the purchase module.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iPurchaseOrderAdvice
The purchase order advice which needs to be transferred.
This is mandatory to fill.
iOrderSeries
The order series which has to be used when the advice
is transferred to a purchase order. If empty the
default order series will be used.
iDirectDeliverySeries
The direct delivery order series which has to be used
when the advice is transferred to a direct delivery
purchase order. If empty the default direct delivery
order series will be used.
iOrderType
The order type which has to be used when the advice
is transferred to a purchase order. If empty the
default order type will be used.
iDirectDeliveryOrderType
The direct delivery order type which has to be used when
the advice is transferred to a direct delivery purchase
order. If empty the default direct delivery order type
will be used.
iDirectDeliveryReturnOrderType
The direct delivery return order type which has to be
used when the advice is transferred to a direct delivery
return purchase order. If empty the default direct
delivery return order type will be used.
Output: oPurchaseOrderOrSchedule
The purchase order or purchase schedule to which the
purchase advice is transferred.
oOrderType
The purchase order or purchase schedule indicator
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0               - The purchase order advice has been transferred successfully.
<> 0                       - Error. The purchase order advice could not be transferred.
```

## Public Interfaces for ProductionOrderAdvice

The following functions are available: ProductionOrderAdvice.StartDetail ProductionOrderAdvice.StartOverview ProductionOrderAdvice.Transfer
