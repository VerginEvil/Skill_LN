# PlannedActivity.CreateMaintenancePlan

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PlannedActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1522-1526

```baan
DLL:   tsextspcapi
This function is available from 2025.06 (KB3569155).
Syntax: long PlannedActivity.CreateMaintenancePlan(
long             iProcessingOptionSet,
ref             boolean          oPlannedActivityCreated,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to generate the maintenance plan.
(almost) All selection ranges and options which are available in
session tsspc2200m000 (Generate Maintenance Plan) and which
are not report specific are available as input arguments.
Also see the help for session Generate Maintenance Plan (
tsspc2200m000).
Depending on the selection ranges, the system will determine
the set of serialized items for which planned activities can
be deleted/created. The system will commit the database
changes per serialized item. If for whatever reason, the system
encounters an error, this function will return a value unequal
zero and the reason why the generation of the maintenance
plan was not successful is present in the oExceptionMessage and
oExceptionID.
Note that this means that even though a value <> 0 is returned,
still the oPlannedActivityCreated can be true!
This function does its own database handling, so there is no
need to specify a db.retry.point() before calling this function
and to abort/commit the transactions afterwards.
Pre:    No open database transaction should be present (so before
calling this function the existing database transactions should
either have been aborted or committed).
Call ProcessingOptionSet.Create() to obtain the
iProcessingOptionSet (XML node).
Post:   Delete the option set by calling ProcessingOptionSet.Delete().
Input:
iProcessingOptionSet: a processing option set number
referring to a processing option set containing at
least one valid option. If a certain processing option
is not provided in the option set, then the default
value will be used!
Mandatory.
NAME            TYPE                    DEFAULT
================================================================
SelectionMaintenanceScenarios
domain  tsspc.sel.pmsc
tsspc.sel.pmsc.all
With this option the user can indicate whether a filter
on maintenance scenario level is applicable.
If set to tsspc.sel.pmsc.all (or not set as that is the
default), then no filtering will be done on scenario
level.
TypeOfScenarioSelection
domain  tsspc.sel.type
tsspc.sel.type.both
Only if the SelectionMaintenanceScenarios is set to
tsspc.sel.pmsc.specific, this option is considered.
There are two categories of scenario lines (Time Based
and Usage Based). If the category Time Based is
selected, then only time based and pattern based
scenario lines are processed. If the category Usage
Based is selected, then only usage based scenario lines
are processed.
MaintenanceScenarioFrom
domain  tcorno
empty
If the SelectionMaintenanceScenarios is set to
tsspc.sel.pmsc.all, this option is ignored.
MaintenanceScenarioTo
domain  tcorno
Maximum of the domain.
If the SelectionMaintenanceScenarios is set to
tsspc.sel.pmsc.all, this option is ignored.
ScenarioLineFrom
domain  tcpono
0
If the SelectionMaintenanceScenarios is set to
tsspc.sel.pmsc.all, this option is ignored.
ScnearioLineTo
domain  tcpono
Maximum of the domain.
If the SelectionMaintenanceScenarios is set to
tsspc.sel.pmsc.all, this option is ignored.
SelectionSerializedItems
domain  tsspc.sel.item
tsspc.sel.item.all
With this option the user can indicate whether a filter
on serialized item level is applicable. If set to
tsspc.sel.item.all (or not set, because this is the
default) then no filtering will be done on serialized
item level.
OwnerFrom
domain  tccom.bpid
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
OwnerTo
domain  tccom.bpid
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
InUseByBPFrom
domain  tccom.bpid
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
InUseByBPTo
domain  tccom.bpid
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
DepartmentFrom
domain  tccwoc
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
DepartmentTo
domain  tccwoc
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
ServiceItemGroupFrom
domain  tsmdm.csgr
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
ServiceItemGroupTo
domain  tsmdm.csgr
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
SerializedItemGroupFrom
domain  tscfg.sigr
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
If in the Configuration Management Parameters
(tscfg0100m000) the option 'Serialized Item Group Usage'
is not switched on, then this option is also ignored.
SerializedItemGroupTo
domain  tscfg.sigr
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
If in the Configuration Management Parameters
(tscfg0100m000) the option 'Serialized Item Group Usage'
is not switched on, then this option is also ignored.
UsageClassFrom
domain  tsspc.cusc
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
UsageClassTo
domain  tsspc.cusc
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
InstallationGroupFrom
domain  tsbsc.clst
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
If in the General Service Parameters (tsmdm0100m000),
the implemented parameter 'Installation Groups' is not
switched on, then this option is also ignored.
InstallationGroupTo
domain  tsbsc.clst
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
If in the General Service Parameters (tsmdm0100m000),
the implemented parameter 'Installation Groups' is not
switched on, then this option is also ignored.
ItemFrom
domain  tcitem
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
ItemTo
domain  tcitem
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
SerialNumberFrom
domain  tcibd.sern
empty
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
SerialNumberTo
domain  tcbid.sern
Maximum of the domain.
If the SelectionSerializedItems is set to
tsspc.sel.item.all, this option is ignored.
UseHorizon
domain  tcyesno
tcyesno.yes
If set to tcyesno.yes, the system will use the
FromDateUTC together with the Horizon to calculate a
ToDateUTC
domain  tsmdm.numb
1
If the UseHorizon is set to tcyesno.no, this option is
ignored.
HorizonUnit
domain  tsmdm.pern
tsmdm.pern.year
If the UseHorizon is set to tcyesno.no, this option is
ignored.
FromDateUTC
domain  tcdate
utc.num()
ToDateUTC
domain tcdate
FromDateUTC + 1 year.
If the UseHorizon is set to tcyesno.yes, this option is
ignored. The FromDateUTC together with the Horizon
and HorizonUnit will determine then the ToDateUTC.
If the UseHorizon is set to tcyesno.no and the ToDateUTC
is not provided, then the default will be the
FromDateUTC + 1 year.
GenerateOnlyInActiveContract
domain  tcyesno
tcyesno.no
If set to tcyesno.yes, then only serialized items are
considered with an active service contract and planned
activities will only be created within the contract
period.
IgnorePlannedUntilTime
domain  tcyesno
tcyesno.no
If set to tcyesno.yes, the system will not check whether
a planned activity which is going to be created has
a planned finish time before the Planned Until Time
(attribute on serialized item level, i.e. tscfg200.pltm).
Note that it is dangerous to deviate from the default
value (tcyesno.no), because then it is possible that
the system will generate duplicate planned activities.
TimeBasedMethod
domain  tsspc.2200.mth
tsspc.2200.mth.start.date
If a time based scenario line is handled for a
serialized item, then this determines the start date
from which the planning for that specific serialized
item will start. By default (tsspc.2200.mth.start.date)
it will start using the serialized item planning start
date which is specified in the service planning
parameters (tsspc0100m000).
See the priorities in the parameters (Generate Planned
Activities - Serialized Item Start Date).
GenerationTypeTimeBased
domain  tsspc.gen.type
tsspc.gen.type.keep
This option controls the fact whether first the existing
planned activities will be deleted in the specified
planning horizon. For time based the default will be
that existing planned activities remain and are not
deleted.
GenerationTypeUsageBased
domain  tsspc.gen.type
tsspc.gen.type.regenerate
This option controls the fact whether first the existing
planned activities will be deleted in the specified
planning horizon. For usage based the default will be
that existing planned activities are first deleted,
before any new ones are generated.
Output:
oPlannedActivityCreated
If at least one planned activity was generated, then
this output variable is set to 'True'.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       -       No Error
<> 0    -       Error present. Note that this function is
going to create the maintenance plan
(planned activities) for a set of serialized items.
If an error occurs while generating the planned
activities for a specific serialized item, then the
transaction is aborted and the errors are stored in
the oExceptionID. The process however continues with the
next serialized item. So in the end it could be that
the return value is <> 0 (so error occurred), but there
are also planned activities created. The latter can
be checked with the output argument
oPlannedActivityCreated.
```
