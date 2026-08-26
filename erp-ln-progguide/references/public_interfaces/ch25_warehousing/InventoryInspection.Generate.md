# InventoryInspection.Generate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1275-1277

```baan
DLL:   whextinhapi
This function is available from     2023.08 (KB2296967  ).
Syntax: long InventoryInspection.Generate(
domain  tcsite           iSiteFrom,
domain  tcsite           iSiteTo,
domain  tccwar           iWarehouseFrom,
domain  tccwar           iWarehouseTo,
domain  whloca           iLocationFrom,
domain  whloca           iLocationTo,
domain  tccom.bpid       iLocationOwnerFrom,
domain  tccom.bpid       iLocationOwnerTo,
domain  tccom.bpid       iBuyFromBusinessPartnerFrom,
domain  tccom.bpid       iBuyFromBusinessPartnerTo,
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
domain  tcibd.sern       iSerialNumberFrom,
domain  tcibd.sern       iSerialNumberTo,
domain  whhuid           iHandlingUnitFrom,
domain  whhuid           iHandlingUnitTo,
domain  tcdate           iLastInventoryInspectionDateFrom,
domain  tcdate           iLastInventoryInspectionDateTo,
domain  tcitem           iItemFrom,
domain  tcitem           iItemTo,
boolean          iInspectNonHandlingUnitInventory,
boolean          iInspectHandlingUnitInventory,
domain  whinh.cchu       iHandlingUnitLevel,
boolean          iForceInventoryInspection,
boolean          iExcludeLocationAllocatedItems,
domain  tcltmo           iLeadTime,
domain  tctope           iLeadTimeUnit,
domain  tcseri           iSeries,
ref             long             oNumberOfGeneratedInspections,
ref     domain  tcorno           oInspectionArray() fixed,
ref     domain  tcpono           oInspectionSequenceArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates inventory inspection lines based on
Stock Point Inventory data and based on Handling Units.
Be aware that transaction management is handled within this
function.
Pre:    N.A.
Post:   N.A.
Input:  iSiteFrom               - Optional
iSiteTo                       - Mandatory
iWarehouseFrom                       - Optional
iWarehouseTo                       - Mandatory
iLocationFrom                       - Optional
iLocationTo                       - Mandatory
iLocationOwnerFrom                       - Optional
iLocationOwnerTo                       - Mandatory
iBuyFromBusinessPartnerFrom                       - Optional
iBuyFromBusinessPartnerTo                       - Mandatory
iInventoryDateFrom                       - Optional
iInventoryDateTo                       - Mandatory
iZoneFrom                       - Optional
iZoneTo                       - Mandatory
iRowFrom                       - Optional
iRowTo                       - Mandatory
iLevelFrom                       - Optional
iLevelTo                       - Mandatory
iBinFrom                       - Optional
iBinTo                       - Mandatory
iItemGroupFrom                       - Optional
iItemGroupTo                       - Mandatory
iLotFrom                       - Optional
iLotTo                       - Mandatory
iSerialNumberFrom                       - Optional
iSerialNumberTo                       - Mandatory
iHandlingUnitFrom                       - Optional
iHandlingUnitTo                       - Mandatory
iLastInventoryInspectionDateFrom                       - Optional
iLastInventoryInspectionDateTo                       - Mandatory
iItemFrom                       - Optional
iItemTo                       - Mandatory
iInspectNonHandlingUnitInventory                       - When this is set to True,
inventory that is not stored in handling units is
inspected.
iInspectHandlingUnitInventory                       - When this is set to True,
inventory that is stored in handling units is inspected
iHandlingUnitLevel                       - Mandatory
Allowed Values:
-                                       Inspect Handling Unit Top Levels
(whinh.cchu.top.level)
-                                       Inspect Handling Unit Bottom Levels
(whinh.cchu.bottom.level)
iForceInventoryInspection                       - When this is set to True, all
stock points found in the selection are inspected.
When set to False, the stock points due for inspection
according the planned inspection date and frequency of
inventory inspection are inspected.
iExcludeLocationAllocatedItems                       -  When this is set to True,
ERP LN does not generate inventory inspections for
stock points with location allocated inventory.
iLeadTime                       - Optional
iLeadTimeUnit                       - Mandatory
Allowed Values:
-                                       Hours (tctope.hours)
-                                       Days (tctope.days)
iSeries                       - Optional
Output:
oNumberOfGeneratedInspections                       - Number of generated inventory
inspections
oInspectionArray                       - Array with generated inventory inspection
numbers.
This array must be declared as a based variable; this
function will allocate the memory
oInspectionSequenceArray                       - Array with generated inventory
inventory sequences.
This array must be declared as a based variable; this
function will allocate the memory
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Success
<> 0                          - Error
```

## Public Interfaces for HandlingUnitStockPointDetail

The following functions are available: HandlingUnitStockPointDetail.Inspect HandlingUnitStockPointDetail.SplitForSerial
