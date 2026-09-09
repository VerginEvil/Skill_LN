# WorkCenter.GetCalendar

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for WorkCenter
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 809-809

```baan
DLL:   tiextrouapi
This function is available from 2024.11 (KB3522422).
Syntax: long WorkCenter.GetCalendar(
domain  tccwoc           iWorkCenter,
ref     domain  tcccp.ccal       oCalendarCode,
ref     domain  tcccp.ract       oCalendarAvailabilityType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the calendar code and calendar
availability type for a given work center.
In some scenarios, even functions return 0. oCalendarCode
and oCalendarAvailabilityType can be empty. If those are not
defined for the work center.
Input:  iWorkCenter             - The Work Center for which the calendar
information needs to be obtained
Output: oCalendarCode           - The Calendar used for the Work Center
oCalendarAvailabilityType
- The Calendar Availability Type used
for the Work Center
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function is executed successfully.
<> 0                    - An error occurred.
```
