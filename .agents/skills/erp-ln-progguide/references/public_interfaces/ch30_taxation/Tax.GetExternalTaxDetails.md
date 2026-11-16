# Tax.GetExternalTaxDetails

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1644-1645

```baan
DLL:   tcexttaxapi
This function is available from 2023.11 (KB2308588).
Syntax: long Tax.GetExternalTaxDetails(
domain  tcmcs.xml        iTaxCalcResultsNode,
ref             long             oNumberOfTaxLevels,
ref     domain  tccvat           oLineTaxCodeArray() fixed,
ref     domain  tcamnt           oTaxableAmountArray(),
ref     domain  tcamnt           oNonTaxableAmountArray(),
ref     domain  tcamnt           oExemptAmountArray(),
ref     domain  tcyesno          oExemptArray(),
ref     domain  tcfovn           oExemptCertificateArray() fixed,
ref     domain  tcamnt           oTaxAmountArray(),
ref     domain  tcpvat           oTaxPercentageArray(),
ref     domain  tcctau.type      oTaxAuthorityTypeArray(),
ref     domain  tcmcs.ctau       oTaxAuthorityArray() fixed,
ref     domain  tcdsca           oTaxAuthorityDescriptionArray() fixed mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function gets the external tax result attributes of
the given XML node in which the results of the tax
calculation are stored.
Pre:    None
Post:   None
Input
iTaxCalcResultsNode             - Tax Calculation Results Node:
Mandatory
oNumberOfTaxLevels              - Number Of Tax Levels
oLineTaxCodeArray               - Line Tax Code (array)
oTaxableAmountArray             - Taxable Amount (array)
oNonTaxableAmountArray          - Non Taxable Amount (array)
oExemptAmountArray              - Exempt Amount (array)
oExemptArray                    - Exempt (array)
oExemptCertificateArray         - Exempt Certificate (array)
oTaxAmountArray                 - Tax Amount (array)
oTaxPercentageArray             - Tax Percentage (array)
oTaxAuthorityTypeArray          - Tax Authority Type (array)
oTaxAuthorityArray              - Tax Authority (array)
oTaxAuthorityDescriptionArray   - Tax Authority Description (array)
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Correct.
<> 0                    - Otherwise.
```
