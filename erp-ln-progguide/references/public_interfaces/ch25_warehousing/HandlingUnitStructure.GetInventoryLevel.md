# HandlingUnitStructure.GetInventoryLevel

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnitStructure
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1063-1064

```baan
DLL:   whextwmdapi
This function is available from     2021.10 (KB2210123  ).
Syntax: long HandlingUnitStructure.GetInventoryLevel(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.long       oNumberOfHandlingUnits,
ref     domain  whhuid           oHandlingUnitArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will search in the handling unit structure,
starting at the iHandlingUnit for handling units which contain
the inventory level.
To explain this is more detail some examples will be given:
Example 1:
Item A_LOT is lot                      -controlled item.
Top handling unit iHandlingUnit is multi                      -lot HU.
First child HU_CHILD1 contains LOT1.
Second child HU_CHILD2 contains LOT2.
Function will return array with 2 handling units:
-                       HU_CHILD1
-                       HU_CHILD2
Example 2:
Item A_LOT is lot                      -controlled item.
Top handling unit iHandlingUnit and both child handling units
HU_CHILD1 and HU_CHILD2 contain the same lot LOT0.
Function will return array with 1 handling unit HU_TOP.
Example 3:
Item A_LOT is lot                      -controlled and serialized item.
Top handling unit iHandlingUnit and both child handling units
HU_CHILD1 and HU_CHILD2 contain the same lot LOT0.
Handling Unit HU_CHILD1 contains serial number SERIAL1.
Handling Unit HU_CHILD2 contains serial number SERIAL2.
Function will return array with 2 handling units:
-                       HU_CHILD1
-                       HU_CHILD2
Pre:    oHandlingUnitArray must be declared as based variable.
This function will allocate the memory.
Post:   NA
Input:  iHandlingUnit                         - Handling Unit (mandatory)
Output: oNumberHandlingUnits                  - Number of handling units in array.
oHandlingUnitArray                            - Array with handling units.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
