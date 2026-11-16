# Calendar.StartUpdateWorkingHours

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for Calendar
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 154-155

```baan
DLL:   tcextccpapi
This function is available from 2024.11 (KB3522420).
Syntax: long Calendar.StartUpdateWorkingHours(
long             iStartMode,
domain  tcccp.ccal       iCalendarCodeFrom,
domain  tcccp.ccal       iCalendarCodeTo,
domain  tcccp.ract       iAvailabilityTypeFrom,
domain  tcccp.ract       iAvailabilityTypeTo,
domain  tcyesno          iOnlyChangedCalendars,
domain  tcyesno          iProcessChildCalendars,
domain  tcyesno          iRestoreCalendarDefaults,
domain  tcyesno          iParallelProcessing,
domain  tcyesno          iProcessReport,
domain  tcyesno          iErrorReport,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function Starts the process session
Update Calendar Working Hours (tcccp0226m000).
Input:
iStartMode                      Start Mode
Possible values are:
MODAL - The parent session is
blocked until the child session
exits. The session will be
started as a zoom session.
iCalendarCodeFrom               Calendar code from
iCalendarCodeTo                 Calendar code to
iAvailabilityTypeFrom           Availability Type from
iAvailabilityTypeTo             Availability Type from
iOnlyChangedCalendars           Only process changed calendars
iProcessChildCalendars          Process child calendars.
This field is not applicable when
Calendar code and Availability type
is run for full range and
Only changed calendars is NO.
iRestoreCalendarDefaults        Restore calendar defaults
iParallelProcessing             Parallel Processing
iProcessReport                  Process Report
iErrorReport                    Error Report
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started successfully.
<> 0                    - An error occurred.
```
