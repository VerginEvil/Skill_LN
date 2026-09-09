# Tax.ProcessTestScenario

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1647-1648

```baan
DLL:   tcexttaxapi
This function is available from 2023.12 (KB2314899).
Syntax: long Tax.ProcessTestScenario(
const   domain  tclogn           iLogonCode,
domain  tctax.seqn       iTestNumber,
ref     domain  tcccty           oTaxCountry,
ref     domain  tccvat           oTaxCode,
ref     domain  tcpvat           oTaxRate,
ref     domain  tcmcs.cste       oTaxState,
ref     domain  tcezty           oTaxEconomicZoneType,
ref     domain  tcccty           oBusinessPartnerTaxCountry,
ref     domain  tcmcs.cste       oBusinessPartnerTaxState,
ref     domain  tcezty           oBusinessPartnerTaxEconomicZoneType,
ref     domain  tcyesno          oExempt,
ref     domain  tcfovn           oExemptCertificate,
ref     domain  tccdis           oExemptReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes the given tax scenario and returns
the results.
Pre:    The test scenario to be processed must be available in
session 'Test Tax Scenario' (tctax8100m000).
Post:   na
Input:  iLogonCode              - Logon Code (mandatory)
iTestNumber             - Test Number(mandatory)
Output: oTaxCountry             - Tax Country
oTaxCode                - Tax Code
oTaxRate                - Tax Rate
oTaxState               - Tax State
oTaxEconomicZoneType    - Tax Economic Zone Type
oBusinessPartnerTaxCountry
- Business Partner Tax Country
oBusinessPartnerTaxState- Business Partner Tax State
oBusinessPartnerTaxEconomicZoneType
- Business Partner Tax Economic Zone Type
oExempt                 - Exempt
oExemptCertificate      - Exempt Certificate
oExemptReason           - Exempt Reason
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - succes
<> 0                    - otherwise
```
