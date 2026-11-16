# Attendance.UseAttendanceTypePostingDifferenceTypeClockOut

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1908-1908

```baan
DLL:   bpextxtmapi
This function is available from 2022.11 (KB2268271).
Syntax: long Attendance.UseAttendanceTypePostingDifferenceTypeClockOut(
ref             boolean          oUseAttendanceTypePostingDifferenceTypeClockOut,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns true when attendance type Posting
Difference Clock Out is being used for the employee group which
is under review.
Pre:
Post:
Input:
Output:
oUseAttendanceTypePostingDifferenceTypeClockOut
- Use attendance type Posting Difference
Type Clock Out (true/false)
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
