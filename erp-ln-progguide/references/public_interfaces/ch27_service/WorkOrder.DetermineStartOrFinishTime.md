# WorkOrder.DetermineStartOrFinishTime

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for WorkOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1489-1491

```baan
DLL:   tsextwcsapi
This function is available from     2022.10 (KB2262990  ).
Syntax: long WorkOrder.DetermineStartOrFinishTime(
domain  tsmdm.cstp       iServiceType,
domain  tcemno           iAssignedEngineer,
domain  tcemno           iPreferredEngineer,
domain  tccwoc           iOperationsDepartment,
domain  tccwoc           iWorkCenter,
domain  tsmdm.pldt       iBaseTime,
domain  tcplcd           iPlanningMethod,
domain  tcccp.ccal       iCalendarCode,
domain  tcccp.ract       iAvailabilityType,
domain  tsmdm.tmdu       iDuration,
ref     domain  tsmdm.pldt       oTime,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines a finish time for a given start time
or a start time for a given finish time:
-                         When plan method is 'plan forward' the start time must be
given and the finish time is calculated.
-                         When plan method is 'plan backward' the finish time must be
given and the start time is calculated.
If passed empty, the calendar code used for planning is
retrieved in the following way.
When the parameter 'Use Engineer Calendar for Planning'
is No, the calendar is searched in the following
order:
1. Assigned Service Engineer
2. Preferred Service Engineer
3. Work Center
4. Operations Department
5. Enterprise Unit
6. Company
This means that the assigned engineer calendar is retrieved
first. When no assigned engineer calendar is available the
calendar of the preferred engineer is retrieved. And so on.
Finally the company calendar is retrieved, this calendar
should always be available.
When this parameter is no, the calendar hierarchy is:
1. Work Center
2. Service Department
3. Enterprise Unit
4. Company
The Time Zone is searched in the same order as done for
the Calendar. With the exception that no Time Zone is present
on Enterprise Unit or Company level.
If passed empty, the Availability Type is retrieved from
the Service Type.
Input:  iServiceType            Service Type
Not Mandatory
iAssignedEngineer       Assigned Service Engineer
Not Mandatory
iPreferredEngineer      Preferred Service Engineer
Not Mandatory
iOperationsDepartment   Operations Department
iWorkCenter             Work Center
Either Operation Department or
Work Center must be filled.
iBaseTime               Base Time, , dependent on the Planning
Method this is the start or finish time.
Mandatory
iDuration               Duration, expressed in general service
parameter 'Time Duration Unit'
(tsmdm000.untd)
Not Mandatory
iCalendarCode           Calendar
Not Mandatory
iAvailabilityType       Availability Type
Not Mandatory
iPlanMethod             Planning Method (forward/ backward)
Mandatory
Output:
oTime                   Result Time (planned start/ finish date)
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     -               No Error.
<> 0                          -               Error.
```
