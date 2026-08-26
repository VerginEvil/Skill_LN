# ServiceOrderActivity.Plan

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1444-1447

```baan
DLL:   tsextsocapi
This function is available from     2023.06 (KB2290749  ).
Syntax: long ServiceOrderActivity.Plan(
domain  tcorno           iServiceOrder fixed,
domain  tsmdm.acln       iActivityLine,
domain  tcyesno          iReplan,
domain  tcyesno          iPerformATPCheck,
domain  tcyesno          iPerformPlannedAvailableCheck,
domain  tcyesno          iPerformOnHandAvailableCheck,
domain  tcyesno          iSkipBlockedInventory,
domain  tcyesno          iBlockPlanningOfOrdersWithShortages,
domain  tsmdm.scin       iInventoryScope,
domain  tcyesno          iUpdatePlannedDeliveryTimeOfMaterialLines,
domain  tcyesno
iUpdateActivitiesAndOrdersWithLatestPlannedMaterialLine,
domain  tcyesno
iSynchronizeMaterialsWithLatestPlannedMaterialLine,
domain  tccotp           iPurchaseOrderTypeNormalDelivery,
domain  tcseri           iPurchaseOrderSeriesNormalDelivery,
domain  tccotp           iPurchaseOrderTypeDirectDelivery,
domain  tcseri           iPurchaseOrderSeriesDirectDelivery,
domain  tccotp           iServicesProcurementOrderType,
domain  tcseri           iServicesProcurementOrderSeries,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to plan one specific Service Order
Activity (tssoc210 record).
If planning does not succeed for whatever reason, this function
will return a value unequal zero and the reason why the
plan action was not successful is present in the
oExceptionMessage and oExceptionID. If planning succeeds then
the value zero is returned. Even if a value zero is returned,
which means that the given activity changed its status to
Planned, the oExceptionMessage can be filled (and
even more information can be present in the oExceptionID),
because the system generates information messages about the
flow of the process.
This interface has the same options as when the user
would select one specific service order activity in session
Service Order Activities (tssoc2110m000) and use the
specific option Plan Activity, which starts session Service
Order Resource Planning (tssoc2260m000).
All the options which are available in the planning session
are also available as input arguments for this
interface function. It can be useful to look at the Help for
session tssoc2260m000.
Note that this interface behaves exactly the same as the
planning session, which means that the same checks are executed
for the input process options as is being done in the planning
session. If a certain combination of input arguments is not
allowed, the user will be notified.
Pre:    db.retry.point must have been set.
Post:   Blocking status of the service order could have been changed.
Status of Service Order Activity could have been changed from
Free to Planned.
Commit/abort the transaction.
Input:  iServiceOrder
Service Order
Mandatory.
iActivityLine
Service Order Activity
Mandatory.
iReplan
If Replan is Yes, Service Order Activity with status
Free, or Planned, are planned or replanned.
If Replan is No, only Service Order Activity with
status Free will be planned.
Mandatory.
iPerformATPCheck
Indicator whether the ATP check is performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites                              -concept has been implemented).
Mandatory.
iPerformPlannedAvailableCheck
Indicator whether the Planned Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites                              -concept has been implemented).
Mandatory.
iPerformOnHandAvailableCheck
Indicator whether the On Hand Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites                              -concept has been implemented).
Mandatory.
iSkipBlockedInventory
Indicator whether Blocked Inventory has to be considered
during the various material availability checks.
Note: value Yes only allowed if material availability
is present in the Service Order Parameters
(or site specific record, if the Sites                              -concept has
been implemented). Furthermore, at least one of the
input arguments iPerformPlannedAvailableCheck or
iPerformOnHandAvailableCheck should have the value
Yes.
Mandatory.
iBlockPlanningOfOrdersWithShortages
If set to Yes, then the planning of the activity
will not be successful if one of the material
availability checks reports a shortage.
Note: value Yes only allowed if at least one of the
material availability checks is being executed, which
means that either iPerformATPCheck,
iPerformPlannedAvailableCheck or
iPerformOnHandAvailableCheck should have the value Yes.
Mandatory.
iInventoryScope
Indicator if during the various material availability
checks only the current warehouse should be considered
or the whole warehouse cluster.
Possible values:
Current Warehouse Only
Checks if the material is available in the
warehouse defined on the Material Line.
All Warehouses in Planning Cluster
Checks if the material is available in one of
the warehouses in the same cluster as the
warehouse defined on the Material Line.
Mandatory.
iUpdatePlannedDeliveryTimeOfMaterialLines
Indicator whether the material availability checks
should update the planned delivery time of related
material lines.
Note: value Yes only allowed if at least one of the
input arguments iPerformATPCheck or
iPerformPlannedAvailableCheck has the value Yes.
Mandatory.
iUpdateActivitiesAndOrdersWithLatestPlannedMaterialLine
Indicator whether the material availability checks
should update the activity and order with the time of
the latest planned material line.
Note: value Yes only allowed if at least one of the
input arguments iPerformATPCheck or
iPerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
iUpdatePlannedDeliveryTimeOfMaterialLines is Yes.
Mandatory.
iSynchronizeMaterialsWithLatestPlannedMaterialLine
Indicator whether the material availability checks
should synchronize material lines with the latest
planned material line.
Note: value Yes only allowed if at least one of the
input arguments iPerformATPCheck or
iPerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
iUpdatePlannedDeliveryTimeOfMaterialLines is Yes.
Mandatory.
iPurchaseOrderTypeNormalDelivery
If the delivery type of the required material for a
service order activity is By Purchase Order, this
Purchase Order Type is used to create its purchase
order.
Not mandatory.
iPurchaseOrderSeriesNormalDelivery
The number group used to assign series numbers to the
generated purchase orders.
Not mandatory.
iPurchaseOrderTypeDirectDelivery
If the delivery type of the required material for a
service order activity is Supplier Direct Delivery, this
Purchase Order Type is used to create its purchase
order.
Not mandatory.
iPurchaseOrderSeriesDirectDelivery
The number group used to assign series numbers to the
generated purchase orders.
Not mandatory.
iServicesProcurementOrderType
Services Procurement Order Type
Not mandatory.
iServicesProcurementOrderSeries
Services Procurement Order Series
Not mandatory.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then this is an error situation and
the status of the service order activity was not changed
to Planned.
If the return value = 0 (so not an error), the
oExceptionID can still contain information about the
process.
Return: 0                     -       No Error and the status of the given
Service Order Activity changed to Planned.
<> 0                          -       The status of the Service Order Activity could
not be changed to Planned.
```
