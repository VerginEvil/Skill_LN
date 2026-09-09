# ReceiptLine.Reverse

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1256-1256

```baan
DLL:   whextinhapi
This function is available from 2025.07 (KB3561538).
Syntax: long ReceiptLine.Reverse(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  whhuid           iHandlingUnit,
domain  whloca           iAdjustLocation,
boolean          iSetPackingSlipQuantityToZero,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will reverse the given receipt line.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iReceipt                - Mandatory
iReceiptLine            - Mandatory
iHandlingUnit           - Optional, unless handling units are
linked to the receipt line.
iAdjustLocation         - Optional, value is ignored when
iHandlingUnit is filled.
When warehouse and item of receipt
line are location controlled, then
this field becomes mandatory when
iHandlingUnit is not filled.
iSetPackingSlipQuantityToZero - Mandatory
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
