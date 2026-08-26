# HandlingUnit.Remove

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1049-1049

```baan
DLL:   whextwmdapi
This function is available from     2026.01 (KB3641117  ).
Syntax: long HandlingUnit.Remove(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will remove the iHandlingUnit. All the
child handling units will be removed as well.
The iHandlingUnit can be removed if:
1) iHandlingUnit has status 'Inactive' or 'Closed'
2) iHandlingUnit has children present and the status is not
equal to 'Closed'
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit                 - Handling Unit which must be removed (Mandatory)
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - iHandlingUnit is removed.
<> 0                          - Error
```
