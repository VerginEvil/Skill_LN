# ProjectCostPegTransfer.CheckInventoryAvailable

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectCostPegTransfer
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1099-1100

```baan
DLL:   whextwmdapi
This function is available from 2023.09 (KB2304786).
Syntax: long ProjectCostPegTransfer.CheckInventoryAvailable(
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tccwar           iWarehouse,
domain  tccprj           iProject,
domain  tcpdm.cspa       iElement,
domain  tcpdm.cact       iActivity,
domain  tcowns           iOwnership,
domain  tcqiv1           iTransferQuantity,
domain  whinh.cptt       iTransferType,
ref     domain  whinh.cptt       oTransferType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface checks if there is enough inventory
available to transfer a cost peg.
Pre:    N.a.
Post:   N.a.
Input:  iItem - Item (mandatory)
iEffectivityUnit - Effectivity Unit
iWarehouse - Warehouse (mandatory)
iProject - Project
iElement - Element
iActivity - Activity
iOwnership - Ownership
iTransferQuantity - Transfer Quantity
iTransferType - Cost peg transfer type
Output: oTransferType - Cost peg transfer type, switched if only
'Permanent' is allowed.
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Inventory is available to be transferred
<> 0    - Error
```
