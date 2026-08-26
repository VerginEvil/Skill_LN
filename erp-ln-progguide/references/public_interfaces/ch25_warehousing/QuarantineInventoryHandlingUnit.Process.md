# QuarantineInventoryHandlingUnit.Process

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventoryHandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1217-1218

```baan
DLL:   whextwmdapi
This function is available from     2020.05 (KB2124871  ).
Syntax: long QuarantineInventoryHandlingUnit.Process(
domain  tcorno           iQuarantineIdentifier,
domain  whhuid           iHandlingUnit,
ref     domain  tcorno           oAdjustmentOrder,
ref     domain  tcorno           oDispositionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will process a given Handling Unit in
Quarantine Inventory. Processing the handling unit is allowed if
-                       The handling unit is not processed yet.
-                       Active Handling Unit Process data (whwmd273) exists
-                       The disposition (whwmd273.disp) is not 'Awaiting disposition'
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier               - The Quarantine ID of the handling unit
to be processed (mandatory).
iHandlingUnit                       - The Handling Unit to be processed (mandatory).
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
Return: 0                     - Handling Unit has been processed succesfully
<> 0                          - Error
```
