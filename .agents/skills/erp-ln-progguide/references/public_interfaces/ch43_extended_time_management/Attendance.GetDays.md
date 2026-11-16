# Attendance.GetDays

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1883-1883

```baan
DLL:   bpextxtmapi
This function is available from 2022.11 (KB2268271).
Syntax: long Attendance.GetDays(
domain  bpxtm.atty       iAttendanceType,
ref     domain  bpxtm.days       oDays,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns a number of days calculated for the
employee, depratment, employee group, period table code, period,
and date which are under review and given attendance type.
Pre:
Post:
Input:
iAttendanceType         - Attendance type
Output:
oDays                   - Number of days
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:         0                       - Data read
```
