# Weight.Convert

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Weight
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1291-1291

```baan
DLL:   whextwmdapi
This function is available from 2021.11 (KB2211532).
Syntax: long Weight.Convert(
domain  tcwght           iWeight,
domain  tccuni           iFromWeightUnit,
domain  tccuni           iToWeightUnit,
ref     domain  tcwght           oConvertedWeight,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface converts a weight to a different weight
unit.
Pre:    N.A.
Post:   N.A.
Input:  iWeight                 - Weight to be convert, expressed in
iFromWeightUnit
iFromWeightUnit         - Initial weight unit to convert from
(Mandatory)
iToWeightUnit           - Desired weight unit to convert to
(Mandatory)
Output: oConvertedWeight        - The converted weight, expressed in
iToWeightUnit.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: N.A.
```
