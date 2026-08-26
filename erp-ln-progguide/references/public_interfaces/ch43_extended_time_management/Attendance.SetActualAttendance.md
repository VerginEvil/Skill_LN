# Attendance.SetActualAttendance

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1882-1883

```baan
DLL:   bpextxtmapi
This function is available from     2022.11 (KB2268271  ).
Syntax: long Attendance.SetActualAttendance(
domain  bpxtm.atty       iAttendanceType,
domain  tcyesno          iManuallyAdded,
domain  bpxtm.hours      iNumberOfHours,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function sets a new value in the field "Number of Hours"
(bpxtm250.hour) for a record in the table "Attendance type"
(bpxtm250) for the employee and date which are under review
and given attendance type and manually added.
If the record exists the number of hours will be overwritten.
If the record does not exist a new record will be created.
Pre:    db.retry.point
Post:   commit.transaction
Input:
iAttendanceType                       - Attendance type
iManuallyAdded                        - Manually added
iNumberOfHours                        - Number of hours
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Record updated
<> 0                                          - An error occurred
```
