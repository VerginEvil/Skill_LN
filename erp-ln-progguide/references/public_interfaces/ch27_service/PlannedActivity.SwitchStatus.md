# PlannedActivity.SwitchStatus

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PlannedActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1513-1516

```baan
DLL:   tsextspcapi
This function is available from     2022.03 (KB2231979  ).
Syntax: long PlannedActivity.SwitchStatus(
const   domain  tcorno           iPlannedActivity fixed,
const   domain  tcpono           iActivityLine,
const   domain  tsspc.stat       iSwitchStatusTo,
const   domain  tcyesno          iPerformATPCheck,
const   domain  tcyesno          iPerformPlannedAvailableCheck,
const   domain  tcyesno          iPerformOnHandAvailableCheck,
const   domain  tcyesno          iSkipBlockedInventory,
const   domain  tsmdm.scin       iInventoryScope,
const   domain  tcyesno          iBlockRelease,
const   domain  tcyesno          iUpdateTimeWithLatestPlannedMaterialLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : With this function it is possible for one single planned
activity (tsspc200, with key iPlannedActivity and
iActivityLine), to switch its status (tsspc200.stat).
If a status change is not allowed, then a value <> 0 is
returned and the reason why is present in the
oExceptionMessage/oExceptionID.
Note that even if the return value is 0, so no error, and
the status switch is executed, there can still be information
in the oExceptionMessage and oExceptionID. This can happen if
for example the status switch is done to 'Released' and the
material availability checks are executed and there is a
shortage, but the input argument iBlockRelease is not set to
'yes'. In this scenario the status switch is executed, but
a message of type 'Information' is put on the message stack
and is present in the oExceptionMessage and oExceptionID.
Note that the input arguments after the input argument
iSwitchStatusTo (so iPerformATPCheck upto and including
i.UpdateTimeWithLatestPlannedMaterialLine) are only
used if:
1) The switch is done to the status 'Released' (so
i.SwitchStatusTo = tsspc.stat.released).
2) The Material Availability functionality has been switched
on in the SPC planning parameters (or if the concept
'Sites' has been implemented and there is a site specific
record in tsspc003 with the site from the planned activity
(tsspc200.site)).
Pre     : A db.retry.point() must have been specified.
Post    : An abort.transaction() or commit.transaction() must be
executed.
Input   :
iPlannedActivity                                                            -
The planned activity order number.
Mandatory input.
iActivityLine                                                            -
The planned activity line number.
Manatory input.
iSwitchStatusTo                                                            -
The status to which the planned activity has to be
switched.
Mandatory input.
iPerformATPCheck
If the functionality of Material Availability is
switched on in the planning parameters and if the status
is switched to 'Released' and this input argument
is set to 'yes', then the system will perform the ATP
(Available To Promise) check.
Mandatory input.
iPerformPlannedAvailableCheck                                                 -
If the functionality of Material Availability is
switched on in the planning parameters and if the status
is switched to 'Released', then when this input argument
is set to 'yes', the system will perform the Planned
Available check.
Mandatory input.
iPerformOnHandAvailableCheck                                                  -
If the functionality of Material Availability is
switched on in the planning parameters and if the status
is switched to 'Released', then when this input argument
is set to 'yes', the system will perform the On Hand
check.
Mandatory input.
iSkipBlockedInventory                                                         -
If the functionality of Material Availability is
switched on in the planning parameters and if the status
is switched to 'Released', then when this input argument
is set to 'yes', the system will skip blocked inventory
during the different Material Availability checks.
Mandatory input.
iInventoryScope                                                            -
If the functionality of Material Availability is
switched on in the planning parameters and if the status
is switched to 'Released', then with this input argument
it can be controlled whether the Material Availability
checks should be executed for the current Warehouse
only or for the whole warehouse cluster.
Mandatory input.
iBlockRelease                                                            -
If the functionality of Material Availability is
switched on in the planning parameters and if the status
is switched to 'Released', then if the material
availability checks result in a shortage, or if the
supply is too late, a DALHOOKERROR is returned otherwise
only an information message is put on the message stack.
Mandatory input.
iUpdateTimeWithLatestPlannedMaterialLine                                      -
If the functionality of Material Availability is
switched on in the planning parameters and if the status
is switched to 'Released', and this input parameters is
set to 'yes', then the planning times on the planned
activity line (tsspc200) are updated with the times of
the latest material line.
Mandatory input.
Output  :
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
