# ProductionOrder.GenerateHandlingUnitForLineSideLabeling

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1300-1301

```baan
DLL:   whextinhapi
This function is available from     2023.09 (KB2304620  ).
Syntax: long ProductionOrder.GenerateHandlingUnitForLineSideLabeling(
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
boolean          iPublishLabel,
domain  tclabl           iLabelLayout,
domain  tcmcs.long       iNumberOfCopies,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates handling unit structure for production
order in Line Side Labeling scenario.
When generating lot is required Lot Code will be generated or
derived from iLotCode and added in the Item                       - Lot table.
Pre:    db.retry.point()
Post:   commit/abort transaction.
Input:  iOrderNumber                          - production order number (Mandatory)
iEffectivityUnit                              - Effectivity Unit (Optional)
iLabelQuantity                                - Quantity to be labeled (Mandatory)
iLabelUnit                                    - Storage unit (Mandatory)
iLotCode                                      - Lot Code (Optional)
iGenerateLot                                  - Generate Lot (True/False)
iPackageDefinition                            - Package Definition (Optional)
iPackagingItem                                - Packaging Item (Mandatory if
iPackageDefinition is empty)
iPackagingItemQuantity                        - Packaging Item Quantity (Mandatory if
iPackagingItem is filled)
iHandlingUnitMask                             - Handling Unit Mask (Optional,
default mask will be used if empty)
iSSCCMask                                     - SSCC Handling Unit Mask (Mandatory)
iShipmentMask                                 - Use shipment or internal mask
(Mandatory)
iPublishLabel                                 - Publish Package Label BOD (True/False)
iLabelLayout                                  - Label Layout (Optional)
iNumberOfCopies                               - Number of Copies (Mandatory if
iPublishLabel is True)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     - Handling Units are generated
<> 0                          - Generating Handling Units failed
```
