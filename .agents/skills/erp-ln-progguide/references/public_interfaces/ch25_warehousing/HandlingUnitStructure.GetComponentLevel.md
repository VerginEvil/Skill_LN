# HandlingUnitStructure.GetComponentLevel

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnitStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1072-1073

```baan
DLL:   whextwmdapi
This function is available from 2021.10 (KB2212145).
Syntax: long HandlingUnitStructure.GetComponentLevel(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.long       oNumberOfHandlingUnits,
ref     domain  whhuid           oHandlingUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will search in the handling unit structure,
starting at the iHandlingUnit for handling units which
contain components of the main item.
To explain this is more detail an example will be given:
Handling Unit Structure is created for List/BOM item and
contains both main item MAIN_ITEM and components COMP1 and
COMP2.
Handling Unit Structure has three levels:
Level 1 - HU1 container with MAIN_ITEM
Level 2 - HU2.1 pallet with component COMP1
Level 3 - HU 3.1 10 boxes with component COMP1
Level 2 - HU2.2 pallet with component COMP2
Level 3 - HU3.2 10 boxes with component COMP2
This public interface will return array with 2 handling units:
- HU2.1 containing component COMP1
- HU2.2 containing component COMP2
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
