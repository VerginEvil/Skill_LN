# ReceiptLine.RemoveHandlingUnits

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1245-1246

```baan
DLL:   whextinhapi
This function is available from     2026.05 (KB3660940  ).
Syntax: long ReceiptLine.RemoveHandlingUnits(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface can be used to remove handling units
from the specified receipt line.
This function removes the handling units from the receipt line
and closes the handling unit. If the handling unit is part of
a structure, all child handling units will also be removed.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iReceipt                              - Mandatory. Receipt number.
iReceiptLine                                  - Mandatory. Receipt line number.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
