# PurchaseInvoice.StartMultiMain

> Chapter: Chapter 38 Public Interfaces for Accounts Payable
>
> Group: Public Interfaces for PurchaseInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1799-1801

```baan
DLL:   tfextacpapi
This function is available from     2025.11 (KB3632925  ).
Syntax: long PurchaseInvoice.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tfgld.ttyp       iTransactionType,
domain  tfgld.docn       iDocument,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts MMT session Purchace Invoice Inquiry
(tfacp2600m100).
Pre:    na
Post:   na
Input:  iStartMode                            - Start Mode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:""
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a iStartFilter
the session index will match the value of this variable.
No Session Index available for tfacp2600m100.
iQueryExtend
A specific query to be used when zooming to this session.
iTransactionType                              - Transaction Type
iDocument                                     - Invoice number
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - succes
<> 0                      otherwise
```

## Chapter 39 Public Interfaces for Accounts

## Receivable

## Public Interfaces for AccountsReceivable

The following functions are available: AccountsReceivable.DetermineDueDate AccountsReceivable.StartOverview
