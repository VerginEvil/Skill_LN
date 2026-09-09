# QuarantineInventory.Move

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1211-1212

```baan
DLL:   whextwmdapi
This function is available from 2021.09 (KB2198331).
Syntax: long QuarantineInventory.Move(
domain  tcorno           iQuarantineIdentifier,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  whloca           iDestinationLocation,
ref             boolean          oMoved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will Move all quarantine inventory of a
Quarantine Identifier to another quarantine location.
Moving the quarantine inventory is allowed if still unprocessed
disposition line(s) exist.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier - The Quarantine ID (mandatory)
iWarehouse - Warehouse (mandatory)
iItem - Item (mandatory)
iDestinationLocation - The destination quarantine location
(mandatory).
Output: oMoved - Indicates whether moving succeeded or not
true: Inventory successfully moved
false: Inventory not successfully moved (or not found)
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Quarantine Inventory has been moved succesfully
<> 0    - Error
```
