# Calendar.PlanLeadTimeBackward

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for Calendar
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 151-152

```baan
DLL:   tcextccpapi
This function is available from     2020.06 (KB2100763  ).
Syntax: long Calendar.PlanLeadTimeBackward(
domain  tcccp.ccal       iCalendarCode,
domain  tcccp.ract       iAvailabilityType,
domain  tcdate           iFinishDate,
domain  tcccp.ccap       iLeadTime,
domain  tcccp.ptmu       iTimeUnit,
domain  tczone           iTimeZone,
ref     domain  tcdate           oFinishDate,
ref     domain  tcdate           oStartDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function plans lead time backward.
For the given finish date and leadtime, the start date
is calculated for the in the given calendar (= calendar code /
availability type combination).
Depending on the Time Unit (iTimeUnit) the planning
will be done in seconds, hours or days (not capacity).
The constraint here is that the given lead time also must be
in seconds, hours or days.
Use the following table for finding the unit of the lead time:
+                      -------------------------------+-----------------+
| Time Unit                     | Lead Time
+                      -------------------------------+-----------------+
| Seconds (tcccp.pltmu.seconds) | Seconds
| Hours (tcccp.pltmu.hours)     | Hours
| Days (tcccp.pltmu.days)       | Days
+                      -------------------------------+-----------------+
So if the plan time unit is seconds than also the lead time
must be expressed in seconds, the same goes for hours and days.
Time Unit Hours can have fractions (e.g. 1.5),
The Time Units Seconds and Days must be passed into this
functions without fractions (e.g. 5400 when seconds or
1 if days).
Input:  iCalendarCode                 -       Calendar Code, Mandatory
iAvailabilityType                       -     Availability Type, Mandatory
iFinishDate                           -       Requested Finish date (utc), Mandatory
iLeadTime                             -       Lead Time
iTimeUnit                             -       Time Unit, Mandatory
iTimeZone                             -       Time Zone, Optional
When not specified, the time
zone of the company is used
Output:
oFinishDate                           -       Actual finish date (= iFinishDate or
if iFinishDate is between availability
periods: iStartDate moved backward
to the end of the previous
availability period)
oStartDate                            -       Calculated Start Date
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                             -       Start Date is succesfully calculated
<> 0                                  -       Start Date could not be calculated
```
