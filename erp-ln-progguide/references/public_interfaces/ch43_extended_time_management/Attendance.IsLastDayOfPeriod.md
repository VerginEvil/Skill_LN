# Attendance.IsLastDayOfPeriod

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1881-1881

```baan
DLL:   bpextxtmapi
This function is available from     2022.11 (KB2268271  ).
Syntax: long Attendance.IsLastDayOfPeriod(
ref             boolean          oLastDayOfPeriod,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns true when the date which is under review
is equal to the last day defined for attendance period.
Pre:
Post:
Input:
Output:
oLastDayOfPeriod                              - Is last day of period (true/false)
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
