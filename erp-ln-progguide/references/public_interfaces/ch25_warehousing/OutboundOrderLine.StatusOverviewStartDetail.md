# OutboundOrderLine.StatusOverviewStartDetail

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1241-1242

```baan
DLL:   whextinhapi
This function is available from 2025.08 (KB3606158).
Syntax: long OutboundOrderLine.StatusOverviewStartDetail(
long             iStartMode,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the detail session Outbound Line
Status Overview (whinh2129m000).
Input:  iStartMode
Specifies the start mode for the session. (Mandatory)
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iOrderOrigin            - Order Origin (Mandatory)
iOrderNumber            - Order Number (Mandatory)
iOrderLine              - Order Line (Optional)
iOrderSequence          - Order Line Sequence (Optional)
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
