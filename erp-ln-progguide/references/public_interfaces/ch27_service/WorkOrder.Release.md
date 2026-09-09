# WorkOrder.Release

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1510-1511

```baan
DLL:   tsextwcsapi
This function is available from 2020.12 (KB2162018).
Syntax: long WorkOrder.Release(
domain  tcorno           iWorkOrder,
domain  tsmdm.acln       iWorkOrderActivityLine,
domain  tccotp           iPurchaseOrderType,
domain  tcseri           iPurchaseOrderSeries,
domain  tcyesno          iATPCheck,
domain  tcyesno          iCheckPlannedInventory,
domain  tcyesno          iCheckInventoryOnHand,
domain  tcyesno          iSkipBlockedInventory,
domain  tsmdm.scin       iScopeOfInventoryCheck,
domain  tcyesno          iBlockInCaseOfInventoryShortage,
domain  tcyesno          iUpdatePlannedDeliveryTimeMaterialLine,
domain  tcyesno          iUpdateOrderActivityWithLastPlannedMaterialLine,
domain  tcyesno
iSynchronizeMaterialLinesWithLastPlannedMaterialLine,
domain  tcgen.ynds       iAutomaticItemReceipt,
domain  tcyesno          iUpdatePlannedQuantityToIssuedQuantity,
domain  tcyesno          iShiftWorkOrderToActualReceiptTime,
domain  tcyesno          iCheckAssignments,
domain  tcyesno          iCheckSkills,
ref     domain  tcyesno          oMaintenanceSalesOrderBlocked,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the release of a work order.
When iWorkOrderActivityLine is filled, the work order will be
released and next only this specific work order activity line
will be released.
Based on the given options/settings for releasing the work order
additional checks related to inventory availability are done, as
well as checks on the presence of assignments and skills.
When 'automatic item receipt' is set to a value other than no,
the work order item is first issued to the repair shop before
releasing the work item.
Before releasing the work order, order blocking checks are done,
if defined in the Maintenance Sales Control parameters or
service office settings, based on which the linked maintenance
sales order can be blocked.
When the linked maintenance sales order is set to blocked, the
work order cannot be released. In that case output argument
oMaintenanceSalesOrderBlocked will be set to 'yes' as the
maintenance sales order is blocked. However releasing the work
order is not successfull.
Pre:    None.
Post:   This function sets a retry-point and will commit and/or abort
the transaction.
Input:  iWorkOrder
Work Order. (mandatory)
iWorkOrderActivityLine
Work Order Activity Line. (optional)
iPurchaseOrderType
Purchase Order Type. (not mandatory)
iPurchaseOrderSeries
Purchase Order Series. (not mandatory)
iATPCheck
Perform ATP check. (mandatory Yes/No)
iCheckPlannedInventory
Check Planned Available Inventory. (mandatory Yes/No)
iCheckInventoryOnHand
Check On Hand Inventory. (mandatory Yes/No)
iSkipBlockedInventory
Skip Blocked Inventory. (mandatory Yes/No)
iScopeOfInventoryCheck
Scope of Inventory Check. (mandatory)
Possible values:
- current warehouse only
- all warehouses in planning cluster
iBlockInCaseOfInventoryShortage
Block Planning or Releasing of Orders with Shortages.
(mandatory Yes/No)
iUpdatePlannedDeliveryTimeMaterialLine
Update Planned Delivery Time of Material Lines.
(mandatory Yes/No)
iUpdateOrderActivityWithLastPlannedMaterialLine
Update Activities and Orders with Latest Planned.
Material Line (mandatory Yes/No)
iSynchronizeMaterialLinesWithLastPlannedMaterialLine
Synchronize Materials with Latest Planned Material Line.
(mandatory Yes/No)
iAutomaticItemReceipt
Automatic Item Receipt. (mandatory)
Possible values:
- yes
- no
- use default settings
iUpdatePlannedQuantityToIssuedQuantity (Yes/No)
Update Planned Quantity to Issued Quantity.
(mandatory Yes/No)
iShiftWorkOrderToActualReceiptTime
Shift Work Order to Actual Receipt Time.
(mandatory Yes/No)
iCheckAssignments
Check Assignments. (mandatory Yes/No)
iCheckSkills
Check Skills. (mandatory Yes/No)
Output: oMaintenanceSalesOrderBlocked
Indicates if the maintenance sales order linked to the
work order is set to blocked.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - release succesfull
<> 0    - Error during release occurred
```
