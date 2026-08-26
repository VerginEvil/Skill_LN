# AdjustmentOrder.GenerateHandlingUnitsV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for AdjustmentOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 897-898

```baan
DLL:   whextinhapi
This function is available from     2025.11 (KB3630769  ).
Syntax: long AdjustmentOrder.GenerateHandlingUnitsV2(
domain  tcorno           iAdjustmentOrder,
domain  tcpono           iAdjustmentLine,
domain  whwmd.pkdf       iPackageDefinition,
boolean          iOverwritePackageDefinition,
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
iPackageDefinition                       - Package Definition; Optional
iOverwritePackageDefinition                       - Boolean indicating whether to
overwrite the package definition field
on the adjustment line if it's already
filled.
True:
The specified package definition will
always be used to generate the handling
unit.
false:
The specified package definition will
only be used to generate the handling
unit, if the package definition field is
not already filled on the adjustment
line.
The specified package definition will be
used if the package definition on the
adjustment line was empty.
Output: oNoHandlingUnits                      - Number of generated Handling Units
oHandlingUnitArray                            - Array with all the generated Handling
Units
Return: 0: OK, <> 0: Error
```
