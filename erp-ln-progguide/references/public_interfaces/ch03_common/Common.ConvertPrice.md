# Common.ConvertPrice

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 102-103

```baan
DLL:   tcextcomapi
This function is available from     2022.03 (KB2220118  ).
Syntax: long Common.ConvertPrice(
domain  tcitem           iItem,
domain  tccitg           iItemGroup,
domain  tccuni           iInventoryUnit,
domain  tccuni           iFromUnit,
domain  tcconv           iConversionFactorBetweenFromUnitAndInventoryUnit,
domain  tccuni           iToUnit,
domain  tcconv           iConversionFactorBetweenInventoryUnitAndToUnit,
domain  tcpric           iPriceInFromUnit,
ref     domain  tcpric           oPriceInToUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This method converts a price expressed in "iFromUnit" to a price
expressed in "iToUnit".
Input:  If the "iInventoryUnit" or one of the conversion factors
(iConversionFactorBetweenFromUnitAndInventoryUnit /
iConversionFactorBetweenInventoryUnitAndToUnit) are
not filled the "iItem" (and possibly "iItemGroup") must be
filled so the function can search for this information by itself.
iItem                   Item Code
iItemGroup              Item Group
iInventoryUnit          Inventory Unit
iFromUnit               From Unit               Mandatory
iConversionFactorBetweenFromUnitAndInventoryUnit
Conversion Factor between "iFromUnit"
and "iInventoryUnit".
iToUnit                 To Unit                 Mandatory
iConversionFactorBetweenInventoryUnitAndToUnit
Conversion factor between "iInventoryUnit"
and "iToUnit".
iPriceInFromUnit        Price in "iFromUnit"
Output: oPriceInToUnit          Price in "iToUnit"
oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Succesfully Converted Price
<> 0                    Otherwise
```
