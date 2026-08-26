# Inventory.GetAnonymousInventoryQuantities

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 946-947

```baan
DLL:   whextwmdapi
This function is available from     2021.10 (KB2210123  ).
Syntax: long Inventory.GetAnonymousInventoryQuantities(
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcinvt.date      iInventoryDate,
domain  tccuni           iStorageUnit,
domain  whwmd.pkdf       iPackageDefinition,
ref     domain  tcqst1           oQuantityOnHand,
ref     domain  tcqst1           oQuantityAvailable,
ref     domain  tcqst1           oQuantityAllocated,
ref     domain  tcqst1           oQuantityBlocked,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface returns the anonymous stock quantities of
the specified stock point divided in available, allocated and
blocked stock.
This function only returns the quantities for the specified
inventory structure record.
Pre:    N.A.
Post:   N.A.
Input:  iWarehouse                            - Warehouse (Mandatory)
iLocation                                     - Location (Mandatory, if warehouse
and item are location controlled)
iItem                                         - Item (Mandatory)
iLot                                          - Lot
iInventoryDate                                - Inventory Date
iStorageUnit                                  - Storage Unit (Mandatory)
iPackageDefinition                            - Package definition
Only fixed package definitions are
allowed.
Output: oQuantityOnHand                       - Quantity On Hand
oQuantityAvailable                            - Quantity Available
oQuantityAllocated                            - Quantity Allocated
oQuantityBlocked                              - Quantity Blocked
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Success
<> 0                                          - Error
```
