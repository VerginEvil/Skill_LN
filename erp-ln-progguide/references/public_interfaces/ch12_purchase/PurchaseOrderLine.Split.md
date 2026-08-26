# PurchaseOrderLine.Split

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 464-465

```baan
DLL:   tdextpurapi
This function is available from     2024.01 (KB2312115  ).
Syntax: long PurchaseOrderLine.Split(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcqrd1           iQuantityForNewDetail,
domain  tcdate           iPlannedReceiptDateForNewDetail,
domain  tccdis           iPegChangeReason,
domain  tcyesno          iKeepConfirmedReceiptDates,
domain  tcyesno          iApproveAndProcessChangeRequestAutomatically,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the split purchase order line or detail
process for a public interface. It performs similar
functionality as splitting order lines / details in the purchase
order line / details sessions.
Note:
1. In case change requests are applicable and required, a CR is
initiated to perform the split action. An option is provided
to automatically approve/process the change request to the
order (it performs a straightforward approve; no
recalculations etc.). The change request will have origin
'Manual'.
2. This function does not trigger any automatic processing
afterwards, if applicable.
3. This function does not update the planning pegging data.
Regular planning run will update this.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder          Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iOrderLineSequence      Purchase Order Line Sequence (Mandatory)
iQuantityForNewDetail   The quantity that will be used for the
new detail line (Mandatory)
iPlannedReceiptDateForNewDetail                       -
The planned receipt date that will be
used for the new detail line (Mandatory)
iPegChangeReason        The Peg Change Reason that will be stored
in the Peg Audit History.
(Mandatory if parameter 'Audit Manual
Project Peg Modifications' is set to Yes
in Project Pegging Parameters.)
iKeepConfirmedReceiptDates
Yes: Indicates that the Confirmed Receipt
Dates of the given purchase order
line will also be used on the new
detail line.
No:  Confirmed Receipt Dates will be
cleared on the new detail line.
iApproveAndProcessChangeRequestAutomatically
Yes: If a change request was created,
then it will be approved and
processed automatically.
No:  If a change request was created,
then it will NOT be approved and
processed automatically.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The order line has been split.
<> 0                    An error occurred
```
