# HandlingUnit.ConfirmReceipt

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1044-1045

```baan
DLL:   whextinhapi
This function is available from 2021.08 (KB2196655).
Syntax: long HandlingUnit.ConfirmReceipt(
domain  whhuid           iHandlingUnit,
ref             boolean          oHandlingUnitConfirmed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will confirm the given handling unit.
When successful, also the automatic inbound process is started
for this receipt line.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iHandlingUnit           - Mandatory
Output: oHandlingUnitConfirmed  - Handling Unit is confirmed
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
