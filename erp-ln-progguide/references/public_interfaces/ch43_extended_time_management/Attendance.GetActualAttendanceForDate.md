# Attendance.GetActualAttendanceForDate

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1849-1849

```baan
DLL:   bpextxtmapi
This function is available from     2022.11 (KB2268271  ).
Syntax: long Attendance.GetActualAttendanceForDate(
domain  bpxtm.atty       iAttendanceType,
domain  tcyesno          iManuallyAdded,
domain  bpxtm.date       iDate,
ref     domain  bpxtm.hours      oActualAttendance,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns a number of hours calculated for the
attendance type for the employee which is under review
and given attendance type, manually added, and date.
Pre:
Post:
Input:
iAttendanceType                               - Attendance type
iManuallyAdded                                - Manually added
iDate                                         - Date
Output:
oActualAttendance                             - number of hours Actual Attendance
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Data read
```
