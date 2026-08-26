# PurchaseOrderLine.ConfirmPotentialBackorder

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 457-458

```baan
DLL:   tdextpurapi
This function is available from     2025.01 (KB3546270  ).
Syntax: long PurchaseOrderLine.ConfirmPotentialBackorder(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iPurchaseOrderLine,
domain  tcpono           iPurchaseOrderLineSequence,
domain  tcqrd1           iBackorderQuantityToBeConfirmed,
domain  tccuni           iBackorderUnit,
domain  tcdate           iBackorderPlannedReceiptDate,
domain  tctxtn           iNotesTextNumber,
domain  tccdis           iPegChangeReason,
domain  tcyesno          iApproveAndProcessChangeRequestAutomatically,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to confirm a Potential Backorder
after a final Partial Receipt has been done. A new Purchase
Backorder Line will be created.
First the Purchase Backorder Data will be changed based on the input
values if needed; then the Potential Backorder will be confirmed.
This all is only possible if allowed; otherwise an error message is
returned.
If Peg Distribution is used on the purchase order line and
constraint planning is implemented, then normally pegging relations
will be updated in the next planning run; but not in this interface,
because it has its own transaction logic. If there is a need for
this, it must be met in another way.
When the Potential Backorder has been confirmed successfully
automatically processing of orders can be done afterwards with the
Public Interface PurchaseOrder.StartAutomaticProcessing() if needed.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder                                - Purchase Order (mandatory)
iPurchaseOrderLine                                    - Purchase Order Line (mandatory)
iPurchaseOrderLineSequence                            - Purchase Order Line Sequence (mandatory)
iBackorderQuantityToBeConfirmed                       - Backorder Quantity to be confirmed
(Quantity in Backorder Unit;
if given value is zero no new
receipt can be done anymore)
iBackorderUnit                                        - Backorder Unit
(if given value is 'empty'
default system value is used)
iBackorderPlannedReceiptDate                          - Backorder Planned Receipt Date
(if given value is zero
default system value is used)
iNotesTextNumber                                      - Notes that are related to the
specific backorder line
(if given Text Number is zero
default system value is used)
iPegChangeReason                                      - The Peg Change Reason that will be
stored in the Peg Audit History.
Mandatory if parameter 'Audit Manual
Project Peg Modifications' is ON.
iApproveAndProcessChangeRequestAutomatically                          -
Yes: If Change Requests are applicable the created change
request will be approved and processed automatically.
No: Approval and processing of the change request
(if any) is not done automatically.
Output: oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                          - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                             - Potential Backorder is confirmed
<> 0                                                  - An error occurred
```
