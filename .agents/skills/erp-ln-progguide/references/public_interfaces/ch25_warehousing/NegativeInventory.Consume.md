# NegativeInventory.Consume

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for NegativeInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1290-1290

```baan
DLL:   whextwmdapi
This function is available from 2021.10 (KB2205676).
Syntax: long NegativeInventory.Consume(
domain  tccwar           iWarehouse,
domain  whloca           ilocation,
domain  tcitem           iItem,
domain  tcclot           iLot,
domain  tcinvt.date      iInventoryDate,
domain  tcqst1           iQuantity,
domain  tccuni           iStorageUnit,
domain  whwmd.pkdf       iPackageDefinition,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This public interface consumes negative inventory.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iWarehouse              - Warehouse (Mandatory)
iLocation               - Location (Mandatory, if warehouse
and item are location controlled)
iItem                   - Item (Mandatory)
iLot                    - Lot
iInventoryDate          - Inventory Date
iQuantity               - Quantity in Storage Unit (Mandatory)
Must have a positive value.
iStorageUnit            - Storage Unit (Mandatory)
iPackageDefinition      - Package definition
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success
<> 0                    - Error
```
