# NonConformanceReport.StartDetail

> Chapter: Chapter 35 Public Interfaces for Quality Management
>
> Group: Public Interfaces for NonConformanceReport
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1793-1793

```baan
DLL:   qmextncmapi
This function is available from 2022.08 (KB2226027).
Syntax: long NonConformanceReport.StartDetail(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iNonConformanceReport,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Non-Conformance Report
(qmncm1100m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, in case of a
multi-occurrence the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
Not Used.
Following input variables form the primary key, these fields
are mandatory, if the primary key cannot be found an API error
will be set in the oExceptionMessage and the session will not
be started.
Primary Key Fields:
iNonConformanceReport
- Non-Conformance Report; Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - An error occurred
```
