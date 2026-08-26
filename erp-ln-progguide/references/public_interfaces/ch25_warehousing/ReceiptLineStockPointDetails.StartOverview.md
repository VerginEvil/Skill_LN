# ReceiptLineStockPointDetails.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLineStockPointDetail
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1253-1255

```baan
DLL:   whextinhapi
This function is available from     2023.10 (KB2304920  ).
Syntax: long ReceiptLineStockPointDetails.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  tcmcs.long       iDistributionSequence,
ref     domain  whinh.shpm       oReceipt,
ref     domain  tcpono           oReceiptLine,
ref     domain  tcmcs.long       oDistributionSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Receipt Line Stock
Point Details (whinh3123m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
Receipt
The Receipt to be started
Mandatory if iStartMode = MODELESS
iReceiptLine
The Receipt Line to be started
Mandatory if iStartMode = MODELESS
iDistributionSequence
Optional
Output: for iStartMode MODAL:
oReceipt                                      - selected receipt
oReceiptLine                                  - selected receipt line
oDistributionSequence                         - selected distribution sequence
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```

## Public Interfaces for StorageList

The following functions are available: StorageList.SplitAdvice StorageList.StartAutomaticInboundProcessing
