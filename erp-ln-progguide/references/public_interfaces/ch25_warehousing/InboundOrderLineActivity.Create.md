# InboundOrderLineActivity.Create

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundOrderLineActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1076-1076

```baan
DLL:   whextinhapi
This function is available from 2026.09 (KB3688426).
Syntax: long InboundOrderLineActivity.Create(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcyesno          iInspection,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will create the inbound order line activities
for an inbound order line.
Pre:    db.retry.point should be set
Post:   commit or abort transaction depending on the return value.
Input:  iOrderOrigin            - Order Origin (Mandatory)
iOrderNumber            - Order Number (Mandatory)
iOrderLine              - Order Line (Optional)
iOrderSequence          - Order Line Sequence (Optional)
iInspection             - Inspection (Mandatory)
Indicates whether inspection is
applicable for this inbound order
line. When set to tcyesno.yes, the
inspection activities will be marked
as applicable. When set to tcyesno.no,
the inspection activities will be
created but marked as not applicable.
Allowed Values:
tcyesno.yes
tcyesno.no
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
