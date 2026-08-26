# Common.UpdateApprovedConversionFactor

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 113-114

```baan
DLL:   tcextcomapi
This function is available from     2022.04 (KB2235599  ).
Syntax: long Common.UpdateApprovedConversionFactor(
domain  tcitem           iItem,
domain  tccitg           iItemGroup,
domain  tccuni           iFromUnit,
domain  tccuni           iToUnit,
domain  tcconv           iConversionFactor,
domain  tcrpow           iConversionFactorExponent,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface updates an approved conversion factor.
The given Item cannot have Inventory, a Package Definition,
Requisition Lines or a Quotation for the Conversion Factor to be
updated.
The given Item Group cannot have Inventory for the Conversion
Factor to be changed.
As generic Conversion Factors cannot be changed, either iItem,
iItemGroup or both need to be filled.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iItem                   Item Code (Mandatory if iItemGroup is
empty).
iItemGroup              Item Group  (Mandatory if iItem is
empty).
iFromUnit               From Unit (Mandatory).
iToUnit                 To Unit (Mandatory).
iConversionFactor       New Conversion Factor between
"iFromUnit" and "iToUnit". Should be
positive (Mandatory).
iConversionFactorExponent
New Conversion Factor exponent.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
found, these are present in the
oExceptionID
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Succesfully updated the Conversion
Factor.
<> 0                    Otherwise.
```
