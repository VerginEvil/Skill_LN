# QuarantineInventoryDispositionLine.Move

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventoryDispositionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1213-1214

```baan
DLL:   whextwmdapi
This function is available from     2021.09 (KB2198331  ).
Syntax: long QuarantineInventoryDispositionLine.Move(
domain  tcorno           iQuarantineIdentifier,
domain  tcmcs.long       iDispositionLine,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  whloca           iDestinationLocation,
domain  tcqst1           iQuantityInStorageUnit,
domain  tccuni           iStorageUnit,
ref             boolean          oMoved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will Move an individual quarantine
disposition line to another quarantine location.
Moving the disposition is allowed if still unprocessed and
no Handling Unit is linked.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier               - The Quarantine ID (mandatory)
iDispositionLine                       - Disposition Line Number (mandatory)
iWarehouse                       - Warehouse (mandatory)
iItem                       - Item (mandatory)
iDestinationLocation                       - The destination quarantine location.
(mandatory).
iQuantityInStorageUnit                       - Disposition line quantity to be
moved in storage unit (mandatory).
If this quantity is less than the disposition line
quantity, the line will be split and only this
quantity will be moved.
iStorageUnit                       - Unit of the disposition line (mandatory).
Output: oMoved               - Indicates whether moving succeeded or not
true: Inventory successfully moved
false: Inventory not successfully moved (or not found)
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Quarantine Inventory has been moved succesfully
<> 0                          - Error
```
