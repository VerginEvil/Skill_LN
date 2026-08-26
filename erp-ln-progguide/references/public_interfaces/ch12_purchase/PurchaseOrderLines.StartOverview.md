# PurchaseOrderLines.StartOverview

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 465-466

```baan
DLL:   tdextpurapi
This function is available from     2020.03 (KB2111387  ).
Syntax: long PurchaseOrderLines.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcitem           iItem,
domain  tcsite           iSite,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcdate           iCurrentPlannedReceiptDate,
ref     domain  tcorno           oOrder,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderLineSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Purchase Order Lines Overview
(tdpur4101m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           The session index that will be used.
iQueryExtend            A specific query to be used when zooming
to this session.
iOrder                  Order (Mandatory if iStartMode is MODELESS
and iSessionIndex is 1)
iOrderLine              Order Line
iOrderLineSequence      Order Line Sequence
iItem                   Item (Mandatory if iStartMode is MODELESS
and iSessionIndex is 2)
iSite                   Site
iBuyFromBusinessPartner Buy                      -from Business Partner (Mandatory if
iStartMode is MODELESS and iSessionIndex
is 3)
iCurrentPlannedReceiptDate
Current Planned Receipt Date
Output: for iStartMode MODAL:
oOrder          Order number of the selected order line
oOrderLine      Order Line of the selected order line
oOrderLineSequence
Sequence of the selected order line
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - An error occurred
```

## Public Interfaces for PurchaseOrderReceipt

The following functions are available: PurchaseOrderReceipt.Confirm PurchaseOrderReceipt.ConfirmV2 PurchaseOrderReceipt.StartDetail
