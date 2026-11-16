# ReceiptLine.Confirm

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1246-1247

```baan
DLL:   whextinhapi
This function is available from 2021.08 (KB2196655).
Syntax: long ReceiptLine.Confirm(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
ref             boolean          oReceiptLinesConfirmed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will confirm the given Receipt Line.
When zero iReceiptLine is passed all receipt lines of iReceipt
will be confirmed.
When handling units are linked to the receipt line all
handling units will be confirmed automatically.
When successful, also the automatic inbound process is started
for this receipt line.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iReceipt                - Mandatory
iReceiptLine            - Optional
0 means that all receipt lines will be confirmed.
Output: oReceiptLinesConfirmed  - One ore more Receipt Lines are
confirmed
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
