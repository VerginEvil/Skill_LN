# Common.ConvertQuantity

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 103-104

```baan
DLL:   tcextcomapi
This function is available from     2019.03 (KB2042397  ).
Syntax: long Common.ConvertQuantity(
domain  tcitem           iItem,
domain  tccuni           iFromUnit,
domain  tcqst1           iFromQuantity,
domain  tccuni           iToUnit,
ref     domain  tcqst1           oToQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts a quantity specified in a unit to
a quantity specified in another unit.
Rounding will not be done. Common.RoundQuantity can be used for
rounding.
Post:   None
Input:  iItem                                 - Item
iFromUnit                                     - From Unit: Mandatory
iFromQuantity                                 - From Quantity
iToUnit                                       - To Unit: Mandatory
Output: oToQuantity                           - To Quantity
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                             - Quantity is converted.
<> 0                                  - Otherwise.
```
