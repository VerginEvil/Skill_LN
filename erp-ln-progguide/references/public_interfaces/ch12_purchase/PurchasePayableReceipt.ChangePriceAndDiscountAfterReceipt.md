# PurchasePayableReceipt.ChangePriceAndDiscountAfterReceipt

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchasePayableReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 472-474

```baan
DLL:   tdextpurapi
This function is available from 2020.12 (KB2161926).
Syntax: long PurchasePayableReceipt.ChangePriceAndDiscountAfterReceipt(
long             iObjectType,
domain  tcorno           iPurchaseOrderOrSchedule,
domain  tcpono           iLine,
domain  tcpono           iLineSequence,
domain  tcpono           iReceiptSequence,
domain  tcpsno           iPayableReceiptSequence,
boolean          iAllowPriceChangeInvoicedLines,
domain  tcyesno          iApplyPriceAndDiscountsToOtherPayableReceipts,
domain  tcyesno          iApplyPriceStageToOtherPayableReceipts,
domain  tcyesno          iUpdatePriceInItemPurchase,
domain  tcyesno          iUpdatePriceInItemPurchaseBySite,
domain  tcyesno          iApproveAndProcessChangeRequestAutomatically,
domain  tcpric           iPrice,
domain  tcprsg           iPriceStage,
const   domain  tcdisc           iDiscountPercentage(),
const   domain  tddiam           iDiscountAmount(),
const   domain  tddmth           iDiscountMethod(),
const   domain  tccdsc           iDiscountCode() fixed,
domain  tcamnt           iPayableAmount,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Function can be used to change the Price and Discounts after
Receipt. The change is done for the Purchase Payable Receipts.
If ION Workflow Document Approval is used, then the following
applies:
* if the Order is waiting for Approval in
ION, then updating is not allowed.
Payable receipt lines are only updated if the invoicing
status is free.
Price changes must be possible (meaning that e.g. price is not
read-only (yet))
When a contract is linked and prices and/or discounts are
changed the contract will be unlinked depending on the
'Always Use Contract Price and Discount' setting.
By default, changes are not done when the Invoice number on the
Payable Receipt is already filled. Setting
iAllowPriceChangeInvoicedLines can overrule this.
By setting iApplyPriceAndDiscountsToOtherPayableReceipts it
is possible to apply the Price and Discount changes also to the
other Payable Receipt of the same Line / Line Sequence.
By setting iApplyPriceStageToOtherPayableReceipts it is
possible to apply the Price Stage changes also to the
other Payable Receipt of the same Line / Line Sequence.
By setting iUpdatePriceInItemPurchase it is possible to
update the Purchase Price in Item Purchase.
By setting iUpdatePriceInItemPurchaseBySite it is
possible to update the Purchase Price in Item Purchase by Site.
The Purchase Price is updated for the Site of the given Object.
If Change Requests are applicable for the given Purchase
Order, then the following applies:
* A change request will be created for the status change.
* Depending on the input argument
'iApproveAndProcessChangeRequestAutomatically',
Approving and Processing of the Change Request will be
done automatically or not.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iObjectType                     - Object Type;
Possible values:
1: Purchase Order
2: Purchase Schedule;
(Mandatory)
iPurchaseOrderOrSchedule        - Purchase Order or
Schedule Number;
(Mandatory)
iLine                           - Order or Schedule Line;
(Mandatory)
iLineSequence                   - Line Sequence
iReceiptSequence                - Receipt Sequence
iPayableReceiptSequence         - Payable Receipt Sequence;
(Mandatory)
iAllowPriceChangeInvoicedLines  - True: Allow price changes on
invoiced lines.
False: Price changes are not
not allowed on invoiced lines. Line will be skipped.
iApplyPriceAndDiscountsToOtherPayableReceipts   -
Yes: Other Payable Receipt of the same
Line / Line Sequence will be updated with
Price and Discounts.
No: Other Payable Receipt of the same
Line / Line Sequence will not be updated.
iApplyPriceStageToOtherPayableReceipts  -
Yes: Other Payable Receipt of the same
Line / Line Sequence will be updated with
Price Stage.
No: Other Payable Receipt of the same
Line / Line Sequence will not be updated.
iUpdatePriceInItemPurchase      -
Yes: Price in Item Purchase will be updated.
No: Price is not updated
iUpdatePriceInItemPurchaseBySite        -
Yes: Price in Item Purchase by Site will be updated.
No: Price is not updated
iApproveAndProcessChangeRequestAutomatically    -
Yes: The created change request will be approved and
processed automatically.
No: Approval and processing of the change request
(if any) are not done automatically.
iPrice                          - Price
(In order Currency)
iPriceStage                     - Price Stage
iDiscountPercentage             - Discount Percentage;
Array of 11 elements
iDiscountAmount                 - Discount Amount;
Array of 11 elements
(In order Currency)
iDiscountMethod                 - Discount Method;
Array of 11 elements
iDiscountCode                   - Discount Code;
Array of 11 elements
iPayableAmount                  - Payable Amount;
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Price and Discounts are updated.
<> 0                    - An error occurred
```
