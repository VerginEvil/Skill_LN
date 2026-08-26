# OutboundOrderLineActivity.Create

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLineActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1223-1224

```baan
DLL:   whextinhapi
This function is available from     2023.01 (KB2271017  ).
Syntax: long OutboundOrderLineActivity.Create(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will create the outbound order line activities
for an outbound order line.
Pre:    db.retry.point should be set
Post:   commit or abort transaction depending on the return value.
Input:  iOrderOrigin                          - Mandatory
iOrderNumber                                  - Mandatory
iOrderLine                                    - Optional (inbound line can be 0)
iOrderSequence                                - Optional (inbound sequence can
be 0)
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
