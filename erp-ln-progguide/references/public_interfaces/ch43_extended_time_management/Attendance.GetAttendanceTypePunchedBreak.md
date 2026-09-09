# Attendance.GetAttendanceTypePunchedBreak

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1876-1876

```baan
DLL:   bpextxtmapi
This function is available from 2022.11 (KB2268271).
Syntax: long Attendance.GetAttendanceTypePunchedBreak(
ref     domain  bpxtm.atty       oAttendanceTypePunchedBreak,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns attendance type Punched Break
for the employee group which is under review.
Pre:
Post:
Input:
Output:
oAttendanceTypePunchedBreak
- Attendance type Punched Break
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
