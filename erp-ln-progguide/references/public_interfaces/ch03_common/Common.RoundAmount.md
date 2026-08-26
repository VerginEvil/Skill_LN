# Common.RoundAmount

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 112-112

```baan
DLL:   tcextcomapi
Syntax: long Common.RoundAmount(
double           iUnroundedAmount,
domain  tcmcs.st14       iDomainName,
domain  tcccur           iCurrency,
ref             double           oRoundedAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This functions rounds an amount with a given domain and currency.
Pre:    NA
Post:   NA
Input : iUnroundedAmount                      - The amount that must be rounded.
iDomainName                                   - The domain name. (mandatory)
iCurrency                                     - The currency. (mandatory)
Output: oRoundedAmount                        - The rounded amount.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return values:
0                                             - Rounded amount is returned
<> 0                                          - on errors
```
