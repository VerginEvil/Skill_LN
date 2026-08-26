# ProjectPeggedInventory.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectPeggedInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1221-1223

```baan
DLL:   whextwmdapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long ProjectPeggedInventory.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccwar           iWarehouse,
domain  tccprj           iProject,
domain  tcitem           iItem,
domain  tcuef.effn       iEffectivityUnit,
domain  tcpdm.cspa       iElement,
domain  tcpdm.cact       iActivity,
domain  tcptc.cstl       iExtension,
domain  tccpcp           iCostComponent,
ref     domain  tccwar           oWarehouse,
ref     domain  tccprj           oProject,
ref     domain  tcitem           oItem,
ref     domain  tcuef.effn       oEffectivityUnit,
ref     domain  tcpdm.cspa       oElement,
ref     domain  tcpdm.cact       oActivity,
ref     domain  tcptc.cstl       oExtension,
ref     domain  tccpcp           oCostComponent,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts session Project Pegged Inventory
(whwmd2560m000) in Overview Mode.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, in case of a
multi                                              -occurrence the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byWarehouseProject":
data is displayed by Warehouse and Project
session will be started on index 1
view field: Warehouse
"byWarehouseItemEffectivityUnit":
data is displayed by Warehouse, Item and
Effectivity Unit
session will be started on index 2
view field: Warehouse
"byWarehouseProjectPeg":
data is displayed by Warehouse and Project Peg
session will be started on index 3
view field: Warehouse
"byItemEffectivityUnitProject":
data is displayed by Item, Effectivity Unit and Project
session will be started on index 4
view field: Item
"byItemEffectivityUnitWarehouse":
data is displayed by Item, Effectivity Unit and
Warehouse
session will be started on index 5
view field: Item
"byProjectWarehouse":
data is displayed by Project and Warehouse
session will be started on index 6
view field: Project
"byProjectPeg":
data is displayed by Project Peg
session will be started on index 7
view field: Project
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iWarehouse
Mandatory if iStartMode = MODELESS and
iSessionIndex = 1, 2 or 3
(or iStartFilter = "byWarehouseProject"
or iStartFilter = "byWarehouseItemEffectivityUnit"
or iStartFilter = "byWarehouseProjectPeg")
iProject
Mandatory if iStartMode = MODELESS and
iSessionIndex = 6 or 7
(or iStartFilter = "byProjectWarehouse"
or iStartFilter = "byProjectPeg")
iItem
Mandatory if iStartMode = MODELESS and
iSessionIndex = 4 or 5
(or iStartFilter = "byItemEffectivityUnitProject"
or iStartFilter = "byItemEffectivityUnitWarehouse")
iEffectivityUnit
Optional
iElement
Optional
iActivity
Optional
iExtension
Optional
iCostComponent
Optional
Output:
oWarehouse                                    - Warehouse of the selected record,
if iStartMode = MODAL.
oProject                                      - Project of the selected record,
if iStartMode = MODAL.
oItem                                         - Item of the selected record,
if iStartMode = MODAL.
oEffectivityUnit                              - Effectivity Unit of the selected
record, if iStartMode = MODAL.
oElement                                      - Element of the selected record,
if iStartMode = MODAL.
oActivity                                     - Activity of the selected record,
if iStartMode = MODAL.
oExtension                                    - Extension of the selected record,
if iStartMode = MODAL.
oCostComponent                                - Cost Component of the selected record,
if iStartMode = MODAL.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for OutboundOrderLineActivity

The following functions are available: OutboundOrderLineActivity.Create OutboundOrderLineActivity.ModifyAutomaticProcessing
