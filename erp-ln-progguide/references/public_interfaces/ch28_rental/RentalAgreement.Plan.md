# RentalAgreement.Plan

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalAgreement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1587-1591

```baan
DLL:   tsextsocapi
This function is available from 2024.11 (KB3532033).
Syntax: long RentalAgreement.Plan(
domain  tcorno           iRentalOrder fixed,
domain  tsmdm.acln       iAgreementLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to plan one specific Rental Agreement
(tssoc210 record).
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
would select one specific Rental Agreement in session
Rental Agreements  (tssoc2110m200, tssoc2610m300) and use the
specific option Plan... , which starts session Rental Order
Resource Planning (tssoc2260m100).
All the options which are available in the planning session
are also available as input arguments for this
interface function. It can be useful to look at the Help for
session tssoc2260m100.
Note that this interface behaves exactly the same as the
planning session, which means that the same checks are executed
for the input process options as is being done in the planning
session. If a certain combination of input arguments is not
allowed, the user will be notified.
Pre:    db.retry.point must have been set.
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Blocking status of the Rental Order could have been changed.
Status of Rental Agreement could have been changed from
Free to Planned.
Commit/abort the transaction.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iRentalOrder
Rental Order
Mandatory.
iAgreementLine
Rental Agreement
Mandatory.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
Replan
domain  tcyesno         tcyesno.no
If Replan is Yes, Rental Agreement with status
Free, or Planned, are planned or replanned.
If Replan is No, only Rental Agreement with
status Free will be planned.
PerformATPCheck
domain  tcyesno         tcyesno.no
Indicator whether the ATP check is performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites-concept has been implemented).
PerformPlannedAvailableCheck
domain  tcyesno         tcyesno.no
Indicator whether the Planned Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites-concept has been implemented).
PerformOnHandAvailableCheck
domain  tcyesno         tcyesno.no
Indicator whether the On Hand Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites-concept has been implemented).
SkipBlockedInventory
domain  tcyesno         tcyesno.no
Indicator whether Blocked Inventory has to be considered
during the various material availability checks.
Note: value Yes only allowed if material availability
is present in the Service Order Parameters
(or site specific record, if the Sites-concept has
been implemented). Furthermore, at least one of the
input arguments PerformPlannedAvailableCheck or
PerformOnHandAvailableCheck should have the value
Yes.
BlockPlanningOfOrdersWithShortages
domain  tcyesno         tcyesno.no
If set to Yes, then the planning of the activity
will not be successful if one of the material
availability checks reports a shortage.
Note: value Yes only allowed if at least one of the
material availability checks is being executed, which
means that either PerformATPCheck,
PerformPlannedAvailableCheck or
PerformOnHandAvailableCheck should have the value Yes.
InventoryScope
domain  tsmdm.scin      tsmdm.scin.curr.warehouse
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
UpdatePlannedDeliveryTimeOfMaterialLines
domain  tcyesno         tcyesno.no
Indicator whether the material availability checks
should update the planned delivery time of related
material lines.
Note: value Yes only allowed if at least one of the
input arguments PerformATPCheck or
PerformPlannedAvailableCheck has the value Yes.
UpdateActivitiesAndOrdersWithLatestPlannedMaterialLine
domain  tcyesno         tcyesno.no
Indicator whether the material availability checks
should update the Agreement and Order with the time of
the latest planned material line.
Note: value Yes only allowed if at least one of the
input arguments PerformATPCheck or
PerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
UpdatePlannedDeliveryTimeOfMaterialLines is Yes.
SynchronizeMaterialsWithLatestPlannedMaterialLine
domain  tcyesno         tcyesno.no
Indicator whether the material availability checks
should synchronize material lines with the latest
planned material line.
Note: value Yes only allowed if at least one of the
input arguments PerformATPCheck or
PerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
UpdatePlannedDeliveryTimeOfMaterialLines is Yes.
PurchaseOrderTypeNormalDelivery
domain  tccotp          empty
If the delivery type of the required material is
By Purchase Order, this Purchase Order Type is used to
create its purchase order.
PurchaseOrderSeriesNormalDelivery
domain  tcseri          empty
The number group used to assign series numbers to the
generated purchase orders.
PurchaseOrderTypeDirectDelivery
domain  tccotp          empty
If the delivery type of the required material is
Supplier Direct Delivery, this Purchase Order Type is
used to create its purchase order.
PurchaseOrderSeriesDirectDelivery
domain  tcseri          empty
The number group used to assign series numbers to the
generated purchase orders.
ServicesProcurementOrderType
domain  tccotp          empty
Services Procurement Order Type
ServicesProcurementOrderSeries
domain  tcseri          empty
Services Procurement Order Series
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
Return: 0       -       No Error and the status of the given
Rental Agreement changed to Planned.
<> 0    -       The status of the Rental Agreement could
not be changed to Planned.
```
