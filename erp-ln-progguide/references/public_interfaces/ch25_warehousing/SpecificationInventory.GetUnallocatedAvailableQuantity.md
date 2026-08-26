# SpecificationInventory.GetUnallocatedAvailableQuantity

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for SpecificationInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 951-952

```baan
DLL:   whextwmdapi
This function is available from     2023.02 (KB2272169  ).
Syntax: long SpecificationInventory.GetUnallocatedAvailableQuantity(
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
ref     domain  tcqiv1           oUnallocatedAvailableQuantity,
ref     domain  tccuni           oInventoryUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the unallocated available quantity for
an item in a warehouse. When inventory is allocated to a demand
peg, it is not available as unallocated inventory. When
effectivity units are in use, this public interface will
determine if the iEffectivityUnit is interchangeable with the
effectivity unit which is found for the iItem and iWarehouse and
will include the available quantity in the
oAvailableUnalocatedQuantity. When the iEffectivityUnit is
passed as empty (zero) the same rule applies.
Pre:    N.A.
Post:   N.A.
Input:  iWarehouse                            - Warehouse (Mandatory)
iItem                                         - Item (Mandatory)
iEffectivityUnit                              - Effectivity Unit
Output: oUnallocatedAvailableQuantity
-                                               Unallocated available quantity
in Inventory Unit
oInventoryUnit                                - Inventory Unit
Return: 0                                     - Success
<> 0                                          - Error
```

## Public Interfaces for InventoryCommitment

The following functions are available: InventoryCommitment.AllowedForOrderLine InventoryCommitment.CalculateCommitmentDate InventoryCommitment.CalculateCommitmentDateV2 InventoryCommitment.Cancel InventoryCommitment.CommitInventoryToOrderLine InventoryCommitment.ConsumeFromBuffer InventoryCommitment.CreateAllocationBuffer InventoryCommitment.Generate InventoryCommitment.GetAvailableQuantityToCommit
