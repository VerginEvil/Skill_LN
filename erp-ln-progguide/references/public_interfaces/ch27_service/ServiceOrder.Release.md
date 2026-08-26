# ServiceOrder.Release

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1427-1432

```baan
DLL:   tsextsocapi
This function is available from     2022.04 (KB2235599  ).
Syntax: long ServiceOrder.Release(
const   domain  tcorno           iServiceOrder fixed,
const   domain  tcyesno          iPerformATPCheck,
const   domain  tcyesno          iPerformPlannedAvailableCheck,
const   domain  tcyesno          iPerformOnHandAvailableCheck,
const   domain  tcyesno          iSkipBlockedInventory,
const   domain  tsmdm.scin       iInventoryScope,
const   domain  tcyesno          iBlockRelease,
const   domain  tcyesno          iUpdatePlannedDeliveryTimeOfMaterialLines,
const   domain  tcyesno
iUpdateActivitiesAndOrdersWithLatestPlannedMaterialLine,
const   domain  tcyesno
iSynchronizeMaterialsWithLatestPlannedMaterialLine,
const   domain  tcyesno          iUpdateAllActualRentalLocationAddresses,
const   domain  tcyesno          iIncludeOrdersWithStatusFree,
const   domain  tcyesno          iCheckCapacityAvailability,
const   domain  tcyesno          iCheckProjectStatus,
const   domain  tcyesno          iCheckServiceKitAllocation,
const   domain  tcyesno          iCheckSkills,
const   domain  tcyesno          iCheckAssignments,
const   domain  tcyesno          iCopyEstimatesToActualsForOtherCosts,
const   domain  tcyesno          iOverWriteManualPrice,
const   domain  tcyesno          iOverWriteManualDiscount,
const   domain  tcyesno          iRecalculatePrice,
const   domain  tcyesno          iApplyCumulativePrice,
const   domain  tcyesno          iRecalculateDiscount,
const   domain  tcyesno          iApplyTotalDiscount,
const   domain  tcyesno          iApplyCumulativeDiscounts,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to release one specific service order
(tssoc200 record).
If releasing does not succeed for whatever reason, this function
will return a value unequal zero and the reason why the
release action was not successful is present in the
oExceptionMessage and oExceptionID. If releasing succeeds then
the value zero is returned. Even if a value zero is returned,
which means that the given order changed its status to
Released, the oExceptionMessage can be filled (and
even more information can be present in the oExceptionID),
because the system generates information messages about the
flow of the process (if the activity is first planned, this
is logged as an information message etc.).
This interface has exactly the same options as when the user
would select one specific service order in session Service
Orders (tssoc2100m000) and would use the specific option
Release, which starts the session tssoc2200m000. All the
options which are available in the release session are also
available as input arguments for this interface function.
It can be useful to look at the help for session tssoc2200m000.
Note that this interface behaves exactly the same as the
release session, which means that the same checks are executed
for the input process options as is being done in the release
session. If a certain combination of input arguments is not
allowed, the user will be notified.
If the option iIncludeOrdersWithStatusFree is set to Yes and
the user has selected an order with status Free, then
the system will first try to Plan this order. If that
succeeds the status of the order is changed to Planned and
committed in the database.
If the change to Planned succeeds or the service order
already had the status Planned, the system will try to
release this order.
If that succeeds and warehouse orders have been created, and
some of the warehouse orders activities have been set to
automatic, the system will try to execute those warehouse
activities.
Note that because of the blocking check on the service order and
the automatic processing of warehouse orders, the system
will commit the database transactions in this function.
This means that it is not necessary to set a db.retry.point()
before calling this function and abort/commit after this
function, because that is already handled within this function.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Post:   Blocking status of the service order could have been changed.
Status of service order could have been changed from Free to
Planned, if releasing itself did not succeed, but
the order had initial status Free and planning did
succeed (this can only happen if also the input argument
iIncludeOrdersWithStatusFree has been set to Yes).
The status of the service order could have been changed from
Free or Planned to Released. If warehouse procedures
have been set to automatic, then these are also executed.
Input:  iServiceOrder                                                         -
The service order.
Mandatory input.
iPerformATPCheck                                                            -
Indicator whether the ATP check has to be executed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
service order parameters (or site specific record, if
the Sites                              -concept is implemented).
Furthermore the iIncludeOrdersWithStatus
Free should also have the value Yes.
Mandatory input.
iPerformPlannedAvailableCheck                                                 -
Indicator whether the Planned Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
service order parameters (or site specific record, if
the Sites                              -concept is implemented).
Mandatory input.
iPerformOnHandAvailableCheck                                                  -
Indicator whether the On Hand Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
service order parameters (or site specific record, if
the Sites                              -concept is implemented).
Mandatory input.
iSkipBlockedInventory                                                         -
Indicator whether Blocked Inventory has to be considered
during the various material availability checks.
Note: value Yes only allowed if material availability
is present in the service order parameters
(or site specific record, if the Sites                              -concept is
implemented). Furthermore at least one of the input
arguments iPerformPlannedAvailableCheck or
iPerformOnHandAvailableCheck should have the value
Yes.
Mandatory input.
iInventoryScope                                                            -
Indicator if during the various material availability
checks only the current warehouse should be considered
or the whole warehouse cluster.
Mandatory input.
iBlockRelease                                                            -
If set to Yes, then the releasing of the order
will not be successful if one of the material
availability checks reports a shortage.
Note: value Yes only allowed if at least one of the
material availability checks is being executed, which
means that either iPerformATPCheck,
iPerformPlannedAvailableCheck or
iPerformOnHandAvailableCheck should have the value Yes.
Mandatory input.
iUpdatePlannedDeliveryTimeOfMaterialLines                                     -
Indicator whether the material availability checks
should update the planned delivery time of related
material lines.
Note: value Yes only allowed if at least one of the
input arguments iPerformATPCheck or
iPerformPlannedAvailableCheck has the value Yes.
Mandatory input.
iUpdateActivitiesAndOrdersWithLatestPlannedMaterialLine                       -
Indicator whether the material availability checks
should update the activities and order with the time of
the latest planned material line.
Note: value Yes only allowed if at least one of the
input arguments iPerformATPCheck or
iPerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
iUpdatePlannedDeliveryTimeOfMaterialLines is Yes.
Mandatory input.
iSynchronizeMaterialsWithLatestPlannedMaterialLine                            -
Indicator whether the material availability checks
should synchronize material lines with the latest
planned material line.
Note: value Yes only allowed if at least one of the
input arguments iPerformATPCheck or
iPerformPlannedAvailableCheck has the value Yes.
Value Yes only allowed if the input argument
iUpdatePlannedDeliveryTimeOfMaterialLines is Yes.
Mandatory input.
iUpdateAllActualRentalLocationAddresses                                       -
Indicator whether the addresses of rental equipment
has to be updated. If a related activity is rentable and
this indicator is set to Yes, then the rental location
of the rental equipment is updated with the location
address of the activity.
Mandatory input.
iIncludeOrdersWithStatusFree                                                  -
Indicator whether also an order with status Free
is allowed to be released.
Mandatory input.
iCheckCapacityAvailability                                                    -
Indicator whether the system should check during
releasing whether there is enough capacity on the
specified service order. If set to Yes and
there is not enough capacity, the release of the
order will not be executed.
Mandatory input.
iCheckProjectStatus                                                           -
Indicator whether the system should check during
releasing whether the status of a related project
allows releasing the order. If set to Yes and
the status of the project is not ok, the release of the
order will not be executed.
Mandatory input.
iCheckServiceKitAllocation                                                    -
Indicator whether the system should check during
releasing whether the service kit (if present) can be
allocated. If set to Yes and the allocation for the
service kit cannot be done, the release of the
order will not be executed.
Mandatory input.
iCheckSkills                                                            -
Indicator whether the system should check during
releasing whether the correct skills are available to
execute each related service order activity. If set to
Yes and not the correct skills are available, the
release of the order will not be executed.
Mandatory input.
iCheckAssignments                                                            -
Indicator whether the system should check during
releasing that each activity has at least one
assignment. If set to Yes and no assignment is
related to a related activity, the release of the
order will not be executed.
Note: the value No will be converted to Yes if
assignments are mandatory in the service order
parameters.
Mandatory input.
iCopyEstimatesToActualsForOtherCosts.yn                                       -
Indicator whether the system should take over the
estimates to the actual values for Other Costs (
tssoc240) during the release process.
Mandatory input.
iOverWriteManualPrice                                                         -
If in the pricing module, the parameter has been set in
such a way that the repricing should be automatic or
interactive, then this input parameter is considered.
This means that if Yes is given but for this order the
automatic repricing is not applicable, it will be
ignored and handled as if it is set to No.
If repricing is applicable for this order, this means
that it is allowed by the pricing process to overwrite
manually changed prices.
Mandatory input.
iOverWriteManualDiscount
Mandatory Input.                                                            -
If in the pricing module, the parameter has been set in
such a way that the repricing should be automatic or
interactive, then this input parameter is considered.
This means that if Yes is given but for this order the
automatic repricing is not applicable, it will be
ignored and handled as if it is set to No.
If repricing is applicable for this order, this means
that it is allowed by the pricing process to overwrite
manually changed discounts.
iRecalculatePrice                                                            -
If in the pricing module, the parameter has been set in
such a way that the repricing should be automatic or
interactive, then this input parameter is considered.
This means that if Yes is given but for this order the
automatic repricing is not applicable, it will be
ignored and handled as if it is set to No.
If repricing is applicable and this input parameter is
set to Yes, the system will reprice the order.
Mandatory Input.
iApplyCumulativePrice                                                         -
If in the pricing module, the parameter has been set in
such a way that the repricing should be automatic or
interactive, then this input parameter is considered.
This means that if Yes is given but for this order the
automatic repricing is not applicable, it will be
ignored and handled as if it is set to No.
If repricing is applicable and this input parameter is
set to Yes, the system will apply the concept of
cumulative prices.
Mandatory Input.
iRecalculateDiscount                                                          -
If in the pricing module, the parameter has been set in
such a way that the repricing should be automatic or
interactive, then this input parameter is considered.
This means that if Yes is given but for this order the
automatic repricing is not applicable, it will be
ignored and handled as if it is set to No.
If repricing is applicable and this input parameter is
set to Yes, the system will recalculate the discounts.
Mandatory Input.
iApplyTotalDiscount                                                           -
If in the pricing module, the parameter has been set in
such a way that the repricing should be automatic or
interactive, then this input parameter is considered.
This means that if Yes is given but for this order the
automatic repricing is not applicable, it will be
ignored and handled as if it is set to No.
If repricing is applicable and this input parameter is
set to Yes, the system will apply the concept of
total discounts.
Mandatory Input.
iApplyCumulativeDiscounts                                                     -
If in the pricing module, the parameter has been set in
such a way that the repricing should be automatic or
interactive, then this input parameter is considered.
This means that if Yes is given but for this order the
automatic repricing is not applicable, it will be
ignored and handled as if it is set to No.
If repricing is applicable and this input parameter is
set to Yes, the system will apply the concept of
cumulative discounts.
Mandatory Input.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation and the status of the service order was not
changed to Released.
If the return value = 0 (so not an error), the
oExceptionID can still contain information about the
process.
Return: 0                     -       No Error and the status of the given
service order changed to Released.
<> 0                          -       The status of the service order could not be
changed to Released.
```
