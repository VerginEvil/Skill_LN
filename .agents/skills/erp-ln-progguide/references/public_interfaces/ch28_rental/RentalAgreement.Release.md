# RentalAgreement.Release

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalAgreement
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1591-1596

```baan
DLL:   tsextsocapi
This function is available from 2024.11 (KB3532033).
Syntax: long RentalAgreement.Release(
domain  tcorno           iRentalOrder fixed,
domain  tsmdm.acln       iAgreementLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to release one specific Rental Agreement
(tssoc210 record).
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
would select one specific Rental Agreement in session Rental
Agreements (tssoc2110m200, tssoc2610m300) and would use the
specific option
Release, which starts session tssoc2200m100. All the
options which are available in the release session are also
available as input arguments for this interface function.
It can be useful to look at the help for session tssoc2200m100.
Note that this interface behaves exactly the same as the
release session, which means that the same checks are executed
for the input process options as is being done in the release
session. If a certain combination of input arguments is not
allowed, the user will be notified.
If the option IncludeOrdersWithStatusFree is set to Yes and
the user has selected an order with status Free, then
the system will first try to Plan this order. If that
succeeds the status of the order is changed to Planned and
committed in the database.
If the change to Planned succeeds or the Rental Order
already had the status Planned, the system will try to
release this order.
If that succeeds and warehouse orders have been created, and
some of the warehouse orders activities have been set to
automatic, the system will try to execute those warehouse
activities.
Note that because of the blocking check on the Rental Order and
the automatic processing of warehouse orders, the system
will commit the database transactions in this function.
This means that it is not necessary to set a db.retry.point()
before calling this function and abort/commit after this
function, because that is already handled within this function.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Blocking status of the Rental Order could have been changed.
Status of Rental Order could have been changed from Free to
Planned, if releasing itself did not succeed, but
the order had initial status Free and planning did
succeed (this can only happen if also the input argument
IncludeOrdersWithStatusFree has been set to Yes).
The status of the Rental Order could have been changed from
Free or Planned to Released. If warehouse procedures
have been set to automatic, then these are also executed.
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
CheckSkills
domain  tcyesno         tcyesno.yes
Indicator whether the system should check during
releasing whether the correct skills are available to
execute each related Agreement. If set to
Yes and not the correct skills are available, the
release of the order will not be executed.
CheckProjectStatus
domain  tcyesno         tcyesno.yes
Indicator whether the system should check during
releasing whether the status of a related project
allows releasing the order. If set to Yes and
the status of the project is not ok, the release of the
order will not be executed.
IncludeOrdersWithStatusFree
domain  tcyesno         tcyesno.yes
Indicator whether also a Rental Order with status Free
is allowed to be released.
UpdateActualRentalLocationAddresses
domain  tcyesno         tcyesno.no
Indicator whether the addresses of rental equipment
have to be updated.
UseActivityLocationAddressForRentalAddress
domain  tcyesno         tcyesno.yes
Indicator whether the Location Address of the Agreement
must be used, or another address to be specified in
ActualRentalLocationAddress.
ActualRentalLocationAddress
domain  tccom.cadr      empty
On releasing a Rental Agreement, another Address
for the rental equipment than specified on
the Agreement can be used.
CheckOperators
domain  tcyesno         tcyesno.yes
Indicator whether the system should check during
releasing that each Agreement has at least one
Operator. If set to Yes and no operator is
assigned to an Agreement, the release of the
Agreement will not be executed.
Note: the value No will be converted to Yes if
Assignments are mandatory for Rental in the Service
Order Parameters.
CalculateRentalUsage
domain  tcyesno         tcyesno.no
When this indicator is set to Yes, the actual quantity
is determined and set on the new actual resource rental
usage line.
SetActualOnHireDate
domain  tcyesno         tcyesno.no
When this indicator is set to Yes, the current system
date and time is used as the On Hire date for the
released Rental Order.
CopyEstimatesToActualsForOtherCosts
domain  tcyesno         tcyesno.no
Indicator whether the system should take over the
estimates to the actual values for Other Costs
(tssoc240) during the release process.
CheckServiceKitAllocation
domain  tcyesno         tcyesno.yes
Indicator whether the system should check during
releasing whether the service kit (if present) can be
allocated. If set to Yes and the allocation for the
service kit cannot be done, the release of the
order will not be executed.
PerformATPCheck
domain  tcyesno         tcyesno.no
Indicator whether the ATP check is performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Service Order Parameters (or site specific record, if
the Sites-concept has been implemented).
Furthermore the IncludeOrdersWithStatus
Free should also have the value Yes.
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
BlockRelease
domain  tcyesno         tcyesno.no
If set to Yes, then the releasing of the Agreement
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
checks only the current warehouse should be considered,
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
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Note that if the return value of this function is
unequal zero, then we are dealing with an error
situation and the status of the Rental Order was not
changed to Released.
If the return value = 0 (so not an error), the
oExceptionID can still contain information about the
process.
Return: 0       -       No Error and the status of the given
Rental Agreement changed to Released.
<> 0    -       The status of the Rental Agreement could not be
changed to Released.
```
