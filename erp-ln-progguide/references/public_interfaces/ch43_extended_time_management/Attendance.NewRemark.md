# Attendance.NewRemark

> Chapter: Chapter 43 Public Interfaces for Extended Time Management
>
> Group: Public Interfaces for Attendance
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1881-1882

```baan
DLL:   bpextxtmapi
This function is available from     2022.11 (KB2268271  ).
Syntax: long Attendance.NewRemark(
domain  bpxtm.rem.code   iCode,
domain  bpxtm.rem.text   iText mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates a new remark using the employee and
department which are under review, if there is yes in the
field "Generate Remarks" (bpxtm000.gere).
Pre:
Post:
Input:
iCode                                         - Code
iText                                         - Text
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Remark created
<> 0                                          - An error occurred
```
