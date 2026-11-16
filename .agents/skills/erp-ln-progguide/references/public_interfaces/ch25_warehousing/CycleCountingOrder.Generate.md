# CycleCountingOrder.Generate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for CycleCountingOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 916-918

```baan
DLL:   whextinhapi
This function is available from 2022.10 (KB2261934).
Syntax: long CycleCountingOrder.Generate(
domain  tcsite           iSiteFrom,
domain  tcsite           iSiteTo,
domain  tccwar           iWarehouseFrom,
domain  tccwar           iWarehouseTo,
domain  whloca           iLocationFrom,
domain  whloca           iLocationTo,
domain  tccom.bpid       iLocationOwnerFrom,
domain  tccom.bpid       iLocationOwnerTo,
domain  tcdate           iInventoryDateFrom,
domain  tcdate           iInventoryDateTo,
domain  whwmd.zone       iZoneFrom,
domain  whwmd.zone       iZoneTo,
domain  whwmd.strt       iRowFrom,
domain  whwmd.strt       iRowTo,
domain  whwmd.coln       iLevelFrom,
domain  whwmd.coln       iLevelTo,
domain  whwmd.rack       iBinFrom,
domain  whwmd.rack       iBinTo,
domain  tccitg           iItemGroupFrom,
domain  tccitg           iItemGroupTo,
domain  tcclot           iLotFrom,
domain  tcclot           iLotTo,
domain  whhuid           iHandlingUnitFrom,
domain  whhuid           iHandlingUnitTo,
domain  tcdate           iLastCountingDateFrom,
domain  tcdate           iLastCountingDateTo,
domain  tcabcc           iABCCodeFrom,
domain  tcabcc           iABCCodeTo,
domain  tcamnt           iInventoryValueFrom,
domain  tcamnt           iInventoryValueTo,
domain  tcccur           iCurrency,
domain  tcrtyp           iRateType,
domain  tcitem           iItemFrom,
domain  tcitem           iItemTo,
boolean          iReconciliation,
boolean          iForceCycleCount,
boolean          iExcludeLocationAllocatedItems,
boolean          iCountBasedOnInventoryValue,
boolean          iCountNewItems,
boolean          iCountNonHandlingUnitInventory,
boolean          iCountHandlingUnitInventory,
domain  whinh.cchu       iHandlingUnitLevel,
boolean          iOnlyCompleteHandlingUnitTopLevels,
domain  whinh.ccmihu     iMultiItemHandlingUnits,
domain  tcseri           iSeries,
domain  tcqcia           iMaximumNumberOfLinesPerOrder,
domain  tcqcia           iMaximumNumberOfStockPoints,
ref             long             oNumberOfCreatedLines,
ref     domain  tcorno           oOrderArray() fixed,
ref     domain  tcsern           oCountNumberArray(),
ref     domain  tcpono           oOrderLineArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates cycle counting orders.
Be aware that transaction management is handled within this
function.
Pre:    oOrderArray, oCycleCountNumberArray and oOrderLineArray must be
declared as based variables. This function will allocate the
memory.
Post:   N.a.
Input:  iSiteFrom - Optional
iSiteTo - Mandatory
iWarehouseFrom - Optional
iWarehouseTo - Mandatory
iLocationFrom - Optional
iLocationTo - Mandatory
iLocationOwnerFrom - Optional
iLocationOwnerTo - Mandatory
iInventoryDateFrom - Optional
iInventoryDateTo - Mandatory
iZoneFrom - Optional
iZoneTo - Mandatory
iRowFrom - Optional
iRowTo - Mandatory
iLevelFrom - Optional
iLevelTo - Mandatory
iBinFrom - Optional
iBinTo - Mandatory
iItemGroupFrom - Optional
iItemGroupTo - Mandatory
iLotFrom - Optional
iLotTo - Mandatory
iHandlingUnitFrom - Optional
iHandlingUnitTo - Mandatory
iLastCountingDateFrom - Optional
iLastCountingDateTo - Mandatory
iABCCodeFrom - Optional
iABCCodeTo - Mandatory
iInventoryValueFrom - Optional
iInventoryValueTo - Mandatory
iCurrency - Optional
iRateType - Optional
iItemFrom - Optional
iItemTo - Mandatory
iReconciliation - When this is set to True, the discrepancies
will be reconciled between ERP LN and the WMS system.
iForceCycleCount -  When this is set to True, all stock points
found in the selection are added to a cycle count order.
iExcludeLocationAllocatedItems -  When this is set to True,
ERP LN does not generate a cycle count order line for
stock points with location allocated inventory.
iCountBasedOnInventoryValue - When this is set to True, the
InventoryValue range will be used and applied.
iCountNewItems -  When this is set to True, cycle counting order
lines are generated for new items that were earlier
never handled in the logistic process
iCountNonHandlingUnitInventory -  When this is set to True,
inventory that is not stored in handling units is
counted.
iCountHandlingUnitInventory - When this is set to True,
inventory that is stored in handling units is counted
iHandlingUnitLevel - Mandatory
Allowed Values:
- Count Handling Unit Top Levels
(whinh.cchu.top.level)
- Count Handling Unit Bottom Levels
(whinh.cchu.bottom.level)
iOnlyCompleteHandlingUnitTopLevels - When this is set to True,
cycle counting orders are generated for top-level
handling units for which the Complete and Labeled check
boxes are selected in the Handling Units session.
When this is set to False, cycle counting orders are
generated for top-level handling units regardless of the
settings of the Complete and Labeled check boxes in the
Handling Units session.
iMultiItemHandlingUnits - Mandatory
Allowed Values:
- Include
(whinh.ccmihu.include)
- Exclude
(whinh.ccmihu.exclude)
- Only
(whinh.ccmihu.only)
iSeries - Optional
iMaximumNumberOfLinesPerOrder - Mandatory
iMaximumNumberOfStockPoints - Mandatory
Output: oNumberOfCreatedLines - Number of Created Cycle Counting Order
Lines
oOrderArray - Array with created Orders
oCycleCountNumberArray - Array with created Cycle Count Numbers
oOrderLineArray - Array with created Cycle Counting Order Lines
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Success
<> 0    - Error
```
