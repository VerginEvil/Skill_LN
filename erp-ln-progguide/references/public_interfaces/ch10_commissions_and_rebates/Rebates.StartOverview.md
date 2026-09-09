# Rebates.StartOverview

> Chapter: Chapter 10 Public Interfaces for Commissions and Rebates
>
> Group: Public Interfaces for Rebate
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 389-390

```baan
DLL:   tdextcmsapi
This function is available from 2022.12 (KB2262331).
Syntax: long Rebates.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderSequence,
domain  tcpono           iActualDeliverySequence,
domain  tcpono           iInvoiceLine,
domain  tccom.bpid       iRelation,
domain  tcpono           iSerialNumber,
ref     domain  tcorno           oSalesOrder,
ref     domain  tcpono           oSalesOrderLine,
ref     domain  tcpono           oSalesOrderSequence,
ref     domain  tcpono           oActualDeliverySequence,
ref     domain  tcpono           oInvoiceLine,
ref     domain  tccom.bpid       oRelation,
ref     domain  tcpono           oSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Rebates Overview
(tdcms2550m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iSessionIndex           Specifies the table-index that will be
used.
iQueryExtend            A specific query to be used when zooming
to this session.
iSalesOrder             Sales Order.
Mandatory if iStartMode is MODELESS
and session index 1 is used.
iSalesOrderLine         Sales Order Line
Not mandatory
iSalesOrderSequence     Sales Order Sequence
Not mandatory
iActualDeliverySequence Actual Delivery Sequence
Not mandatory
iInvoiceLine            Invoice Line
Not mandatory
iRelation               Relation
Mandatory if iStartMode is MODELESS
and session index 2 is used.
iSerialNumber           Serial Number
Not mandatory
Output: for iStartMode MODAL:
oSalesOrder     The sales order of the selected record
oSalesOrderLine The sales order line of the selected record
oSalesOrderSequence
The sales order sequence of the selected
record
oActualDeliverySequence
The actual delivery sequence of the selected
record
oInvoiceLine    The invoice line of the selected
record
oRelation       The relation of the selected record
oSerialNumber   The serial number of the selected record
oExceptionMessage       The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```
