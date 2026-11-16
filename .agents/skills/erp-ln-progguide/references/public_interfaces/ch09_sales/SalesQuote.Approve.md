# SalesQuote.Approve

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 289-290

```baan
DLL:   tdextslsapi
This function is available from 2024.08 (KB3515640).
Syntax: long SalesQuote.Approve(
domain  tcqono           iSalesQuote,
domain  tcgen.ynds       iRecalculatePricesAndDiscounts,
domain  tcgen.ynds       iRedetermineMaterialPriceInformation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to approve the input sales quote.
Function is using the same logic as the LN session 'Approve
Sales Quotations'(tdsls1102m000).
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesQuote                - Sales Quote (mandatory)
iRecalculatePricesAndDiscounts -
Recalculate Price and Discounts
before Sales Quote is approved
(mandatory)
No  - Do not recalculate
Yes - Recalculate
Use Default Settings - Consider
the parameter and/or sales
office setting 'Recalculate
Prices and Discounts'
iRedetermineMaterialPriceInformation -
Redetermine Material Price Information
before Sales Quote is approved
(mandatory)
No  - Do not redetermine
Yes - Redetermine
Use Default Settings - Consider
the parameter and/or sales
office setting 'Redetermine
Material Information in Sales'
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Approval was successful
<> 0                    - An error occurred
```
