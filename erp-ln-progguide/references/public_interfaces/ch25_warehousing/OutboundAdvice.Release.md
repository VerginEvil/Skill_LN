# OutboundAdvice.Release

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundAdvice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1194-1195

```baan
DLL:   whextinhapi
This function is available from 2026.08 (KB3675737).
Syntax: long OutboundAdvice.Release(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iAdvice,
domain  whinh.btno       iOutboundRun,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface releases Outbound Advice for the given
outbound order line.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iOrderOrigin            - Order Origin (Mandatory)
iOrderNumber            - Order Number (Mandatory)
iOrderSet               - Order Set (Mandatory)
iOrderLine              - Order Line (Optional)
iOrderSequence          - Order Sequence (Optional)
iAdvice                 - Outbound Advice (Optional).
When filled, only specific advice
will be released
iOutboundRun            - Outbound Run number (Mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0 - Outbound order line has been processed successfully
<> 0 - Error.
```
