# PurchaseOrderChangeRequest.Cancel

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderChangeRequest
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 481-481

```baan
DLL:   tdextpurapi
This function is available from 2026.04 (KB3663690).
Syntax: long PurchaseOrderChangeRequest.Cancel(
domain  tcorno           iChangeRequest,
domain  tcmcs.str2       iAcknowledgementCode,
domain  tcmcs.str8       iChangeOrderSequence,
domain  tccdis           iChangeReason,
domain  tccdis           iChangeType,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function cancels the given purchase order change request.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iChangeRequest          - Purchase Order Change Request (Mandatory)
iAcknowledgementCode    - Acknowledgement code (Optional)
iChangeOrderSequence    - Change sequence (Optional)
iChangeReason           - Change reason (Optional)
iChangeType             - Change type (Optional)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       -> The change request has been cancelled
<> 0    -> An error occurred
```
