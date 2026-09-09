# Tax.GetInternalTaxDetails

> Chapter: Chapter 30 Public Interfaces for Taxation
>
> Group: Public Interfaces for Tax
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1645-1646

```baan
DLL:   tcexttaxapi
This function is available from 2023.11 (KB2308588).
Syntax: long Tax.GetInternalTaxDetails(
domain  tcmcs.xml        iTaxCalcResultsNode,
ref             long             oNumberOfTaxLines,
ref     domain  tccvat           oLineTaxCodeArray() fixed,
ref     domain  tcamnt           oTaxableAmountArray(),
ref     domain  tcamnt           oExemptAmountArray(),
ref     domain  tcyesno          oExemptArray(),
ref     domain  tcamnt           oTaxAmountArray(),
ref     domain  tcamnt           oShiftedTaxAmountArray(),
ref     domain  tcamnt           oClaimableTaxAmountArray(),
ref     domain  tcamnt           oNonClaimableTaxAmountArray(),
ref     domain  tcpvat           oTaxPercentageArray(),
ref     domain  tcmcs.ctau       oTaxAuthorityArray() fixed,
ref     domain  tcdsca           oTaxAuthorityDescriptionArray() fixed mb,
ref     domain  tctvat           oTaxTypeArray(),
ref     domain  tcmcs.clcm       oCalculationMethodArray(),
ref     domain  tcyesno          oExpensePurchaseTaxArray(),
ref     domain  tctax.payt       oPayTaxArray(),
ref     domain  tccom.bpid       oCollectionOfficeArray() fixed,
ref     domain  tccdis           oTaxArticleArray() fixed,
ref     domain  tcfovn           oExemptCertificateArray() fixed,
ref     domain  tccdis           oExemptReasonArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function gets the internal tax result attributes of
the given XML node in which the results of the tax
calculation are stored.
Pre:    None
Post:   None
Input
iTaxCalcResultsNode             - Tax Calc Results Node:Mandatory
oNumberOfTaxLines               - Number Of Tax Lines
oLineTaxCodeArray               - Line Tax Code (array)
oTaxableAmountArray             - Taxable Amount (array)
oExemptAmountArray              - Exempt Amount (array)
oExemptArray                    - Exempt (array)
oTaxAmountArray                 - Tax Amount (array)
oShiftedTaxAmountArray          - Shifted Tax Amount (array)
oClaimableTaxAmountArray        - Claimable Tax Amount (array)
oNonClaimableTaxAmountArray     - Non Claimable Tax Amount (array)
oTaxPercentageArray             - Tax Percentage (array)
oTaxAuthorityArray              - Tax Authority (array)
oTaxAuthorityDescriptionArray   - Tax Authority Description (array)
oTaxTypeArray                   - Tax Type (array)
oCalculationMethodArray         - Calculation Method (array)
oExpensePurchaseTaxArray        - Expense Purchase Tax (array)
oPayTaxArray                    - Pay Tax (array)
oCollectionOfficeArray          - Collection Office (array)
oTaxArticleArray                - Tax Article (array)
oExemptCertificateArray         - Exempt Certificate (array)
oExemptReasonArray              - Exempt Reason (array)
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
