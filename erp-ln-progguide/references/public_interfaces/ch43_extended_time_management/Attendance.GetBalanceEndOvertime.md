# Attendance.GetBalanceEndOvertime

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1879-1880

```baan
DLL:   bpextxtmapi
This function is available from 2022.11 (KB2268271).
Syntax: long Attendance.GetBalanceEndOvertime(
ref     domain  bpxtm.hours      oBalanceEndOvertimeHours,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns a number of balance overtime end hours
calculated for the employee, depratment, employee group,
period table code, and period which are under review.
Pre:
Post:
Input:
Output:
oBalanceEndOvertimeHours
- Number of balance overtime end hours
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
