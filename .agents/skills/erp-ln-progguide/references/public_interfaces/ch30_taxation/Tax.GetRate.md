# Tax.GetRate

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1646-1647

```baan
DLL:   tcexttaxapi
This function is available from 2022.05 (KB2236284).
Syntax: long Tax.GetRate(
domain  tcncmp           iCompany,
domain  tcccty           iTaxCountry,
domain  tccvat           iTaxCode,
domain  tcdate           iEffectiveDate,
ref     domain  tcpvat           oTaxRate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the Tax Rate of a Tax Country/Tax Code
combination. If the Tax Code is a Group Tax Code the VAT Tax Code
of that group is used instead.
Pre:    na
Post:   na
Input:  iCompany                - Company (mandatory)
iTaxCountry             - Tax Country (mandatory)
iTaxCode                - Tax Code (mandatory)
iEffectiveDate          - Effective date (mandatory)
Output: oTaxRate                - Tax Rate
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       succes
<> 0                    error
```
