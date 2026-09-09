# Common.RoundQuantity

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 113-114

```baan
DLL:   tcextcomapi
Syntax: long Common.RoundQuantity(
double           iUnroundedQuantity,
domain  tcmcs.st14       iDomainName,
domain  tccuni           iUnit,
ref             double           oRoundedQuantity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function rounds a quantity dependending on given
domain and unit.
Pre:    NA
Post:   NA
Input : iUnroundedQuantity      - The quantity that must be rounded.
iDomainName             - The domain name. (mandatory)
iUnit                   - The unit. (mandatory)
Output: oRoundedQuantity        - The rounded quantity.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return values:
0                       - Rounded quantity is returned
<> 0                    - on errors
```
