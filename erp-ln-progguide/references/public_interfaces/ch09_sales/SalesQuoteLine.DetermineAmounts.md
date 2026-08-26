# SalesQuoteLine.DetermineAmounts

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesQuoteLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 295-296

```baan
DLL:   tdextslsapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long SalesQuoteLine.DetermineAmounts(
domain  tcqono           iSalesQuote,
domain  tcpono           iSalesQuoteLine,
domain  tcpono           iSalesQuoteLineAlternative,
ref     domain  tcamnt           oNetLineAmount,
ref     domain  tcamnt           oLineDiscountAmount,
ref     domain  tcamnt           oOrderDiscountAmount,
ref     domain  tcdisc           oStructureDiscountPercentage,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function determines the Net Line Amount, Line Discount
Amount, Order Discount Amount and the Structure Discount
Percentage for the given Sales Quote Line.
The calculated amounts are expressed in the currency of the
Sales Quote.
Pre:    None
Post:   None
Input:  iSalesQuote                           - Sales Quote (Mandatory)
iSalesQuoteLine                               - Sales Quote Line (Mandatory)
iSalesQuoteLineAlternative
-                                               Sales Quote Line Alternative
(Optional)
Output: oNetLineAmount                        - Net amount of the Quote Line, i.e.
the Line amount minus the total Line
Discount amount.
oLineDiscountAmount                           - The total Line Discount amount
oOrderDiscountAmount                          - The Order Discount amount
This amount is calculated by applying
the Order Discount of the Quote to
the calculated net Line amount.
oStructureDiscountPercentage
-                                               The Structure Discount Percentage
This is the Discount Percentage of
the Quote Line that is based on
the total of line discount that
is not manually specified.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     -> No error
<> 0                          -> Error occurred
```
