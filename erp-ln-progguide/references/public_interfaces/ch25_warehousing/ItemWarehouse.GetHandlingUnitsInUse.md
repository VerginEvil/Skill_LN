# ItemWarehouse.GetHandlingUnitsInUse

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ItemWarehouse
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 903-903

```baan
DLL:   whextwmdapi
This function is available from     2024.08 (KB3517597  ).
Syntax: long ItemWarehouse.GetHandlingUnitsInUse(
domain  tcncmp           iLogisticCompany,
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
ref     domain  tcyesno          oHandlingUnitsInUse,
ref     domain  tcyesno          oHandlingUnitsInReceipts,
ref     domain  tcyesno          oHandlingUnitsInInboundInspection,
ref     domain  tcyesno          oHandlingUnitsInInventory,
ref     domain  tcyesno          oHandlingUnitsInOutboundInspection,
ref     domain  tcyesno          oHandlingUnitsInShipments,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns information regarding usage of
handling units for combiantion of item and warehouse.
Input:  iLogisticCompany = Logistic Company (Mandatory)
iItem                                 - Item (Mandatory)
iWarehouse                            - Warehouse (Mandatory)
Output: oHandlingUnitsInUse                   - Handling Units in use.
oHandlingUnitsInReceipts                       - Handling Units in use in Receipts
oHandlingUnitsInInboundInspection                       - Handling Units in use in
Inbound Inspection.
oHandlingUnitsInInventory                       - Handling Units in use in Inventory.
oHandlingUnitsInOutboundInspection                       - Handling Units in use
Outbound Inspection.
oHandlingUnitsInShipments = Handling Units in use in Shipments.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0 / DALHOOKERROR
```
