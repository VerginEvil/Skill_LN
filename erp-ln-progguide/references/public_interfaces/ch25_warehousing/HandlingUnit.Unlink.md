# HandlingUnit.Unlink

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1058-1058

```baan
DLL:   whextwmdapi
This function is available from     2021.08 (KB2200928  ).
Syntax: long HandlingUnit.Unlink(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will unlink the handling unit from its
parent handling unit.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit               - Handling Unit (Mandatory)
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Handling Unit structure is unlinked successfully
<> 0                          - Error
```
