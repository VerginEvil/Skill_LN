# Attendance.GetAttendanceTypeClosingDifference

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1873-1873

```baan
DLL:   bpextxtmapi
This function is available from 2022.11 (KB2268271).
Syntax: long Attendance.GetAttendanceTypeClosingDifference(
ref     domain  bpxtm.atty       oAttendanceTypeClosingDifference,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns attendance type Closing Difference
for the employee group which is under review.
Pre:
Post:
Input:
Output:
oAttendanceTypeClosingDifference
- Attendance type Closing Difference
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Data read
```
