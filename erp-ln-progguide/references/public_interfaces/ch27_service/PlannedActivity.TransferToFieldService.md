# PlannedActivity.TransferToFieldService

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PlannedActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1516-1521

```baan
DLL:   tsextspcapi
This function is available from     2023.08 (KB2290765  ).
Syntax: long PlannedActivity.TransferToFieldService(
domain  tcorno           iPlannedActivity fixed,
domain  tcpono           iActivityLine,
domain  tcyesno          iUseCallData,
domain  tsmdm.pldt       iEarliestStartTime,
domain  tsmdm.pldt       iLatestFinishTime,
domain  tsmdm.pldt       iPlannedStartTime,
domain  tsmdm.pldt       iPlannedFinishTime,
domain  tcyesno          iAppointment,
domain  tcyesno          iGroupActivities,
domain  tcyesno          iGroupWithExistingServiceOrders,
domain  tcyesno          iExcludeEmergencyOrders,
domain  tcyesno          iGroupByInstallationGroup,
domain  tcyesno          iGroupByItem,
domain  tcyesno          iGroupBySerialNumber,
domain  tcyesno          iGroupByActivityGroup,
domain  tcyesno          iGroupByLocationAddress,
domain  tcyesno          iGroupByPlannedStartTimesWithinSpanOf,
domain  tsmdm.tmdu       iDifferenceInStartTime,
domain  tcyesno          iPlanActivitiesInSequence,
domain  tsspc.2220.tra   iTravelTime,
domain  tcyesno          iPerformATPCheck,
domain  tcyesno          iPerformPlannedAvailableCheck,
domain  tcyesno          iPerformOnHandAvailableCheck,
domain  tcyesno          iSkipBlockedInventory,
domain  tsmdm.scin       iInventoryScope,
domain  tcyesno          iBlockRelease,
domain  tcyesno          iUpdateActivitiesWithLatestPlannedMaterialLine,
domain  tcyesno          iRecalculatePlannedTimes,
domain  tcseri           iServiceOrderSeries,
ref     domain  tcorno           oServiceOrder,
ref     domain  tsmdm.acln       oServiceOrderActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  With this function it is possible to transfer a Planned
Activity (tsspc200, with key iPlannedActivity and
iActivityLine) to a Service Order.
If a transfer is not allowed, then a value <> 0 is
returned and the reason why is present in the
oExceptionMessage/oExceptionID.
Note that even if the return value is 0, so no error, and
the transfer is executed, there can still be information
in the oExceptionMessage and oExceptionID. This can happen
when the material availability checks are executed and
there is a shortage, but the input argument iBlockRelease
is not set to Yes. In this scenario the transfer is executed,
but a message of type 'Information' is put on the message
stack and is present in the oExceptionMessage and
oExceptionID.
Note that the input arguments after the input argument
iTravelTime (so iPerformATPCheck upto and including
iUpdateActivitiesWithLatestPlannedMaterialLine,) are only
used when the Material Availability functionality has been
switched on in the SPC Planning Parameters.
All the options which are available in the Transfer                      -session
are also available as input arguments for this
interface function. It can be useful to look at the Help for
session tsspc2220m000.
Pre:    A db.retry.point() must have been set.
Post:   An abort.transaction() or commit.transaction() must be
executed.
Input:
iPlannedActivity
The Planned Activity number.
Mandatory input.
iActivityLine
The Planned Activity line number.
Mandatory input.
iUseCallData
Indicator whether the Call or the Planned Activity
is used in case the Planned Activity originates
from a Call.
Mandatory input.
iEarliestStartTime
Earliest Start Time.
Not mandatory.
iLatestFinishTime
Latest Finish Time.
Not mandatory.
iPlannedStartTime
Planned Start Time.
Not mandatory.
iPlannedFinishTime
Planned Finish Time.
Not mandatory.
iAppointment
Appointment. Only used when iUseCallData is Yes and
the Planned Activity originates from a Call.
Mandatory input.
iGroupActivities
Group activities.
Mandatory input.
iGroupWithExistingServiceOrders
If possible the transferred Planned Activity is added
to an existing service order.
Mandatory input.
iExcludeEmergencyOrders
Emergency Orders are excluded when the transferred
Planned Activity is added to an existing service order.
Mandatory input.
iGroupByInstallationGroup
Group by Installation Group
Mandatory input.
iGroupByItem
Group by Item
Mandatory input.
iGroupBySerialNumber
Group by Serial Number
Mandatory input.
iGroupByActivityGroup
Group by Activity Group
Mandatory input.
iGroupByLocationAddress
Group by Location Address
Mandatory input.
iGroupByPlannedStartTimesWithinSpanOf
Group by Planned Start Times within span of...
Mandatory input.
iDifferenceInStartTime
Difference in Start Time, expressed in Time Duration
Unit as defined in the General Service Parameters.
Not mandatory.
iPlanActivitiesInSequence
Use parallel planning Yes/No.
Mandatory input.
iTravelTime
When Planned Activity is added to a Service Order,
it must be ensured that the Planned Activity's Travel
Time is used effectively.
This argument can have the following values:
Minimum
The travel time is the minimum of the planned
activity and that of the service order.
Maximum
The travel time is the maximum of the planned
activity and that of the service order.
Cumulative
The travel time is the cumulative of the
planned activity and that of the service order.
Mandatory input.
iPerformATPCheck
Indicator whether the ATP check is performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Planning Parameters (or site specific record, if
the concept of Sites has been implemented).
Mandatory input.
iPerformPlannedAvailableCheck
Indicator whether the Planned Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Planning Parameters (or site specific record, if
the concept of Sites has been implemented).
Mandatory input.
iPerformOnHandAvailableCheck
Indicator whether the On Hand Inventory check is
performed.
Note: value Yes will be ignored and converted to
No if material availability is not present in the
Planning Parameters (or site specific record, if
the concept of Sites has been implemented).
Mandatory input.
iSkipBlockedInventory
Indicator whether Blocked Inventory has to be considered
during the various material availability checks.
Note: value Yes only allowed if material availability
is present in the Planning Parameters
(or site specific record, if the concept of Sites has
been implemented). Furthermore, at least one of the
input arguments iPerformPlannedAvailableCheck or
iPerformOnHandAvailableCheck should have the value
Yes.
Mandatory input.
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
Mandatory input.
iBlockRelease
If the functionality of Material Availability is
switched on in the Planning Parameters and the
Service Order is released, then if the material
availability checks result in a shortage, or if the
supply is too late, a DALHOOKERROR is returned otherwise
only an information message is put on the message stack.
Mandatory input.
iUpdateActivitiesWithLatestPlannedMaterialLine
Indicator whether the material availability checks
should update the activity and order with the time of
the latest planned material line.
Note: value Yes only allowed if at least one of the
input arguments iPerformATPCheck or
iPerformPlannedAvailableCheck has the value Yes.
Mandatory input.
iRecalculatePlannedTimes
Recalculate the planned time for the Planned Activity.
Mandatory input.
iServiceOrderSeries
The series of the Service Orders to which the
Planned Activity is transferred.
Not mandatory.
Output  :
oServiceOrder
Service Order
oServiceOrderActivity
Service Order Activity
oExceptionMessage
The last message if if any message is found.
Note that if the return value equals 0, so
no error, and the status switch to 'Released' was
executed successfully, then it can contain information
that there is a material shortage, but that that is not
blocking because of the input argument iBlockRelease.
If more than one message is given, these are present in
the oExceptionID
oExceptionID
An ID that refers to all error information if the
return value of the function is <> 0. Use the
functions in Exception to get all relevant information.
Note that if the return value equals 0, so
no error, and the status switch to 'Released' was
executed successfully, then it can contain information
that there is a material shortage, but that that is not
blocking because of the setting of the input argument
iBlockRelease.
Return  : 0                           - No error
<> 0                                  - An error occurred
```

## Public Interfaces for CustomerClaim

The following functions are available: CustomerClaim.Close CustomerClaim.GenerateLinesFromDocument CustomerClaim.GenerateSerializedItem CustomerClaim.StartMultiMain CustomerClaim.StartOverview CustomerClaim.Submit
