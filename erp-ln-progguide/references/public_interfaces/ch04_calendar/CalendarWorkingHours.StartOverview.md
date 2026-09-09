# CalendarWorkingHours.StartOverview

> Chapter: Chapter 4 Public Interfaces for Calendar
>
> Group: Public Interfaces for CalendarWorkingHour
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 156-157

```baan
DLL:   tcextccpapi
This function is available from 2024.11 (KB3522436).
Syntax: long CalendarWorkingHours.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcccp.ccal       iCalendarCode,
domain  tcccp.ract       iAvailabilityType,
domain  tcccp.date       iDate,
domain  tcccp.sern       iSequenceNumber,
domain  tctmhs           iStartTime,
domain  tcyesno          iShowDerivedWorkingTimes,
ref     domain  tcccp.ccal       oCalendarCode,
ref     domain  tcccp.ract       oAvailabilityType,
ref     domain  tcccp.date       oDate,
ref     domain  tcccp.sern       oSequenceNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Calendar Working Hours in
overview mode (tcccp0120m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Specifies the table-index that is to
be used.
Standard supported values:
3. Sort by Calendar Code, Availability
Type, Date,  Start Time, Sequence
Number (default).
iQueryExtend            A specific query to be used when zooming
to this session.
iCalendarCode           Calendar Code
iAvailabilityType       Availability Type
iDate                   Date
iSequenceNumber         Sequence Number
iStartTime              Start Time
iShowDerivedWorkingTimes
Show Derived Working Times
Output: Variables below contain the values of the selected record.
They are only filled if iStartMode is MODAL and 1 record has
been selected.
oCalendarCode           Calendar Code
oAvailabilityType       Availability Type
oDate                   Date
oSequenceNumber         Sequence Number
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started.
<> 0                    Otherwise.
```
