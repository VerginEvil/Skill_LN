# SupplierStagePaymentLines.StartDetail

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for SupplierStagePaymentLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 481-483

```baan
DLL:   tdextpurapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long SupplierStagePaymentLines.StartDetail(
long             iStartMode,
domain  tdssp.boty       iBusinessObjectType,
domain  tcqono           iRequestForQuote,
domain  tcpono           iRequestForQuoteLine,
domain  tcpono           iRequestForQuoteResponseSequence,
domain  tccom.bpid       iRequestForQuoteBidder,
domain  tcorno           iPurchaseOrder,
domain  tcpono           iPurchaseOrderLine,
domain  tcpono           iStagePaymentLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Supplier Stage Payments
Details (tdpur5120m000).
This session can be started for three different contexts:
-                       Request for Quote (RFQ) Response
To use this context set iBusinessObjectType to value
tdssp.boty.tdpur106 and specify the fields:
iRequestForQuote
iRequestForQuoteLine
iRequestForQuoteResponseSequence
iRequestForQuoteBidder
-                       Purchase Order Line
To use this context set iBusinessObjectType to value
tdssp.boty.tdpur401 and specify the fields:
iPurchaseOrder
iPurchaseOrderLine
-                       Purchase Order
To use this context set iBusinessObjectType to value
tdssp.boty.tdpur400 and specify the fields:
iPurchaseOrder
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS        Parent and child are parallel
sessions that can be manipulated
simultaneously.
iBusinessObjectType     Business Object Type (Mandatory).
Possible values are:
tdssp.boty.tdpur106
Use when the context is RFQ Response.
tdssp.boty.tdpur401
Use when the context is Purchase Order
Line.
tdssp.boty.tdpur400
Use when the context is Purchase Order.
iRequestForQuote        Request for Quote (Mandatory when
iBusinessObjectType is set to
tdssp.boty.tdpur106).
iRequestForQuoteLine    Request for Quote Line (Mandatory
when iBusinessObjectType is set to
tdssp.boty.tdpur106).
iRequestForQuoteResponseSequence
Request for Quote Response Sequence
(Optional).
iRequestForQuoteBidder  Request for Quote Bidder (Mandatory
when iBusinessObjectType is set to
tdssp.boty.tdpur106).
iPurchaseOrder          Purchase Order (Mandatory when
iBusinessObjectType is set to
tdssp.boty.tdpur401 or
tdssp.boty.tdpur400).
iPurchaseOrderLine      Purchase Order Position (Mandatory when
iBusinessObjectType is set to
tdssp.boty.tdpur401).
iStagePaymentLine       Stage Payment Line (Mandatory)
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
