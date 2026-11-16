# HandlingUnit.Unpack

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1068-1070

```baan
DLL:   whextwmdapi
This function is available from 2022.06 (KB2223834).
Syntax: long HandlingUnit.Unpack(
domain  whhuid           iHandlingUnit,
boolean          iAllowHandlingUnitWithChilds,
domain  tcqst1           iQuantityToSplit,
domain  tccuni           iStorageUnit,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
boolean          iSetTargetHandlingUnitId,
domain  whhuid           iTargetHandlingUnitId,
boolean          iToPackageDefinition,
domain  whwmd.pkdf       iPackageDefinition,
domain  tcitem           iPackagingItem,
domain  tcqiv1           iQuantityOfPackagingItem,
boolean          iCheckSplittable,
domain  tcmcs.long       iNumberOfStockPointDetails,
ref     domain  tcclot           iStockPointDetailLotArray() fixed,
ref     domain  tcibd.sern       iStockPointDetailSerialArray() fixed,
ref     domain  tcqst1           iStockPointDetailQuantityArray(),
ref     domain  tccuni           iStockPointDetailStorageUnitArray() fixed,
ref     domain  tcmcs.long       oNumberHandlingUnits,
ref     domain  whhuid           oCreatedHandlingUnitsArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface supports unpack of the handling unit and
moving of the unpacked parts to the newly created handling units.
Pre:    db.retry.point()
oCreatedHandlingUnitsArray must be declared as based variable.
This function will allocate the memory.
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit - Handling Unit to be unpacked (Mandatory)
iHandlingUnit is valid if:
- iHandlingUnit has status Receipt Open, Received, Approved,
In Stock, Partially Allocated, Partially Released or Staged;
- iHandlingUnit has empty package definition or package
definition of type Variable.
iAllowHandlingUnitWithChilds - Allow unpack of the handling unit
with children. If this parameter is on True iHandlingUnit can
have bottom level handling units.
First bottom level handling unit with quantity which is greater
than iQuantityToSplit will be unpacked.
If no such handling unit is found an error message will be
returned.
iQuantityToSplit - Quantity to be split from the handling unit
(Mandatory)
iStorageUnit     - Storage unit (Mandatory)
iOrderOrigin     - Order origin (Optional)
iOrder           - Order number (Optional)
iOrderSet        - Order set (Optional)
iOrderLine       - Order Line (Optional)
iOrderSequence   - Order Line Sequence (Optional)
Order data is needed to generate handling unit code
for the new handling unit if handling unit mask contains
order related fields.
iSetTargetHandlingUnitId - Target Handling Unit code is defined
(Mandatory)
iTargetHandlingUnitId - defines code of the new handling unit.
Note: it is not allowed to unpack handling unit to the
existing target handling unit in stock. This parameter
only defines the code of the newly created handling unit.
If handling unit with this code already exists it must
have status Inactive.
If iTargetHandlingUnitId is empty a new handling unit
will be generated.
(Mandatory if iSetTargetHandlingUnitId is True)
iToPackageDefinition - Create new handling unit with a
package definition (Mandatory)
iPackageDefinition    - package definition
(Mandatory if iToPackageDefinition is True)
Only package definition of type Variable is allowed.
iPackageDefinition is only allowed when iHandlingUnit
has status In Stock, Partially Allocated or
Partially Released.
iPackageDefinition is not allowed if
iTargetHandlingUnitId is filled.
Reason: multiple handling units can be generated when
repacking to the new iPackageDefinition.
iPackagingItem        - packaging item (Optional)
iPackagingItem is not allowed in combination with
iPackageDefinition.
iQuantityOfPackagingItem  - Quantity of packaging item
(Mandatory if iPackagingItem is filled)
iCheckSplittable      - Check whether handling unit is splittable.
(Mandatory)
If iCheckSplittable is False a checkbox Splittable in
iHandlingUnit will be ignored.
iNumberOfStockPointDetails - Number of stock point details
(Mandatory)
iStockPointDetailLotArray       - Array of Lots
iStockPointDetailSerialArray    - Array of serials
iStockPointDetailQuantityArray  - Array with quantities
iStockPointDetailStorageUnitArray - Array with storage units
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
