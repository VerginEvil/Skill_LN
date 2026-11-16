# PurchaseOrders.StartOverview

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 453-454

```baan
DLL:   tdextpurapi
This function is available from 2024.06 (KB3501666).
Syntax: long PurchaseOrders.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcorno           iOrder,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcrefc           iBuyFromBusinessPartnerOrder mb,
domain  tccwoc           iPurchaseOffice,
domain  tcemno           iBuyer,
ref     domain  tcorno           oOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Overview session Purchase Orders
(tdpur4100m000).
Input:  iStartMode              Specifies the start mode for the session
(Mandatory).
Possible values are:
MODAL           The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS        Parent and child are parallel sessions
that can be manipulated simultaneously.
iStartFilter            Start filter (Not used).
iSessionIndex           Session index
Possible values are:
1               Purchase Order (default)
2               Buy-from Business Partner
3               Buy-from Business Partner Order
4               Buyer
5               Purchase Office
iQueryExtend            A specific query to be used when zooming
to this session (Optional).
iOrder                  Purchase Order (Optional).
iBuyFromBusinessPartner Buy-from Business Partner (Mandatory if
iStartMode is MODELESS and iSessionIndex
is 2).
iBuyFromBusinessPartnerOrder
Buy-from Business Partner Order (Optional).
iPurchaseOffice         Purchase Office (Mandatory if iStartMode
is MODELESS and iSessionIndex is 4).
iBuyer                  Buyer (Optional).
Output:
For iStartMode MODAL:
oOrder          Selected Order number
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
