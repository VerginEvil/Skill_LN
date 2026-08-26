# BOD.ConvertFromISOUnitToERP

> Chapter: Chapter 31 Public Interfaces for BOD & BDE
>
> Group: Public Interfaces for BOD
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1637-1638

```baan
DLL:   tcextbodapi
This function is available from     2023.08 (KB2302511  ).
Syntax: long BOD.ConvertFromISOUnitToERP(
domain  tcitem           iItem,
domain  tcictc           iUnit,
boolean          iCheckUnitSet,
boolean          iCheckConversionFactor,
ref     domain  tccuni           oERPUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts the ISO unit code, to the ERP unit code.
When item is empty, first unit found with the correct
ISO code, is returned; when no unit is found, unit is
searched for that has empty ISO code and with unit equal to
the ISO code.
When item is filled, last unit found with the correct
ISO code, and found unit is in unit set of item and has
conversion factor to the item's inventory unit, is returned.
When unit found equals inventory unit or weight unit of item,
this unit overrules other units and is returned;
when no unit is found, unit is searched for that has empty
ISO code and with unit equal to the ISO code.
Example 1:
-                         units with correct ISO code and in unit set with valid
conversion factor: A, B and C
-                         inventory unit of item = B
-                         B is always returned
Example 2:
-                         units with correct ISO code and in unit set with valid
conversion factor: A, B and C
-                         inventory unit of item = D
-                         C is returned
Example 3:
-                         no units with correct ISO code
-                         there is a unit X that equals the ISO code X
-                         X is returned
Pre:    NA
Post:   NA
Input:  iItem                                 - ERP Item
iUnit                                         - ISO unit code. Mandatory
iCheckUnitSet                                 - unit set must be checked, true/false
iCheckConversionFactor                        - conv factor must be checked, true/false
Output: oERPUnit                              - ERP Unit code
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - OK.
<> 0                                          - Error occurred.
```
