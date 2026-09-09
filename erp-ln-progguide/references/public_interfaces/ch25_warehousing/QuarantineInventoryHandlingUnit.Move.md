# QuarantineInventoryHandlingUnit.Move

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for QuarantineInventoryHandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1226-1227

```baan
DLL:   whextwmdapi
This function is available from 2021.09 (KB2198331).
Syntax: long QuarantineInventoryHandlingUnit.Move(
domain  tcorno           iQuarantineIdentifier,
domain  tccwar           iWarehouse,
domain  tcitem           iItem,
domain  whhuid           iHandlingUnit,
domain  whloca           iDestinationLocation,
ref             boolean          oMoved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will Move a given Handling Unit in
Quarantine Inventory to another quarantine location.
Moving the handling unit is allowed if
- The handling unit is not processed yet.
- Active Handling Unit Process data (whwmd273) exists
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iQuarantineIdentifier - The Quarantine ID of the handling unit
to be moved (mandatory).
iWarehouse - Warehouse (mandatory)
iItem - Item (mandatory)
iHandlingUnit - The Handling Unit to be moved (mandatory).
iDestinationLocation - The destination quarantine location to
move the handling unit to (mandatory).
Output: oMoved - Indicates whether moving succeeded or not
true: Inventory successfully moved
false: Inventory not successfully moved (or not found)
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Handling Unit has been moved succesfully
<> 0    - Error
```
