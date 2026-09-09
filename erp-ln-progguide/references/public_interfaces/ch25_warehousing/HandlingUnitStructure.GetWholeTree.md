# HandlingUnitStructure.GetWholeTree

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnitStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1074-1075

```baan
DLL:   whextwmdapi
This function is available from 2021.10 (KB2212145).
Syntax: long HandlingUnitStructure.GetWholeTree(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.long       oNumberOfHandlingUnits,
ref     domain  whhuid           oHandlingUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will search in the handling unit structure,
starting at the iHandlingUnit for all handling units.
To explain this is more detail an example will be given:
Handling Unit Structure has three levels:
Handling Unit Structure has three levels:
Level 1 - HU1                           1 Container
Level 2 - HU2.1                 1 Pallet
Level 3 - HU3.1         2 Boxes
Level 3 = HU3.2         2 Boxes
Level 2 - HU2.2                 1 Pallet
Level 3 - HU3.3         2 Boxes
Level 3 - HU3.4         2 Boxes
This public interface will return array with all handling units
in this order:
Position in array
Handling Unit
1    2      3      4       5      6      7
HU1, HU2.1, HU3.1, HU3.2,  HU2.2, HU3.3, HU3.4
Pre:    oHandlingUnitArray must be declared as based variable.
This function will allocate the memory.
Post:   NA
Input:  iHandlingUnit           - Handling Unit (mandatory)
Output: oNumberHandlingUnits    - Number of handling units in array.
oHandlingUnitArray      - Array with handling units.
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
