# PackageDefinition.Validate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for PackageDefinition
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1030-1031

```baan
DLL:   whextwmdapi
This function is available from     2025.04 (KB3562830  ).
Syntax: long PackageDefinition.Validate(
domain  tcitem           iItem,
domain  whwmd.pkdf       iPackageDefinition,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface validates a package definition.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iItem                 - Item (Optional). If empty not item specific
package definition will be validated.
iPackageDefinition                       - Package Definition (Mandatory)
Output: oExceptionMessage               - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0               - Package Defintion validated succesfully
DALHOOKERROR                       - Package Definition not validated; error message set.
```

## Public Interfaces for HandlingUnit

The following functions are available: HandlingUnit.ApproveRemaining HandlingUnit.CalculateWeightAndDimensions HandlingUnit.Close HandlingUnit.CommitInventory HandlingUnit.ConfirmReceipt HandlingUnit.Create HandlingUnit.GenerateEmptyHandlingUnits HandlingUnit.GenerateLots HandlingUnit.GenerateSerials HandlingUnit.GlobalBlock HandlingUnit.Link HandlingUnit.MoveToLoad HandlingUnit.MoveToShipment HandlingUnit.PrintLabelByPackageLabelBOD HandlingUnit.PrintLabels HandlingUnit.Receive HandlingUnit.RejectRemaining HandlingUnit.Remove HandlingUnit.RemoveEmptyHandlingUnits HandlingUnit.RepackInInventory HandlingUnit.SetToNotShipped HandlingUnit.SetToShipped HandlingUnit.StartAutomaticInboundProcessing HandlingUnit.StartDetail HandlingUnit.StartOverview HandlingUnit.StartPrintLabels HandlingUnit.Transfer HandlingUnit.Unlink HandlingUnit.Unpack HandlingUnit.ValidatePackageDefinition
