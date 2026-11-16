# OutboundRun.UndoAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundRun
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1210-1210

```baan
DLL:   whextinhapi
This function is available from 2025.12 (KB3613235).
Syntax: long OutboundRun.UndoAdvice(
domain  whinh.btno       iOutboundRun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will remove the advice lines with the given run
number which have not been released yet.
This function has its own transaction management. It is not
allowed to call this inside a logical transaction.
When errors occur during the process the errors are visible
in the oExceptionID and the last message is present in
oExceptionMessage.
Pre:    NA
Post:   NA
Input:  iOutboundRun            - Run Number (Mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
