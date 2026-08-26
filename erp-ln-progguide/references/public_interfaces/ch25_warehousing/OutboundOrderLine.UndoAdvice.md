# OutboundOrderLine.UndoAdvice

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1234-1234

```baan
DLL:   whextinhapi
This function is available from     2025.12 (KB3613235  ).
Syntax: long OutboundOrderLine.UndoAdvice(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will remove the advice lines (for the given order
line) which have not been released yet.
This function has its own transaction management. It is not
allowed to call this inside a logical transaction.
When errors occur during the process the errors are visible
in the oExceptionID and the last message is present in
oExceptionMessage.
Pre:    NA
Post:   NA
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
