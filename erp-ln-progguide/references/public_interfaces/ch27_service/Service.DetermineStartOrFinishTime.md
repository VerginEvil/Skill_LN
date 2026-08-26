# Service.DetermineStartOrFinishTime

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for Service
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1326-1328

```baan
DLL:   tsextsocapi
This function is available from     2020.04 (KB2117506  ).
Syntax: long Service.DetermineStartOrFinishTime(
domain  tcncmp           iLogisticCompany,
domain  tsbsc.clst       iInstallationGroup,
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tcemno           iAssignedServiceEngineer,
domain  tcemno           iPreferredServiceEngineer,
domain  tccwoc           iServiceDepartment,
domain  tcccp.ccap       iDuration,
domain  tcccp.ract       iAvailabilityType,
domain  tcplcd           iPlanMethod,
domain  tsmdm.pldt       iTime,
ref     domain  tsmdm.pldt       oTime,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function determines a finish time for a given start time
or a start time for a given finish time:
-                         When plan method is Plan Forward the start time must be
given and the finish time is calculated.
-                         When plan method is Plan Backward the finish time must be
given and the start time is calculated.
The calendar code and time zone used for planning are
retrieved in the following way.
When the parameter Use Engineer Calendar for Planning
is No, the calendar/timezone is searched in the following
order:
1. Serialized Item
2. Installation Group
3. Assigned Service Engineer
4. Preferred Service Engineer
5. Service Center
6. Company
This means that the Serialized Item calendar is retrieved
first. When no Serialized Item calendar is available the
calendar of the Installation Group is retrieved. And so on.
When for the first 5 levels no calendar is found, finally
the Company calendar/timezone is retrieved; this
calendar/timezone is mandatory, so is always available.
When the parameter Use Engineer Calendar for Planning
is Yes, the calendar/timezone is searched in the following
order:
1. Assigned Service Engineer
2. Preferred Service Engineer
3. Service Center
4. Serialized item
5. Installation Group
6. Company
Pre     : None
Post    : None
Input   : iLogisticCompany                            - Logistic Company: Mandatory
iInstallationGroup                                    - Installation Group:
Not Mandatory
iItem                                                 - Item: Not Mandatory
iSerialNumber                                         - Serial Number: Not Mandatory
iAssignedServiceEngineer                              - Assigned Service Engineer:
Not Mandatory
iPreferredServiceEngineer                             - Preferred Service Engineer:
Not Mandatory
iServiceDepartment                                    - Service Department:
Not Mandatory
iDuration                                             - Duration of Activity:
Not Mandatory
The Duration is expressed in
the Time Duration Unit from
the General Service Parameters
iAvailabilityType                                     - Availability Type:
Not Mandatory
iPlanMethod                                           - Planning Method (forward/
backward): Mandatory
iTime                                                 - Base Time (planned start/
finish date): Not Mandatory
Output  : oTime                                       - Result Time (planned start/
finish date)
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - Data read
<> 0                                                  - An error occurred
```
