# Calendar.GetWorkingDays

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for Calendar
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 150-151

```baan
DLL:   tcextccpapi
This function is available from     2023.07 (KB2297011  ).
Syntax: long Calendar.GetWorkingDays(
domain  tcccp.ccal       iCalendarCode,
domain  tcccp.ract       iAvailabilityType,
domain  tczone           iTimeZone,
domain  tcdate           iStartDate,
domain  tcdate           iEndDate,
ref             long             oNumberOfWorkingDays,
ref     domain  tcdate           oWorkingDays(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the working days in the given interval
from the actual calendar.
Input:  iCalendarCode                         - Calendar Code, Mandatory
iAvailabilityType                             - Availability Type, Mandatory
iTimeZone                                     - Time Zone, Optional
If empty, It gets the system
time zone.
This is usually the›¼                                                 time zone of the
user, as defined in User Data Template
(ttams1110m000).
iStartDate                                    - Interval Start Date, Mandatory
Must exist in the calendar.
iEndDate                                      - Interval End Date, Mandatory
Must exist in the calendar.
Output: oNumberOfWorkingDays                  - Number of days in the Working Days
array.
oWorkingDays                                  - Array of working days.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Function is executed successfully.
<> 0                                          - An error occurred.
```
