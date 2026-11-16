# ProductionOrderHours.CloseActiveLine

> Chapter: Chapter 45 Public Interfaces for Time Management
>
> Group: Public Interfaces for ProductionOrderHours
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1916-1917

```baan
DLL:   bpexttmmapi
This function is available from 2023.02 (KB2272425).
Syntax: long ProductionOrderHours.CloseActiveLine(
domain  tcemno           iEmployee,
domain  tcccp.yrno       iYear,
domain  tcccp.peri       iPeriod,
domain  bpmdm.serd       iSequence,
domain  tcdate           iEndDateTime,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to close the inserted active
production order hours line resulting in update of the hours
line with the spent time and possible new hours lines for next
period(s).
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iEmployee               - Employee              (Mandatory)
iYear                   - Year                  (Mandatory)
iPeriod                 - Period                (Mandatory)
iSequence               - Sequence              (Mandatory)
iEndDateTime            - End Date and Time     (Mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Active Production Order Hours Line
has been closed.
<> 0                    - Error while closing active Production
Order Hours Line.
```
