# AllocationChangeOrder.Generate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for AllocationChangeOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1109-1112

```baan
DLL:   whextinhapi
This function is available from 2023.03 (KB2278026).
Syntax: long AllocationChangeOrder.Generate(
domain  tccwar           iWarehouse,
domain  tccdis           iReason,
domain  tcseri           iSeries,
domain  tcyesno          iDirectlyProcess,
boolean          iSetHeaderText,
domain  tctxtn           iHeaderText,
boolean          iSetItem,
domain  tcitem           iItem,
boolean          iSetEffectivityUnit,
domain  tcuef.effn       iEffectivityUnit,
boolean          iSetHandlingUnit,
domain  whhuid           iHandlingUnit,
boolean          iSetOrderQuantity,
domain  tcqst1           iOrderQuantity,
boolean          iSetOrderUnit,
domain  tccuni           iOrderUnit,
boolean          iSetSoldToBusinessPartnerFrom,
domain  tccom.bpid       iSoldToBusinessPartnerFrom,
boolean          iSetShipToBusinessPartnerFrom,
domain  tccom.bpid       iShipToBusinessPartnerFrom,
boolean          iSetBusinessObjectTypeFrom,
domain  tcalbt           iBusinessObjectTypeFrom,
boolean          iSetBusinessObjectFrom,
domain  tcboid           iBusinessObjectFrom,
boolean          iSetBusinessObjectReferenceFrom,
domain  tcborf           iBusinessObjectReferenceFrom,
boolean          iSetReferenceFrom,
domain  tcrefa           iReferenceFrom mb,
boolean          iSetSoldToBusinessPartnerTo,
domain  tccom.bpid       iSoldToBusinessPartnerTo,
boolean          iSetShipToBusinessPartnerTo,
domain  tccom.bpid       iShipToBusinessPartnerTo,
boolean          iSetBusinessObjectTypeTo,
domain  tcalbt           iBusinessObjectTypeTo,
boolean          iSetBusinessObjectTo,
domain  tcboid           iBusinessObjectTo,
boolean          iSetBusinessObjectReferenceTo,
domain  tcborf           iBusinessObjectReferenceTo,
boolean          iSetReferenceTo,
domain  tcrefa           iReferenceTo mb,
boolean          iSetLineText,
domain  tctxtn           iLineText,
ref     domain  tcorno           oAllocationChangeOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function generates an Allocation Change Order header and
line. Optionally, the allocation change order can be processed
directly.
Only allowed when the Demand Pegging concept is enabled in
Implemented Software Components (tccom0500m000).
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iWarehouse (mandatory)
The warehouse where the inventory allocation must change
iReason (mandatory)
The reason code of the allocation change. Must be of
type 'Allocation Change'
iSeries
The series used for allocation change order generation.
Must exist for the Number Group defined for allocation
change orders in Inventory Handling Parameters.
If left empty, the series defined in the User Profiles,
Warehouse Settings by Site or Inventory Handling
Parameters are used
iDirectlyProcess (mandatory)
Directly process the generated allocation change (Yes/No)
iSetHeaderText
Set text for allocation change order header (True/False)
iHeaderText
Allocation change order header text number
iSetItem
Set Item (True/False)
iItem
The Item whose allocation is to change.
Is mandatory if the iHandlingUnit is empty
If iHandlingUnit is filled, this field is derived from
the handling unit.
iSetEffectivityUnit
Set Effectivity Unit (True/False)
iEffectivityUnit
Effectivity Unit. Only applicable if the item is
lot controlled (in inventory).
iSetHandlingUnit
Set Handling Unit (True/False)
iHandlingUnit
The Handling Unit that contains inventory whose
allocation is to change.
Is mandatory if the Allocation Registration
Level of the item by warehouse is by 'Physical Item'
iSetOrderQuantity (mandatory if iHandlingUnit is empty)
Set Order Quantity (True/False)
iOrderQuantity (mandatory if iHandlingUnit is empty)
Order Quantity in order unit. Value must be > 0.
If handling unit is filled, this field is derived from
the handling unit.
iSetOrderUnit (mandatory if iHandlingUnit is empty)
Set Order Unit (True/False)
iOrderUnit (mandatory if iHandlingUnit is empty)
Order Unit
If iHandlingUnit is filled, this field is derived from
the handling unit.
iSetSoldToBusinessPartnerFrom
Set allocated Sold-to Business partner - from (true/false)
iSoldToBusinessPartnerFrom
The sold-to business partner to which the inventory is
allocated before the allocation change order is processed
iSetShipToBusinessPartnerFrom
Set allocated Ship-to Business partner - from (true/false)
iShipToBusinessPartnerFrom
The ship-to business partner to which the inventory is
allocated before the allocation change order is processed
iSetBusinessObjectTypeFrom
Set allocated Business Object Type - from (true/false)
iBusinessObjectTypeFrom
The business object type (Order type) to which the
inventory is allocated before the allocation change
order is processed
iSetBusinessObjectFrom
Set allocated Business Object - from (true/false)
iBusinessObjectFrom
The business object (Order) to which the inventory is
allocated before the allocation change order is processed
iSetBusinessObjectReferenceFrom
Set allocated business object reference - from (true/false)
iBusinessObjectReferenceFrom
The business object reference (Order line) to which
the inventory is allocated before the allocation change
order is processed
iSetReferenceFrom
Set Reference - from (true/false)
iReferenceFrom
A reference code to which the inventory was allocated
before the allocation change order is processed
iSetSoldToBusinessPartnerTo
Set allocated Sold-to Business partner - to (true/false)
iSoldToBusinessPartnerTo
The sold-to business partner to which the inventory is
allocated after the allocation change order is processed
iSetShipToBusinessPartnerTo
Set allocated Ship-to Business partner - to (true/false)
iShipToBusinessPartnerTo
The ship-to business partner to which the inventory is
allocated after the allocation change order is processed
iSetBusinessObjectTypeTo
Set allocated Business Object Type - to (true/false)
iBusinessObjectTypeTo
The business object type (Order type) to which the
inventory is allocated after the allocation change
order is processed
iSetBusinessObjectTo
Set allocated Business Object - to (true/false)
iBusinessObjectTo
The business object (Order) to which the inventory is
allocated after the allocation change order is processed
iSetBusinessObjectReferenceTo
Set allocated business object reference - to (true/false)
iBusinessObjectReferenceTo
The business object reference (Order line) to which
the inventory is allocated after the allocation change
order is processed
iSetReferenceTo
Set Reference - to (true/false)
iReferenceTo
A reference code to which the inventory was allocated
after the allocation change order is processed
iSetLineText
Set allocation change order line text (true/false)
iLineText
Allocation change order line text number
Output: oAllocationChangeOrder
The generated allocation change order number.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0: OK
<> 0: Error
```
