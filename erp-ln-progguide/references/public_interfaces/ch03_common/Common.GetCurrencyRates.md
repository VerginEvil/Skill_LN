# Common.GetCurrencyRates

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Common
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 107-108

```baan
DLL:   tcextemmapi
This function is available from     2020.01 (KB2080844  ).
Syntax: long Common.GetCurrencyRates(
domain  tcncmp           iFinancialCompany,
domain  tcccur           iCurrency,
domain  tcdate           iRateDateUTC,
domain  tcrtyp           iExchangeRateType,
ref     domain  tcratc           oRates(),
ref     domain  tcratf           oRateFactors(),
ref     domain  tccrnd           oRoundingFactors(),
ref     domain  tcyesno          oExpressInBaseCurrency(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Get the rate data between a given transaction currency and the
home currencies. The home currencies are defined in session
"Companies" (tcemm1170m000).
To determine the rate data between two currencies a date and an
exchange rate type is needed. So these two values also need
to be provided.
Depending on the number of home currencies (with a maximum of
three) the rate data is filled. The rate data consists of the
following:
-                       rates
-                       rate factors
-                       rounding factors
-                       express in base currency
In the Standard Currency System, without Multiple Functional
Currencies set, only the local rate will be filled;
the reporting rates will not be determined in that case.
Pre:    Currency system needs to be setup in Companies (tcemm1170m000)
Rates must be defined between the currency and home currencies.
Post:                 -
Input:
iFinancialCompany                             - Financial Company: Mandatory
iCurrency                                     - Transaction currency for which the
rates to the home currencies have to
be retrieved: Mandatory
iRateDateUTC                                  - UTC date for which the rates have to
be retrieved: Mandatory
iExchangeRateType                             - Exchange rate type: Mandatory
Output:
oRates                                        - Array of rates.
oRateFactors                                  - Array of rate factors.
oRoundingFactors                              - Array of rounding factors.
oExpressInBaseCurrency                        - Array of flags (tcyesno) which
indicate if the currency is expressed
in the currency base.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Currency rates are found.
<> 0                                          - Otherwise.
```
