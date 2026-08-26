# Calendar.PlanLeadTimeForward

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for Calendar
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 152-153

```baan
DLL:   tcextccpapi
This function is available from     2020.06 (KB2100763  ).
Syntax: long Calendar.PlanLeadTimeForward(
domain  tcccp.ccal       iCalendarCode,
domain  tcccp.ract       iAvailabilityType,
domain  tcdate           iStartDate,
domain  tcccp.ccap       iLeadTime,
domain  tcccp.ptmu       iTimeUnit,
domain  tczone           iTimeZone,
ref     domain  tcdate           oStartDate,
ref     domain  tcdate           oFinishDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function plans lead time forward.
For the given start date and leadtime, the end date
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
iStartDate                            -       Start date (utc), Mandatory
iLeadTime                             -       Lead Time
iTimeUnit                             -       Time Unit, Mandatory
iTimeZone                             -       Time Zone, Optional
When not specified, the time
zone of the company is used
Output:
oStartDate                            -       Actual start date (= iStartDate or
if iStartDate is between availability
periods: iStartDate moved forward
to the start of the next
availability period)
oFinishDate                           -       Calculated Finish Date
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                             -       Finish Date is succesfully calculated
<> 0                                  -       Finish Date could not be calculated
```
