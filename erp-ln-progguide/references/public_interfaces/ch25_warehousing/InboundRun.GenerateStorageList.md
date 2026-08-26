# InboundRun.GenerateStorageList

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundRun
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1086-1087

```baan
DLL:   whextinhapi
This function is available from     2023.11 (KB2304787  ).
Syntax: long InboundRun.GenerateStorageList(
domain  whinh.btno       iInboundRun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will generate a storage list for the
inbound run.
No data is printed.
Be aware that transaction management is handled within this
function.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iInboundRun                           - Inbound run (Mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
