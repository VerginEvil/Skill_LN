# Common.ConvertAmountWithRates

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 100-101

```baan
DLL:   tcextemmapi
This function is available from 2023.09 (KB2300212).
Syntax: long Common.ConvertAmountWithRates(
domain  tcncmp           iFinancialCompany,
domain  tcamnt           iSourceAmount,
domain  tcccur           iSourceCurrency,
const   domain  tcratc           iSourceRates(),
const   domain  tcratf           iSourceRateFactors(),
domain  tcrtyp           iExchangeRateType,
domain  tcdate           iRateDateUTC,
domain  tcccur           iTargetCurrency,
ref     domain  tcamnt           oTargetAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts iSourceAmount (in iSourceCurrency) to
oTargetAmount (in iTargetCurrency) by means of the iSourceRates
and iSourceRatesFactors. The target rates that are used are
the rates defined for the home currencies and are defined by
the iRateDateUTC and iExchangeRateType.
If the iExchangeRateType is not passed, the function will
use the Internal Rate Type defined for the financial company.
Pre:    Finanial Company must be a valid company.
Post:   None
Input:
iFinancialCompany       - Financial Company: Mandatory
iSourceAmount           - Source Amount
iSourceCurrency         - Source Currency: Mandatory
iSourceRates            - Source Rates (array)
iSourceRateFactors      - Source Rate Factors (array)
iExchangeRateType       - Source Rate Type; if not filled,
the Internal Rate Type will be used.
iRateDateUTC            - Rate Date (UTC)
iTargetCurrency         - Target Currency: Mandatory
Output:
oTargetAmount           - Target Amount, result of the
conversion.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Amount is converted.
<> 0                    - Otherwise.
```
