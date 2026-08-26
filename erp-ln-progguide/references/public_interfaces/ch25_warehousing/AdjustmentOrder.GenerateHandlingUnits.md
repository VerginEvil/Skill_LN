# AdjustmentOrder.GenerateHandlingUnits

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for AdjustmentOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 896-897

```baan
DLL:   whextinhapi
This function is available from     2025.05 (KB3565249  ).
Syntax: long AdjustmentOrder.GenerateHandlingUnits(
domain  tcorno           iAdjustmentOrder,
domain  tcpono           iAdjustmentLine,
ref             long             oNoHandlingUnits,
ref     domain  whhuid           oHandlingUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will generate a handling unit for every line of
the adjustment order
Pre:    db.retry.point()
oHandlingUnitArray must be declared as a based variable, no
memory allocation is necessary
Post:   abort.transaction() or commit.transaction()
Free memory of oHandlingUnitArray
Input:  iAdjustmentOrder               - Adjustment Order; Mandatory
iAdjustmentLine                       - Adjustment Line; when equal to 0 handling unit
will be generated for every line
Output: oNoHandlingUnits                      - Number of generated Handling Units
oHandlingUnitArray                            - Array with all the generated Handling
Units
Return: 0: OK, <> 0: Error
```
