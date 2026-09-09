# NonConformanceReport.SetStatus

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for NonConformanceReport
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1792-1792

```baan
DLL:   qmextncmapi
This function is available from 2023.01 (KB2274383).
Syntax: long NonConformanceReport.SetStatus(
domain  tcorno           iNonConformanceReport,
domain  qmncm.stat       iNonConformanceReportStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will set Non Conformance Report status.
This function must not be called within a logical transaction
as this function will have it's own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iNonConformanceReport   - Non Conformance Report; Mandatory
iNonConformanceReportStatus - Non Conformance Report Status; Mandatory
qmncm.stat.open         - Open (Reset)
qmncm.stat.submitted    - Submitted (Reset if
status is other than Open)
qmncm.stat.assigned     - Assigned
qmncm.stat.dispositioned- Dispositioned
qmncm.stat.cancelled    - Canceled
qmncm.stat.closed       - Closed
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Non Conformance Report Status changed to given status.
<> 0    - Non Conformance Report Status could not be changed.
```
