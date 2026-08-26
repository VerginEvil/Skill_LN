# PurchaseOrderMaterialSupplyLine.DeleteSupplyOrder

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderMaterialSupplyLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 474-475

```baan
DLL:   tdextpurapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long PurchaseOrderMaterialSupplyLine.DeleteSupplyOrder(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcpono           iMaterialSupplyLineSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to delete a supply order for the given
purchase order material supply line.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder          Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iOrderLineSequence      Purchase Order Line Sequence (Mandatory)
iMaterialSupplyLineSequence
Material Supply Line Sequence (Mandatory)
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
