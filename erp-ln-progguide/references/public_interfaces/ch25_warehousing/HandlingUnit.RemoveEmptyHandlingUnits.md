# HandlingUnit.RemoveEmptyHandlingUnits

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1049-1050

```baan
DLL:   whextwmdapi
This function is available from     2023.05 (KB2288542  ).
Syntax: long HandlingUnit.RemoveEmptyHandlingUnits(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will remove empty handling units from
the handling unit structure.
Handling unit must have status Staged or Projected.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iHandlingUnit               - Handling Unit (Mandatory)
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Empty Handling Unit structure are removed successfully
<> 0                          - Error
```
