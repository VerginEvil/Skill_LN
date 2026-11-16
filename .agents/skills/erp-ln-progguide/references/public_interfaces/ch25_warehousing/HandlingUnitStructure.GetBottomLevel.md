# HandlingUnitStructure.GetBottomLevel

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnitStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1071-1072

```baan
DLL:   whextwmdapi
This function is available from 2021.10 (KB2210123).
Syntax: long HandlingUnitStructure.GetBottomLevel(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.long       oNumberOfHandlingUnits,
ref     domain  whhuid           oHandlingUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will search in the handling unit structure,
starting at the iHandlingUnit for bottom level handling units.
To explain this is more detail some examples will be given:
Handling Unit Structure has three levels:
Level 1 - container;
Level 2 - pallets;
Level 3 - boxes.
This function will return array with all boxes.
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
