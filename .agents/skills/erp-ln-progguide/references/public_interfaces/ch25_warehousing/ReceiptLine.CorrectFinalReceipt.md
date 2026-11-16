# ReceiptLine.CorrectFinalReceipt

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1250-1250

```baan
DLL:   whextinhapi
This function is available from 2025.07 (KB3565746).
Syntax: long ReceiptLine.CorrectFinalReceipt(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  tcyesno          iFinalReceipt,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will correct the final receipt for the receipt
line.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iReceipt                - Mandatory
iReceiptLine            - Mandatory
iFinalReceipt           - Mandatory
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
