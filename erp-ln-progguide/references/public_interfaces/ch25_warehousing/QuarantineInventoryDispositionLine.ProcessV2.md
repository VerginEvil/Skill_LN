# QuarantineInventoryDispositionLine.ProcessV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventoryDispositionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1214-1215

```baan
DLL:   whextwmdapi
This function is available from     2025.06 (KB3598190  ).
Syntax: long QuarantineInventoryDispositionLine.ProcessV2(
domain  tcorno           iQuarantineIdentifier,
domain  tcmcs.long       iDispositionLine,
domain  tcyesno          iUserInteraction,
ref     domain  tcorno           oAdjustmentOrder,
ref     domain  tcorno           oDispositionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will process a given Quarantine Inventory
Disposition Line.
The line can be processed using this function if:
-                       It is not processed yet
-                       The Disposition field is not 'Awaiting Disposition'
-                       The disposition quantity is not zero
-                       No handling unit is linked
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier               - The Quarantine ID of the disposition
line to be processed (mandatory).
iDispositionLine                       - The Disposition Line to be processed
(mandatory).
iUserInteraction                       - User interaction allowed (mandatory).
Output: oAdjustmentOrder               - The created adjustment order when processing
a disposition line with disposition Scrap.
oDispositionOrder                       - The created disposition order when
processing a disposition line with disposition
Return To Vendor (RTV), Rework (to new/existing
specification) or Reclassify.
In case of RTV: the generated PUR return order
In case of Rework: the generated production rework order
In case of Reclassify: the generated transfer order
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Disposition line has been processed succesfully
<> 0                          - Error
```
