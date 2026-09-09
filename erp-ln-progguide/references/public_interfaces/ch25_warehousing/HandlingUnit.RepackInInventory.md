# HandlingUnit.RepackInInventory

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1060-1061

```baan
DLL:   whextwmdapi
This function is available from 2024.11 (KB3528024).
Syntax: long HandlingUnit.RepackInInventory(
domain  whhuid           iHandlingUnit,
domain  tcqst1           iQuantityToRepack,
domain  tccuni           iStorageUnit,
boolean          iRepackToTargetHandlingUnit,
domain  whhuid           iTargetHandlingUnit,
domain  whwmd.pkdf       iPackageDefinition,
ref     domain  tcmcs.long       oNumberHandlingUnits,
ref     domain  whhuid           oCreatedHandlingUnitsArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface supports partial or complete unpack of the
handling unit in inventory and moving of the unpacked parts to
the existing or newly created handling units.
Pre:    db.retry.point()
oCreatedHandlingUnitsArray must be declared as based variable.
This function will allocate the memory.
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit - Handling Unit to be repacked (Mandatory)
iHandlingUnit is valid if:
- iHandlingUnit has status In Stock;
- iHandlingUnit is not blocked.
iQuantityToRepack - Quantity to be repacked from the handling unit
(Mandatory)
iStorageUnit     - Storage unit (Mandatory)
iRepackToTargetHandlingUnit - Repack to existing Target Handling
Unit (Mandatory)
iTargetHandlingUnit - defines code of existing target handling
Unit
(Mandatory if iRepackToTargetHandlingUnit is True,
otherwise must be empty)
iTargetHandlingUnit is valid if:
iTargetHandlingUnit has status In Stock;
iTargetHandlingUnit is not blocked;
iTargetHandlingUnit is not fully packed (only for handling units
with a package definition);
iPackageDefinition    - package definition
(Must be empty when iTargetHandlingUnit is filled)
Only package definition of type Variable is allowed.
Output: oNumberHandlingUnits - Number of newly created top level
handling units.
oCreatedHandlingUnitsArray - Array of created handling units.
oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Handling Unit structure is unlinked successfully
<> 0    - Error
```
