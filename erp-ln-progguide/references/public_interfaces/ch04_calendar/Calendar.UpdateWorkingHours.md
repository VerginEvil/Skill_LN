# Calendar.UpdateWorkingHours

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for Calendar
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 155-156

```baan
DLL:   tcextccpapi
This function is available from 2024.11 (KB3522420).
Syntax: long Calendar.UpdateWorkingHours(
domain  tcccp.ccal       iCalendarCode,
domain  tcccp.ract       iAvailabilityType,
domain  tcyesno          iOnlyChangedCalendars,
domain  tcyesno          iProcessChildCalendars,
domain  tcyesno          iRestoreCalendarDefaults,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Updates the Calendar working hours for the given
Calendar and Availability Type.
Input:
iCalendarCode                   Calendar Code (Mandatory).
iAvailabilityType               Availability Type (Mandatory).
iOnlyChangedCalendars           Only process changed calendars.
iProcessChildCalendars          Process child calendars.
iRestoreCalendarDefaults        Restore calendar defaults
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Updated successfully.
<> 0                    - An error occurred.
```
