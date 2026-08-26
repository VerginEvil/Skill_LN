# PurchaseRequisitionLine.StartDetail

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseRequisitionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 422-423

```baan
DLL:   tdextpurapi
This function is available from     2023.04 (KB2286306  ).
Syntax: long PurchaseRequisitionLine.StartDetail(
long             iStartMode,
domain  tcrqno           iPurchaseRequisition,
domain  tcpono           iRequisitionLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the detail session Purchase Requisition Lines
(tdpur2502m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iPurchaseRequisition    Requisition; Mandatory
iRequisitionLine        Requisition Line; Mandatory
Note that the given purchase requisition
line must exist.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is.
given, these are present in the
oExceptionID
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```

## Public Interfaces for

## PurchaseRequisitionPrepareConversion

The following functions are available: PurchaseRequisitionPrepareConversion.StartMultiMain
