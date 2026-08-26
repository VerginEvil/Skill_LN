# PlannedActivity.StartOverview

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for PlannedActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1512-1513

```baan
DLL:   tsextspcapi
This function is available from     2026.06 (KB3669704  ).
Syntax: long PlannedActivity.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iPlannedActivity,
domain  tcpono           iPlannedActivityLine,
long             iViewFieldSet,
ref     domain  tcorno           oPlannedActivity,
ref     domain  tcpono           oPlannedActivityLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Planned Activities
(tsspc2100m000).
Before calling PlannedActivity.StartOverview(), call
ProcessingOptionSet.Create() and assign the value to
iViewFieldSet.
After the call the iViewFieldSet can be deleted by calling
ProcessingOptionSet.Delete().
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the table index that is to be used. (Optional)
Supported values:
1: sort by Planned Activity
2: sort by Serialized Item, Planned Start Time,
Reference Activity
3: sort by Serialized Item, Planned Activity
4: sort by Top Serialized Item, Start Time
5: sort by Installation Group
6: sort by Installation Group, Serialized Item,
Reference Activity
7: sort by Installation Group, Serialized Item,
Start Time
8: sort by Maintenance Scenario, Serialized Item,
Start Time
iQueryExtend
A specific query to be used when zooming to this
session. Note that only extensions on the main
table tsspc200 are supported. (Optional)
iPlannedActivity
The Planned Activity to display at the top of the
grid if present in the chosen view. (Optional)
iPlannedActivityLine
The Planned Activity line to display at the top of the
grid if present in the chosen view. (Optional)
iViewFieldSet
A Set to set the view fields when the index used is not
index 1. (Optional)
INDEX   NAME                    TYPE                    DEFAULT
================================================================
2                      -4,6-8 Item                    domain  tcitem          empty
2                      -4,6-8 SerialNumber            domain  tcibd.sern      empty
2,4,7                      -8 StartTime               domain  tsmdm.pldt      0
2,6     ReferenceActivity       domain  tsacm.cact      empty
5                      -7     InstallationGroup       domain  tsbsc.clst      empty
8       MaintenanceScenario     domain  tcorno          empty
Output:
oPlannedActivity
The selected PlannedActivity if iStartMode is
MODAL and the session is closed with a single selection.
oPlannedActivityLine
The selected PlannedActivityLine if iStartMode is
MODAL and the session is closed with a single selection.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Session started
<> 0    An error occurred
```
