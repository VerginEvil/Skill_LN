# Common.ConvertAmountWithTargetRates

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 101-102

```baan
DLL:   tcextemmapi
This function is available from 2023.11 (KB2303598).
Syntax: long Common.ConvertAmountWithTargetRates(
domain  tcncmp           iFinancialCompany,
domain  tcamnt           iSourceAmount,
domain  tcccur           iSourceCurrency,
domain  tcdate           iSourceRateDateUTC,
const   domain  tcratc           iTargetRates(),
const   domain  tcratf           iTargetRateFactors(),
domain  tcrtyp           iExchangeRateType,
domain  tcccur           iTargetCurrency,
ref     domain  tcamnt           oTargetAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:     Expl: This function converts iSourceAmount (in iSourceCurrency) to
oTargetAmount (in iTargetCurrency) by means of the iTargetRates
and iTargetRatesFactors. The source rates that are used are
the rates defined for the home currencies and are defined by
the iSourceRateDateUTC and iExchangeRateType.
Pre:  Finanial Company must be a valid company.
Post: None
Input:
iFinancialCompany            - Financial Company: Mandatory
iSourceAmount                - Source Amount
iSourceCurrency              - Source Currency: Mandatory
iSourceRateDateUTC           - Source Rate Date (UTC)
iTargetRates                 - Target Rates (array)
itargetRateFactors           - Target Rate Factors (array)
iExchangeRateType            - Target Rate Type,
if not filled, the Internal Rate Type
will be used.
iTargetCurrency              - Target Currency: Mandatory
Output:
oTargetAmount                - Target Amount, result of the
conversion.
oExceptionMessage            - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                 - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return:    0                       - Amount is converted.
<> 0                    - Otherwise.
```
