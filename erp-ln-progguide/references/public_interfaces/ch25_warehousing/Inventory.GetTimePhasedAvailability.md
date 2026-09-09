# Inventory.GetTimePhasedAvailability

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 957-957

```baan
DLL:   whextinpapi
This function is available from 2021.06 (KB2178495).
Syntax: long Inventory.GetTimePhasedAvailability(
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  tcdate           iDate,
ref     domain  tcqiv1           oAvailableQuantity,
ref     domain  tccuni           oInventoryUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the available inventory on the given
date for the given item and warehouse, based on the current
inventory and the planned inventory transactions.
Inventory of a financial warehouse is not taken into account
and will return zero for the available quantity.
Input:  iItem                   - Item          (Mandatory)
iWarehouse              - Warehouse     (Mandatory)
iDate                   - Date          (Mandatory)
Output: oAvailableQuantity      - Available Quantity on the given date
expressed in the inventory unit.
In case the available quantity is
negative, the value zero is returned.
oInventoryUnit          - Inventory unit.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Available Inventory retrieved
<> 0                    - Error
```
