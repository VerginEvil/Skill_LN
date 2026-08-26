# QuarantineInventoryDispositionLine.Split

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventoryDispositionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1215-1216

```baan
DLL:   whextwmdapi
This function is available from     2026.04 (KB3665487  ).
Syntax: long QuarantineInventoryDispositionLine.Split(
domain  tcorno           iQuarantineIdentifier,
domain  tcmcs.long       iDispositionLine,
domain  tcqst1           iQuantityInStorageUnit,
domain  tccuni           iStorageUnit,
ref     domain  tcorno           oQuarantineIdentifier,
ref     domain  tcmcs.long       oDispositionLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will split a given Quarantine Inventory
Disposition Line.
The line can be split using this function if:
-                       It is not processed yet
-                       No handling unit is linked
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier               - The Quarantine ID (mandatory)
iDispositionLine                       - Disposition Line Number (mandatory)
iQuantityInStorageUnit                       - Disposition line quantity to be
split in storage unit (mandatory).
iStorageUnit                        - Unit of the disposition line (mandatory).
Output: oQuarantineIdentifier               - The Quarantine ID with a new line.
oDispositionLine                       - A new Disposition Line.
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0               - Disposition line has been split successfully
DALHOOKERROR                       - Otherwise.
```

## Public Interfaces for

## QuarantineInventoryHandlingUnit

The following functions are available: QuarantineInventoryHandlingUnit.Move QuarantineInventoryHandlingUnit.Process QuarantineInventoryHandlingUnit.ProcessV2
