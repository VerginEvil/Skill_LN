# InventoryCommitment.GetAvailableQuantityToCommit

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 972-973

```baan
DLL:   whextinpapi
This function is available from 2023.10 (KB2304092).
Syntax: long InventoryCommitment.GetAvailableQuantityToCommit(
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tcguid           iSpecification,
boolean          iForAllocationBuffer,
domain  tccuni           iUnit,
ref     domain  tcqiv1           oAvailableQuantityToCommit,
ref     domain  tccuni           oUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the available to commit quantity
To Commit Quantity =    Quantity on Hand -
Quantity on Hold -
Committed Quantity -
Location Allocated Quantity +
Committed Quantity in Process
Input:  iWarehouse - Warehouse (Mandatory)
iItem - Item (Mandatory)
iEffectivityUnit - Effectivity Unit (Optional)
iSpecification - Specification (Optional)
iForAllocationBuffer - Indicator (true/false) if calculation
must be done for allocation buffer with only allocations
(true). Otherwise specify false. (Mandatory)
iUnit - Unit in which the Quantity to Commit has to be
expressed. When left empty then the inventory unit will
be taken. (Optional)
Output: oAvailableQuantityToCommit - Available quantity to commit
oUnit - The specified unit (i.unit) or when left empty it will
be the inventory unit of the item
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0 - Quantity to Commit is calculated
<> 0 - Error
```
