# Attendance.DeleteActualAttendanceGenerated

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1867-1867

```baan
DLL:   bpextxtmapi
This function is available from 2022.11 (KB2268271).
Syntax: long Attendance.DeleteActualAttendanceGenerated(
domain  bpxtm.atty       iAttendanceType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function deletes all records from the table Actual
Attendance (bpxtm250) for the employee and date which are
under review and given attendance type no in the field
"Manually Added" (bpxtm250.maad).
Pre:    db.retry.point
Post:   commit.transaction
Input:
iAttendanceType - Attendance type
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Records deleted
<> 0                    - An error occurred
```
