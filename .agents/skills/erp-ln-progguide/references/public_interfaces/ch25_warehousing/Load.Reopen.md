# Load.Reopen

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Load
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1141-1141

```baan
DLL:   whextinhapi
This function is available from 2021.11 (KB2210929).
Syntax: long Load.Reopen(
domain  whinh.load       iLoad,
ref             boolean          oLoadReopened,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface reopens the frozen Load.
Pre:    db.retry.point()
Post:   abort/commit transaction
Input:  iLoad           - Mandatory
Output: oLoadReopened   - Load is reopened.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
