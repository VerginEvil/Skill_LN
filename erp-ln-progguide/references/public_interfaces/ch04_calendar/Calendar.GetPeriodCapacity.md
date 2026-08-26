# Calendar.GetPeriodCapacity

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for Calendar
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 149-150

```baan
DLL:   tcextccpapi
This function is available from     2021.05 (KB2187487  ).
Syntax: long Calendar.GetPeriodCapacity(
domain  tcncmp           iLogisticCompany,
domain  tcccp.ccal       iCalendarCode,
domain  tcccp.ract       iAvailabilityType,
domain  tczone           iTimeZone,
domain  tcdate           iStartDate,
domain  tcdate           iEndDate,
ref     domain  cpcom.cato       oCapacity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Get the available capacity between the given start and end date,
for the given logistic company and calendar parameters.
In case the optional iTimeZone parameter is not given,
the system timezone is assumed.
Input:
iLogisticCompany
Logistic Company (Mandatory)
iCalendarCode
Calendar (Mandatory)
iAvailabilityType
Availability Type (Mandatory)
iTimeZone
Time zone (Optional)
iStartDate
Start Date (Mandatory)
iEndDate
End Date (Mandatory)
Output:
oCapacity
Capacity (in hours)
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                - Function is executed successfully
<> 0                          - An error occurred
```
