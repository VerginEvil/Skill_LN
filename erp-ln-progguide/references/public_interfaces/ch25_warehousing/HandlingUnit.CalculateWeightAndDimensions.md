# HandlingUnit.CalculateWeightAndDimensions

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1032-1033

```baan
DLL:   whextwmdapi
This function is available from     2024.12 (KB3529999  ).
Syntax: long HandlingUnit.CalculateWeightAndDimensions(
domain  whhuid           iHandlingUnit,
boolean          iOverruleFixedWeightAndDimensions,
ref     domain  tccuni           oWeightUnit,
ref     domain  tcwght           oGrossWeight,
ref     domain  tcwght           oNetWeight,
ref     domain  tccuni           oDimensionUnit,
ref     domain  tcleng           oDepth,
ref     domain  tcleng           oWidth,
ref     domain  tcleng           oHeight,
ref     domain  tcflsp           oFloorSpace,
ref     domain  tcvolm           oVolume,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will calculate and optionally update
weight and dimensions of iHandlingUnit.
Pre:    db.retry.point() is set.
Post:   commit/abort.transaction.
Input:  iHandlingUnit               - Handling Unit (Mandatory).
iOverruleFixedWeightAndDimensions                       - if field Fixed Dimensions in
iHandlingUnit is on Yes this field will be set to No and
Weight and Dimensions will be updated (Mandatory)
Output: oWeightUnit                   - Weight Unit
oGrossWeight                          - Calculated Gross Weight
oNetWeight                            - Calculated Net Weight
oDimensionUnit                        - Dimension Unit
oDepth                                - Calculated Depth
oWidth                                - Calculated Width
oHeight                               - Calculated Height
oFloorSpace                           - Calculated Floor Space
oVolume                               - Calculated Volume
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Handling Unit weight and dimensions are calculated
successfully.
<> 0                          - Error
```
