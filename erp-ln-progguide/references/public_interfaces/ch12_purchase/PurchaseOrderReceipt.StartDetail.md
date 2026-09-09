# PurchaseOrderReceipt.StartDetail

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 471-472

```baan
DLL:   tdextpurapi
This function is available from 2022.06 (KB2233502).
Syntax: long PurchaseOrderReceipt.StartDetail(
long             iStartMode,
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcpono           iReceiptSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Purchase Receipts
(tdpur4106m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
MODAL+START.WITH.ADD.SET -
Session is started in Add-mode, so a new
receipt can be entered directly.
The parent session is blocked until the
child session exits.
MODELESS+START.WITH.ADD.SET -
Session is started in Add-mode, so a new
receipt can be entered directly.
Parent and child are parallel sessions
that can be manipulated simultaneously.
iPurchaseOrder          Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iOrderLineSequence      Purchase Sequence number
Note that the given purchase order line
must exist.
iReceiptSequence        Purchase Order Line Receipt Sequence
Unless the session is started in Add-mode,
the given receipt-sequence is mandatory
and must exist.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
