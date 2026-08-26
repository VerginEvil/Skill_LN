# QuarantineInventoryDisposition.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventoryDisposition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1208-1209

```baan
DLL:   whextwmdapi
This function is available from     2026.01 (KB3639796  ).
Syntax: long QuarantineInventoryDisposition.Process(
domain  tcorno           iQuarantineIdentifier,
domain  tcyesno          iUserInteraction,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will process a given Quarantine Inventory
Disposition.
All disposition lines which are not 'Awaiting Disposition'
and not 'Processed' will be handled.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier               - The Quarantine ID of the disposition
line to be processed (mandatory).
iUserInteraction                       - User interaction allowed (mandatory).
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Disposition has been processed succesfully
<> 0                          - Error
```
