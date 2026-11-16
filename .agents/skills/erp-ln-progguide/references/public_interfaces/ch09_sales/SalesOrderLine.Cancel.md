# SalesOrderLine.Cancel

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 339-341

```baan
DLL:   tdextslsapi
This function is available from 2020.07 (KB2129097).
Syntax: long SalesOrderLine.Cancel(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcmcs.str2       iSalesOrderLineAcknowledgement,
domain  tcmcs.str8       iSalesOrderLineChangeOrderSequence,
domain  tccdis           iSalesOrderLineChangeReason,
domain  tccdis           iSalesOrderLineChangeType,
domain  tcmcs.str2       iPurchaseOrderAcknowledgement,
domain  tcmcs.str8       iPurchaseOrderChangeOrderSequence,
domain  tccdis           iPurchaseOrderChangeReason,
domain  tccdis           iPurchaseOrderChangeType,
domain  tcmcs.str2       iPurchaseOrderLineAcknowledgement,
domain  tcmcs.str8       iPurchaseOrderLineChangeOrderSequence,
domain  tccdis           iPurchaseOrderLineChangeReason,
domain  tccdis           iPruchaseOrderLineChangeType,
domain  tcyesno          iCancelCrossDockOrderLine,
boolean          iCheckCrossDockOrderLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function cancels a sales order line. The input sales order
line can be an order line of type:
- Total (sequence number must be 0)
- Detail
- Backorder
If the given sales order line is of type 'Total', then all
linked order lines are canceled as well.
If the given sales order line is of type 'Detail' or 'Backorder',
then the related Total-line will be be synchronized. If no
detail-lines are open anymore, then the Total-line will be
canceled as well.
Depending on the situation, a purchase order line that is linked
to the given sales order line may be canceled as well.
If it's Direct Delivery, then the purchase order line will be canceled.
If it's Cross Docking, then it depends on the argument
'iCancelCrossDockOrderLine'.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales Order (Mandatory)
iSalesOrderLine         - Sales Order Line (Mandatory)
iSalesOrderSequence     - Sales Sequence number ( must be >= 0)
iSalesOrderLineAcknowledgement
- Acknowledgement code
iSalesOrderLineChangeOrderSequence
- Change Order Sequence Number
iSalesOrderLineChangeReason
- Change Reason Code
(Mandatory if 'Change Codes Mandatory'
is set to Yes in the Sales Order Parameters
or Sales Order Settings by Office)
iSalesOrderLineChangeType
- Change Type
(Mandatory if 'Change Codes Mandatory'
is set to Yes in the Sales Order Parameters
or Sales Order Settings by Office)
iPurchaseOrderAcknowledgement
- Acknowledgement code purchase order
header
iPurchaseOrderChangeOrderSequence
- Change Order Sequence Number purchase
order header
iPurchaseOrderChangeReason
- Change Reason purchase order header
iPurchaseOrderChangeType
- Change Type purchase order header
iPurchaseOrderLineAcknowledgement
- Acknowledgement code purchase order
line
iPurchaseOrderLineChangeOrderSequence
- Change Order Sequence purchase order line
iPurchaseOrderLineChangeReason
- Change Reason purchase order line
(Mandatory if 'Change Codes Mandatory'
is set to Yes in the Purchase Order Parameters
or Purchase Order Settings by Office)
iPruchaseOrderLineChangeType
- Change Type purchase order line
(Mandatory if 'Change Codes Mandatory'
is set to Yes in the Purchase Order Parameters
or Purchase Order Settings by Office)
iCancelCrossDockOrderLine - Yes: If a purchase order line is
linked to the given order line
using cross-docking, then it
will be canceled as well.
No:  The linked cross-dock purchase
order line (if any) is not
canceled.
iCheckCrossDockOrderLine - True:
If a purchase order is linked
to the given order line using
cross-docking, then it is not
allowed to cancel the given
sales order line. The process
is aborted in that case.
False:
The sales order line is allowed
to be canceled if it is linked
to a cross-dock purchase order
line.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Cancellation was successful
<> 0                    An error occurred
```
