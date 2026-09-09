# Inventory.CalculateTimePhasedAvailability

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 939-940

```baan
DLL:   whextinpapi
This function is available from 2023.09 (KB2300987).
Syntax: long Inventory.CalculateTimePhasedAvailability(
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tccwar           iWarehouse,
domain  tcemm.clus       iCluster,
domain  tcguid           iSpecification,
domain  tctrns.date      iDate,
domain  tcyesno          iSkipPlannedReceipts,
ref     domain  tcqiv1           oAvailableQuantity,
ref     domain  tcqiv1           oCurrentlyBlockedQuantity,
ref     domain  tccuni           oInventoryUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will read the available quantity and
the currently blocked quantity from table
Warehouse - Item Inventory (whwmd215).
The available quantity will be calculated up to and
including the given date (whwmd215 + whinp100).
Depending on the values of warehouse and cluster
the following inventory is calculated:
Warehouse       Cluster         Result
------------------------------------------
""              Filled          1
""              ""              2
Filled          Any value       3
1 = Aggregated inventory in the specified cluster
2 = Aggregated inventory in the empty cluster.
3 = Inventory in the specified warehouse
Only warehouses of type Normal, Shop Floor and
Consignment are taken into account.
If specification is filled, then the inventory
levels will not be read from table whwmd215 but
from table whwmd219 (Inventory by Specification).
Input:  iItem                   - Item (Mandatory)
iEffectivityUnit        - Effectivity Unit (Optional)
iWarehouse              - Warehouse (Optional)
iCluster                - Cluster (Optional)
iSpecification          - Specification (Optional)
iDate                   - Date (Mandatory)
iSkipPlannedReceipts    - Skip planned receipts (Yes/No)
Output: oAvailableQuantity      - Available quantity expressed in the
inventory unit.
oCurrentlyBlockedQuantity -
Currently blocked quantity expressed
in the inventory unit.
oInventoryUnit          - Inventory Unit
Return: 0                       - Inventory availability could not be
calculated.
<> 0                    - Error
```
