# PurchaseOrderLine.Approve

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 452-453

```baan
DLL:   tdextpurapi
This function is available from     2021.12 (KB2218711  ).
Syntax: long PurchaseOrderLine.Approve(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function can be used to approve the given purchase order
line. Note that approval is not allowed on line level for the
scenarios below:
* If Workflow is active for purchase orders
* If Change Requests are required
Note:
This function does not start the execution of automatic
order steps. A separate Public Interface can be used to
start automatic order steps if necessary:
'PurchaseOrder.StartAutomaticProcessing'
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder          Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iSequence               Purchase Order Line Sequence.
(must be >= 0).
If 0 is passed, then this will approve
all sequences for the given order line
that require approval.
Otherwise, only the given sequence is
approved.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The order line is approved
<> 0                    An error occurred
```
