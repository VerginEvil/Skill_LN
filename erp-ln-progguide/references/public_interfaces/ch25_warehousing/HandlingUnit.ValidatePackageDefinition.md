# HandlingUnit.ValidatePackageDefinition

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1060-1061

```baan
DLL:   whextwmdapi
This function is available from     2023.05 (KB2287343  ).
Syntax: long HandlingUnit.ValidatePackageDefinition(
domain  whhuid           iHandlingUnit,
domain  whwmd.pkdf       iPackageDefinition,
boolean          iUpdatePackageDefinition,
ref             boolean          oValid,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will validate handling unit against
package definition.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iHandlingUnit               - Handling Unit (Mandatory). Only single item
handling unit is allowed.
iPackageDefinition                       - Package Definition (Optional)
If iPackageDefinition is empty Handling Unit package
definition will be used instead.
If both iPackageDefinition and Handling Unit package
definition are empty an error will be returned.
iPackageDefinition must be of type Variable.
iPackageDefinition must be validated and present for
the item of iHandlingUnit.
iUpdatePackageDefinition                       - Update Handling Unit package
definition after successful validation.
Output: oValid                - Handling Unit structure is according the package
definition.
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Handling Unit structure is validated successfully
<> 0                          - Error
```

## Public Interfaces for HandlingUnitStructure

The following functions are available: HandlingUnitStructure.GetBottomLevel HandlingUnitStructure.GetComponentLevel HandlingUnitStructure.GetInventoryLevel HandlingUnitStructure.GetOrderLineLevel HandlingUnitStructure.GetWholeTree
