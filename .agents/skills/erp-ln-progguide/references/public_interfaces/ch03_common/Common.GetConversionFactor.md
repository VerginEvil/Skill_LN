# Common.GetConversionFactor

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 107-108

```baan
DLL:   tcextcomapi
This function is available from 2022.02 (KB2200198).
Syntax: long Common.GetConversionFactor(
domain  tcitem           iItem,
domain  tccitg           iItemGroup,
domain  tccuni           iFromUnit,
domain  tccuni           iToUnit,
ref     domain  tcconv           oConversionFactor,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function returns the conversion factor between the given
units. The item argument allows for a search on item level. The
Item, Item Group and To Unit arguments will all speed up the
search if entered.
Pre:    -
Post:   -
Input:  iItem                   - Item (Optional).
iItemGroup              - Item Group (Optional).
iFromUnit               - From Unit (Mandatory if iItem is
empty).
iToUnit                 - To Unit (Mandatory).
Output: oConversionFactor       - Conversion Factor.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Conversion Factor successfully
retrieved.
<> 0                    - Otherwise.
```
