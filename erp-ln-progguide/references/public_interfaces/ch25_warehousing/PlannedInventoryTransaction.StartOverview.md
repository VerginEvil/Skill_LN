# PlannedInventoryTransaction.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PlannedInventoryTransaction
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 926-929

```baan
DLL:   whextinpapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long PlannedInventoryTransaction.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tckoor           iOriginatingTypeOfOrder,
domain  tcorno           iOrder,
domain  tckotr           iTransactionType,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcpono           iBillOfMaterialLine,
domain  tcpono           iDistributionLine,
domain  tcuef.effn       iEffectivityUnit,
domain  tcitem           iItem,
domain  tctrns.date      iTransactionDate,
domain  tcmcs.long       iOrderPriority,
domain  tccwar           iWarehouse,
domain  tccprj           iProject,
domain  tcpdm.cspa       iElement,
domain  tcpdm.cact       iActivity,
domain  tcptc.cstl       iExtension,
domain  tccpcp           iCostComponent,
ref     domain  tckoor           oOriginatingTypeOfOrder,
ref     domain  tcorno           oOrder,
ref     domain  tckotr           oTransactionType,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderLineSequence,
ref     domain  tcpono           oBillOfMaterialLine,
ref     domain  tcpono           oDistributionLine,
ref     domain  tcuef.effn       oEffectivityUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the overview session Planned Inventory
Transactions (whinp1500m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"byOriginatingTypeOfOrder":
data is displayed by Originating Type of Order
session will be started on index 1
view field: Originating Type of Order
"byItemTransactionDate":
data is displayed by Item and Transaction Date
session will be started on index 2
view field: Item
"byItemEffectivityUnit":
data is displayed by Item and Effectivity Unit
session will be started on index 3
view field: Item
"byItemWarehouse":
data is displayed by Item and Warehouse
session will be started on index 4
view fields: Item and Warehouse
"byProjectOrder":
data is displayed by Project, Element, Activity,
and Order fields
session will be started on session index 5
view field: Project
"byItemEffectivityUnitProject":
data is displayed by Item and Effectivity Unit
and Project related fields
session will be started on index 6
view field: Item
"byProjectPeggedOrderLine":
data is displayed by Order fields
session will be started on session index 7
view fields: Originating Type of Order, Order,
Line, Sequence and Transaction Type
"byWarehouseItem":
data is displayed by Warehouse and Item
session will be started on index 8
view field: Warehouse
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
iQueryExtend
A specific query to be used when zooming to this session.
iOriginatingTypeOfOrder
Mandatory when iStartFilter "byOriginatingTypeOfOrder" or
"byProjectPeggedOrderLine" is used or iSessionIndex is
1 or 7 and iStartMode is MODELESS
iOrder
Mandatory when iStartFilter "byProjectPeggedOrderLine"
is used or iSessionIndex = 7, and iStartMode is MODELESS
iTransactionType
Mandatory when iStartFilter "byProjectPeggedOrderLine"
is used or iSessionIndex = 7, and iStartMode is MODELESS
iOrderLine
Optional.
iOrderLineSequence
Optional.
iBillOfMaterialLine
Optional
iDistributionLine
Optional
iEffectivityUnit
Optional.
iItem
Mandatory when iStartFilter "byItemTransactionDate",
"byItemEffectivityUnit", "byItemWarehouse" or
"byItemEffectivityUnitProject" is used or when
iSessionIndex = 2, 3, 4 or 6 and iStartMode is MODELESS
iTransactionDate
Optional.
iOrderPriority
Optional.
iWarehouse
Optional.
iProject
Optional.
iElement
Optional.
iActivity
Optional.
iExtension
Optional.
iCostComponent
Optional.
Output: for iStartMode MODAL:
oOriginatingTypeOfOrder                       - Originating Order Type of
selected transaction
oOrder                                        - Order of selected transaction
oTransactionType                              - Transaction type of selected
transaction
oOrderLine                                    - Order Line of selected transaction
oOrderLineSequence                            - Order Line Sequence of selected
transaction
oBillOfMaterialLine                           - BOM Line of selected transaction
oDistributionLine                             - Distribution Line of selected
transaction
oEffectivityUnit                              - Effectivity unit of selected
transaction
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

## Public Interfaces for Inventory

The following functions are available: Inventory.CalculateTimePhasedAvailability Inventory.ChangeMAUC Inventory.ChangeMAUCCostDetails Inventory.CheckAndRepair Inventory.DetermineCompanyOwnedValueDependingOnValuationBasis Inventory.DetermineQuantity Inventory.DetermineQuantityAndValue Inventory.DetermineQuantityAndValueV2 Inventory.GetAnonymousInventoryQuantities Inventory.GetTimePhasedAvailability Inventory.GetTimePhasedAvailabilityV2 Inventory.ProcessVariances Inventory.Start360
