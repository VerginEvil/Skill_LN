# OutboundOrderLine.UndoCancel

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1234-1235

```baan
DLL:   whextinhapi
This function is available from     2023.10 (KB2308375  ).
Syntax: long OutboundOrderLine.UndoCancel(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will reset flag Cancel for an outbound order
line.
Pre:    db.retry.point
Post:   commit or abort transaction.
Input:  iOrderOrigin                          - Order Origin (Mandatory)
iOrderNumber                                  - Order Number (Mandatory)
iOrderLine                                    - Order Line (Optional)
iOrderSequence                                - Order Line Sequence (Optional)
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
