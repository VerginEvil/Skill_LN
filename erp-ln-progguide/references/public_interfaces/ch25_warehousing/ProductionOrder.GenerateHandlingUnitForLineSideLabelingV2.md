# ProductionOrder.GenerateHandlingUnitForLineSideLabelingV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1311-1312

```baan
DLL:   whextinhapi
This function is available from 2025.05 (KB3565601).
Syntax: long ProductionOrder.GenerateHandlingUnitForLineSideLabelingV2(
domain  tcorno           iOrderNumber,
domain  tcuef.effn       iEffectivityUnit,
domain  tcqst1           iLabelQuantity,
domain  tccuni           iLabelQuantityUnit,
domain  tcclot           iLotCode,
boolean          iGenerateLot,
domain  whwmd.pkdf       iPackageDefinition,
domain  tcitem           iPackagingItem,
domain  tcqiv1           iPackagingItemQuantity,
domain  tcuef.mask       iHandlingUnitMask,
domain  tcyesno          iSSCCMask,
domain  tcyesno          iShipmentMask,
boolean          iPrintLabels,
domain  whwmd.lbpb       iLabelPrintedBy,
domain  tcmcs.str15      iDevice,
domain  tclabl           iLabelLayout,
domain  tcmcs.long       iNumberOfCopies,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates handling unit structure for production
order in Line Side Labeling scenario.
When generating lot is required Lot Code will be generated or
derived from iLotCode and added in the Item - Lot table.
Labels of generated handling units can be printed or published.
Pre:    db.retry.point()
Post:   commit/abort transaction.
Input:  iOrderNumber            - Production Order Number (Mandatory)
iEffectivityUnit        - Effectivity Unit (Optional)
iLabelQuantity          - Quantity to be labeled (Mandatory)
iLabelUnit              - Storage unit (Mandatory)
iLotCode                - Lot Code (Optional)
iGenerateLot            - Generate Lot (True/False)
iPackageDefinition      - Package Definition (Optional)
iPackagingItem          - Packaging Item (Mandatory if
iPackageDefinition is empty)
iPackagingItemQuantity  - Packaging Item Quantity (Mandatory if
iPackagingItem is filled)
iHandlingUnitMask       - Handling Unit Mask (Optional,
default mask will be used if empty)
iSSCCMask               - SSCC Handling Unit Mask (Mandatory)
iShipmentMask           - Use shipment or internal mask
(Mandatory)
iPrintLabels            - Print Labels (True/False)
iLabelPrintedBy - Label Printed By (Mandatory if
iPrintLabels = True)
Possible values are:
- whwmd.lbpb.internal - Report will be printed
- whwmd.lbpb.external - BOD will be published
iDevice                 - Report Device (Mandatory if
iPrintLabels = True and
iLabelPrintedBy = whwmd.lbpb.internal
iLabelLayout            - Label Layout (Mandatory if
iPrintLabels = True)
iNumberOfCopies         - Number of Copies (Mandatory if
iPrintLabels = True)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - Handling Units are generated
<> 0    - Generating Handling Units failed
```
