# SalesOrderInvoiceLine.ChangePriceAndDiscounts

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderInvoiceLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 364-365

```baan
DLL:   tdextslsapi
This function is available from     2024.09 (KB3518728  ).
Syntax: long SalesOrderInvoiceLine.ChangePriceAndDiscounts(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcpono           iActualDeliveryLineSequence,
domain  tcpono           iInvoiceLine,
domain  tcyesno          iApplyPriceAndDiscountsToOtherInvoiceLines,
domain  tcyesno
iApplyPriceStageToOtherInvoiceLinesForInstallments,
domain  tcyesno
iUnlinkContractIfAlwaysUseContractPriceAndDiscount,
domain  tcyesno          iUpdatePriceInItemSales,
domain  tcyesno          iUpdatePriceInItemSalesByOffice,
domain  tcyesno          iApproveAndProcessChangeRequestAutomatically,
domain  tcpric           iPrice,
domain  tcprsg           iPriceStage,
const   domain  tcdisc           iDiscountPercentage(),
const   domain  tddiam           iDiscountAmount(),
const   domain  tddmth           iDiscountMethod(),
const   domain  tccdsc           iDiscountCode() fixed,
domain  tcamnt           iInvoiceAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to change the Price and Discounts after
Delivery has taken place. The change is done for the Sales Order
Invoice Lines.
If ION Workflow Document Approval is used and the Order is
waiting for Approval in ION, updating is not allowed.
Invoice lines are only updated if they have not yet been processed
too far in Invoicing. Price changes must be possible (meaning that
e.g. price is not read                      -only (yet)).
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                                           - Sales Order (mandatory)
iSalesOrderLine                                               - Sales Order Line (mandatory)
iSalesOrderLineSequence                                       - Sales Order Line Sequence Number
iActualDeliveryLineSequence                                   - Actual Delivery Line Sequence
Number (mandatory)
iInvoiceLine                                                  - Invoice Line
iApplyPriceAndDiscountsToOtherInvoiceLines                            -
Yes: Other Invoice Lines of the same Sales Order Line
will be updated with Price and Discounts.
No: Other Invoice Lines of the same Sales Order Line
will not be updated.
iApplyPriceStageToOtherInvoiceLinesForInstallments                            -
Yes: Other Invoice Lines of the same Sales Order will be
updated with Price Stage if 'Invoicing by
Installments' applies to the Sales Order.
No: No Invoice Lines of the Sales Order will be updated
with the Price Stage.
iUnlinkContractIfAlwaysUseContractPriceAndDiscount                       -
Yes: When a Contract is linked and Price and/or Discounts
are changed the Contract will be unlinked if
'Always Use Contract Price and Discount' applies
to the Sales Order Invoice Line.
No: Contract for Invoice Line is not unlinked if 'Always
Use Contract Price and Discount' applies to the
Sales Order Invoice Line. The Price and Discounts
will not be changed.
iUpdatePriceInItemSales                       -
Yes: Price in Item Sales will be updated.
No: Price is not updated
iUpdatePriceInItemSalesByOffice                       -
Yes: Price in Item Sales by Office will be updated.
No: Price is not updated
iApproveAndProcessChangeRequestAutomatically                          -
Yes: If Change Requests are applicable the created change
request will be approved and processed automatically.
No: Approval and processing of the change request
(if any) is not done automatically.
iPrice                                                - Price
(In order currency)
iPriceStage                                           - Price Stage
iDiscountPercentage                                   - Discount Percentage;
Array of 11 elements
iDiscountAmount                                       - Discount Amount;
Array of 11 elements
(In order currency)
iDiscountMethod                                       - Discount Method;
Array of 11 elements
iDiscountCode                                         - Discount Code;
Array of 11 elements
iInvoiceAmount                                        - Invoice Amount
(In order currency)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Price and Discounts are updated.
<> 0                                          - An error occurred
```
