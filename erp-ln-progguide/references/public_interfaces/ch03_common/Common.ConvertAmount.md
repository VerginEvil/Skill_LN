# Common.ConvertAmount

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 97-98

```baan
DLL:   tcextemmapi
Syntax: long Common.ConvertAmount(
domain  tcncmp           iFinancialCompany,
domain  tcamnt           iSourceAmount,
domain  tcccur           iSourceCurrency,
domain  tcrtyp           iExchangeRateType,
domain  tcdate           iRateDateUTC,
domain  tcccur           iTargetCurrency,
ref     domain  tcamnt           oTargetAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts an amount in one currency to
an amount in another currency.
The rates are read based on the given iRateDateUTC for the
given iExchangeRateType. If the iExchangeRateType is not passed,
the function will use the Internal Rate Type defined for the
company.
Pre:    Company must be a valid company.
Post:   None
Input:
iFinancialCompany                             - Financial Company: Mandatory
iSourceAmount                                 - Source Amount
iSourceCurrency                               - Source Currency: Mandatory
iExchangeRateType                             - Source Rate Type; if not filled,
the Internal Rate Type will be used.
iRateDateUTC                                  - Rate Date (UTC)
iTargetCurrency                               - Target Currency: Mandatory
Output:
oTargetAmount                                 - Target Amount, result of the
conversion.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Amount is converted.
<> 0                                          - Otherwise.
```
