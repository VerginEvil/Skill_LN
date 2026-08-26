# PurchaseRequisition.StartMultiMain

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseRequisition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 417-418

```baan
DLL:   tdextpurapi
This function is available from     2026.05 (KB3657660  ).
Syntax: long PurchaseRequisition.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcrqno           iPurchaseRequisition,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi-Main session Purchase Requisition
(tdpur2600m000).
Input:  iStartMode              Specifies the start mode for the session
(mandatory).
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not used
iQueryExtend            A specific query to be used when zooming
to this session (optional).
iPurchaseRequisition    Purchase requisition (mandatory).
Output: oExceptionMessage       The last message if any message is
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
