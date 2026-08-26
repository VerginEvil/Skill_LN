# PurchaseOrderLine.Cancel

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 454-457

```baan
DLL:   tdextpurapi
This function is available from     2022.06 (KB2225144  ).
Syntax: long PurchaseOrderLine.Cancel(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tdpur.corg       iOriginForChangeRequest,
domain  tcmcs.str2       iOrderHeaderAcknowledgementCode,
domain  tcmcs.str8       iOrderHeaderChangeOrderSequence,
domain  tccdis           iOrderHeaderChangeReason,
domain  tccdis           iOrderChangeType,
domain  tcmcs.str2       iOrderLineAcknowledgementCode,
domain  tcmcs.str8       iOrderLineChangeOrderSequence,
domain  tccdis           iOrderLineChangeReason,
domain  tccdis           iOrderLineChangeType,
domain  tcmcs.str2       iSalesOrderLineAcknowledgementCode,
domain  tcmcs.str8       iSalesOrderLineChangeOrderSequence,
domain  tccdis           iSalesOrderLineChangeReason,
domain  tccdis           iSalesOrderLineChangeType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to cancel the given purchase order
line(s). It can be used to cancel all order lines, or only a
subset.
If there are subcontracting supply orders linked to an order
line, these supply orders are also cancelled or deleted.
Note:
This function does not start the execution of automatic
order steps. A separate Public Interface can be used to
start automatic order steps if necessary:
'PurchaseOrder.StartAutomaticProcessing'
In some cases, this may be needed:
-                           If a production order is linked to the cancelled (back)
order line, then there can still be inventory waiting to
be transferred from the warehouse to the shopfloor.
When the backorder is cancelled this transfer order still
needs to get an update.
-                           For order lines that are invoiced by stage payments it is
possible that variance transactions are written after
cancellation of an order line (last open detail/backorder
line). In that case the variances must be processed
automatically after the commit of the transaction, which
can be achieved by calling Public Interface
'PurchaseOrder.StartAutomaticProcessing'.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder  Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Optional)
If 0 is passed, then this will cancel
all order lines for the given order.
Otherwise, only the given order line is
cancelled.
iOrderLineSequence      Purchase Order Line Sequence (Optional)
If 0 is passed, then this will cancel
all sequences for the given order line.
Otherwise, only the given sequence is
cancelled.
iOriginForChangeRequest Origin for Change Request (Mandatory)
If modifications to the given purchase
order require a change request to be
created, then the given origin will be
used to create it.
iOrderHeaderAcknowledgementCode
Acknowledgement code purchase order header
iOrderHeaderChangeOrderSequence
Change sequence purchase order header
iOrderHeaderChangeReason
Change reason purchase order header
(Optional).
iOrderChangeType        Change type purchase order header
(Optional).
iOrderLineAcknowledgementCode (Optional)
Acknowledgement code purchase order line
iOrderLineChangeOrderSequence (Optional)
Change sequence purchase order line
iOrderLineChangeReason  (Mandatory if 'Change Codes Mandatory'
is set to Yes in the Purchase Order
Parameters or Purchase Order Settings
by Office and no default is set).
Change reason purchase order line
iOrderLineChangeType    (Mandatory if 'Change Codes Mandatory'
is set to Yes in the Purchase Order
Parameters or Purchase Order Settings
by Office and no default is set).
Change type purchase order line
iSalesOrderLineAcknowledgementCode (Optional)
Acknowledgement code sales order line.
If there are subcontracting supply
orders linked to an order line, then
these are cancelled as well. If the
supply order is a sales order line, then
this acknowledgement code will be used
to cancel it.
iSalesOrderLineChangeOrderSequence (Optional)
Change sequence sales order line.
If there are subcontracting supply
orders linked to an order line, then
these are cancelled as well. If the
supply order is a sales order line, then
this change order sequence will be used
to cancel it.
iSalesOrderLineChangeReason
(Mandatory if 'Change Codes Mandatory'
is set to Yes in the Sales Order Parameters
or Sales Order Settings by Office).
Change reason sales order line.
If there are subcontracting supply
orders linked to an order line, then
these are cancelled as well. If the
supply order is a sales order line, then
this change reason will be used
to cancel it.
iSalesOrderLineChangeType
(Mandatory if 'Change Codes Mandatory'
is set to Yes in the Sales Order Parameters
or Sales Order Settings by Office).
Change type sales order line.
If there are subcontracting supply
orders linked to an order line, then
these are cancelled as well. If the
supply order is a sales order line, then
this change type will be used
to cancel it.
Output: oExceptionMessage       The last message. This can also be filled
if the return value equals 0.
If more than one  message is given,
these are present in the oExceptionID
oExceptionID            An ID that refers to all error
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The order line(s) is/are cancelled.
<> 0                    An error occurred
```
