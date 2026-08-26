# ProductVariantOptions.StartOverview

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductVariantOptions
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 702-706

```baan
DLL:   tiextpcfapi
This function is available from     2023.05 (KB2283720  ).
Syntax: long ProductVariantOptions.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccpva           iProductVariant,
domain  tcopts           iOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Product Variant Options in
overview mode (tipcf5520m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
Optional
iProductVariant
The Product Variant for which the session will be
started. Mandatory.
iOptionSet
The Option Set for which the session will be started.
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```

## Public Interfaces for ProductionOrder

The following functions are available: ProductionOrder.CalculateDeliveryDate ProductionOrder.CalculateStartDate ProductionOrder.Cancel ProductionOrder.CancelV2 ProductionOrder.CheckShortages ProductionOrder.Close ProductionOrder.CompressAutomatedQueueTime ProductionOrder.CreateAsBuilt ProductionOrder.DecreaseQuantityOperations ProductionOrder.FinishOperationAddition ProductionOrder.GetActualQuantity ProductionOrder.GetInProcessQuantity ProductionOrder.InitiateInventoryIssue ProductionOrder.InitiateInventoryIssueV2 ProductionOrder.InitiateMaterialInventoryIssue ProductionOrder.MoveRejectedMaterialToQuarantine ProductionOrder.MoveRejectedMaterialToQuarantineV2 ProductionOrder.NewVersion ProductionOrder.PrintCheckList ProductionOrder.PrintCheckListV2 ProductionOrder.PrintCuttingList ProductionOrder.PrintCuttingListV2 ProductionOrder.PrintInspectionNote ProductionOrder.PrintInspectionNoteV2 ProductionOrder.PrintMaterialIssueNote ProductionOrder.PrintMaterialIssueNoteV2 ProductionOrder.PrintMaterialList ProductionOrder.PrintMaterialListV2 ProductionOrder.PrintOperationNote ProductionOrder.PrintOperationNoteV2 ProductionOrder.PrintOrderCoveringNote ProductionOrder.PrintOrderCoveringNoteV2 ProductionOrder.PrintOrderDistribution ProductionOrder.PrintOrderDistributionV2 ProductionOrder.PrintReceiptNote ProductionOrder.PrintReceiptNoteV2 ProductionOrder.PrintRejects ProductionOrder.PrintRoutingSheet ProductionOrder.PrintRoutingSheetV2 ProductionOrder.PrintSawingList ProductionOrder.PrintSawingListV2 ProductionOrder.PrintSerialNumbersList ProductionOrder.PrintSerialNumbersListV2 ProductionOrder.PrintSubcontractingNote ProductionOrder.PrintSubcontractingNoteV2 ProductionOrder.ProcessMaterialQuantityChanges ProductionOrder.ProcessReturn ProductionOrder.Regenerate ProductionOrder.RegenerateV2 ProductionOrder.Release ProductionOrder.RemoveHandlingUnit ProductionOrder.RemoveUnusedHandlingUnits ProductionOrder.ReportProduct ProductionOrder.ReportProductV2 ProductionOrder.ReportProductV3 ProductionOrder.ReportProductWithHandlingUnits ProductionOrder.ReportProductWithSerials ProductionOrder.ReportProductWithSerialsV2 ProductionOrder.ReportProductWithSerialsV3 ProductionOrder.ResetCompletedToActive ProductionOrder.ScrapRejectedMaterial ProductionOrder.SendAndReceiveHandlingUnitsInWarehouse ProductionOrder.SendHandlingUnitsToWarehouse ProductionOrder.Split ProductionOrder.StartClose ProductionOrder.StartDetail ProductionOrder.StartInventoryOverview ProductionOrder.StartMultiMain ProductionOrder.StartOperationAddition ProductionOrder.StartPrintDocuments ProductionOrder.StartReportOperationsCompleted ProductionOrder.StartReportOrdersCompleted ProductionOrder.StartResetStatus ProductionOrder.UpdateMaterialToIssueQuantity ProductionOrders.ProcessMaterialShortages ProductionOrders.StartOverview
