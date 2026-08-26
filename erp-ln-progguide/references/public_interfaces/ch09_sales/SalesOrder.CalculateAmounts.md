# SalesOrder.CalculateAmounts

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 312-314

```baan
DLL:   tdextslsapi
This function is available from     2023.09 (KB2300531  ).
Syntax: long SalesOrder.CalculateAmounts(
domain  tcorno           iSalesOrder,
boolean          iIncludeCostLines,
boolean          iCalculateInvoiceAmounts,
boolean          iCalculateCostOfSales,
boolean          iCalculateTaxAmount,
ref     domain  tcamnt           oGrossAmount,
ref     domain  tcamnt           oNetAmount,
ref     domain  tcamnt           oDiscountAmount,
ref     domain  tcamnt           oInvoiceRequiredAmount,
ref     domain  tcamnt           oInvoicedAmount,
ref     domain  tccoam           oCompanyOwnedCostOfSales,
ref     domain  tccoam           oCustomerOwnedCostOfSales,
ref     domain  tcamnt           oTaxAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates and returns several sales order
amounts. The returned order amounts are expressed in
the order currency.
Pre:    Not applicable
Post:   Not applicable
Input:  iSalesOrder                                   - The Sales Order. Mandatory.
iIncludeCostLines                                     - True/False
Indicates whether additional
cost lines will be included
in the calculation.
iCalculateInvoiceAmounts                              - True/False
Indicates whether invoice
amounts will be calculated
and returned.
iCalculateCostOfSales                                 - True/False
Indicates whether cost of
sales will be calculated and
returned.
iCalculateTaxAmount                                   - True/False
Indicates whether tax amounts
will be calculated and
returned.
Output: oGrossAmount                                  - Gross amount
oNetAmount                                            - Amount minus all line
and header discounts
(promotions included in
calculation)
oDiscountAmount                                       - Header discount amount
(promotions included in
calculation)
oInvoiceRequiredAmount                                - Amount released to
Invoicing
oInvoicedAmount                                       - Invoiced amount
oCompanyOwnedCostOfSales                              - Company owned cost of sales
oCustomerOwnedCostOfSales                             - Customer owned cost of sales
oTaxAmount                                            - Tax amount
oExceptionMessage                                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - Amounts were successfull
calculated and returned.
DALHOOKERROR                                          - An error occurred
```
