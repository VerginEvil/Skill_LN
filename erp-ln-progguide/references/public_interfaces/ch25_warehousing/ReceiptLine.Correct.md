# ReceiptLine.Correct

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ReceiptLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1237-1240

```baan
DLL:   whextinhapi
This function is available from     2026.05 (KB3628985  ).
Syntax: long ReceiptLine.Correct(
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  whhuid           iHandlingUnit,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will correct the given receipt line and
receipt line stock point details.
Correcting the final receipt flag must be done via
ReceiptLine.CorrectFinalReceipt.
Reversing the receipt of a Receipt Line or Handling Unit
must be done via ReceiptLine.Reverse.
Be aware that transaction management is handled within this
function.
Pre:    N.a.
Post:   N.a.
Input:  iReceipt                Mandatory
iReceiptLine            Mandatory
iHandlingUnit           Optional, unless handling units are
linked to the receipt line.
Handling unit must have no children.
iProcessingOptionSet    Mandatory.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Receipt Correction (whinh3121m000) and are not explained in
further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
NAME                    TYPE                    DEFAULT
NewQuantity             domain tcqst1           Current Quantity
NewUnit                 domain tccuni           Current Unit
NewPackingSlipQuantity  domain tcqiv1           Current Quantity
NewPackingSlipUnit      domain tccuni           Current Unit
AdjustLocation          domain whloca           Current Location
NewWeight               domain tcwght           Current Weight
NewWeightUnit           domain tccuni           Current Unit
CorrectionDetailArray   domain ttjson           0
AdjustLocation               - Value is ignored when iHandlingUnit is filled.
When warehouse and item of receipt line are location
controlled, then this field becomes mandatory when
iHandlingUnit is not filled.
NewWeight               - If not set, it's value will be recalculated based on the
changed NewQuantity and/or NewUnit.
JSON Object CorrectionDetailArray has the following structure:
"CorrectionDetailArray": [
{
"DistributionSequence": 3,
"StockpointDetailOptionSet": 3920279533,
},
{
"DistributionSequence": 5,
"StockpointDetailOptionSet": 4833943222,
}
]
For every distribution sequence of the receipt line stock point
correction detail, a separate stock point detail option set must be
created where only the changed fields need to be passed.
This is not needed when there is only one stock point correction detail
and only the received quantity and/or unit needs to be changed.
In this case the receipt line stock point correction detail is
automatically updated.
These Processing Options have a direct relationship with the form fields
on session Receipt Line Stock Point Correction Details (whinh3141m000)
and are not explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
NAME                        TYPE                DEFAULT
CorrectedSerialNumber       domain tcibd.sern   Received Serial Number
CorrectedLot                domain tcclot       Received Lot
CorrectedBusinessPartnerLot domain whltc.ltbp   Received Bus.Partner Lot
CorrectedInventoryDate      domain tcinvt.date  Received Inventory Date
CorrectedEffectivityUnit    domain tcuef.effn   Received Effect. Unit
CorrectedRevision           domain tcedm.revi   Received Revision
CorrectedQuantity           domain tcqst1       Received Quantity
CorrectedUnit               domain tccuni       Received Unit
This structure can be created with the following code:
CorrectionDetailArray = Json.newArray()
stockpoint.detail = Json.newObject()
Json.setNumber(stockpoint.detail, "DistributionSequence", 3)
ret = ProcessingOptionSet.Create(
StockpointDetailOptionSet,
ExceptionMessage,
ExceptionID,
|* Option name          Value
"CorrectedLot",         "OtherLot1",
"CorrectedQuantity",    2.0)
Json.setNumber( stockpoint.detail,
"StockpointObject",
StockpointDetailOptionSet)
Json.add(CorrectionDetailArray, stockpoint.detail)
stockpoint.detail = Json.newObject()
Json.setNumber(stockpoint.detail, "DistributionSequence", 5)
ret = ProcessingOptionSet.Create(
StockpointDetailOptionSet,
ExceptionMessage,
ExceptionID,
|* Option name          Value
"CorrectedLot",         "NewLot1",
"CorrectedQuantity",    10.0,
"CorrectedUnit",        "pcs")
Json.setNumber( stockpoint.detail,
"StockpointObject",
StockpointDetailOptionSet)
Json.add(CorrectionDetailArray, stockpoint.detail)
This CorrectionDetailArray then needs to be added to the
ProcessingOptionSet.
ret = ProcessingOptionSet.Create(
ProcessingOptionSet,
ExceptionMessage,
ExceptionID,
|* Option name          Value
"NewQuantity",          25.0,
"CorrectionDetailArray",CorrectionDetailArray)
In this example the Receipt Line Quantity is corrected to 25 pcs.
The Lot of Stock Point Correction Detail with distribution sequence 3
is changed to "OtherLot1" and the received quantity to 2.
A new Stock Point Correction Detail with distribution sequence 5
is created for "NewLot1" and a received quantity of 10 pcs.
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
