# HandlingUnit.Create

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1035-1036

```baan
DLL:   whextwmdapi
This function is available from     2020.08 (KB2131029  ).
Syntax: long HandlingUnit.Create(
domain  whhuid           iHandlingUnit,
domain  tcuef.mask       iHandlingUnitMask,
domain  tcyesno          iSSCCMask,
domain  tcitem           iPackagingItem,
domain  tcqiv1           iPackagingItemQuantity,
domain  tccwar           iWarehouse,
domain  tccom.bpid       iBusinessPartner,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
ref     domain  whhuid           oHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will create an inactive handling unit.
Handling unit can contain some extra information based
on input data:
Packaging item and packaging item quantity (when not empty);
Order line related data (when known):
-                       Warehouse;
-                       Business Partner;
Handling Unit mask will be defaulted following below described
priority:
-                       iHandlingUnitMask (if not empty)
-                       Business Partner (when iBusinessPartner is filled or
when the Business Partner can be defaulted based on the passed
order line).
-                               Business Partner in Ship To role mask;
-                               Business Partner in Sold To role mask;
-                       Warehouse Internal mask (if iWarehouse is filled and internal
mask is defined);
Note: if iWarehouse and/or iBusinessPartner are empty they
can be read from the passed order line if any;
-                       Inventory Parameters mask
Input data will be verified as follows:
-                       If iHandlingUnit is not empty, handling unit with the same Id
cannot exist in the system (table whwmd530);
-                       If iPackagingItem is not empty, iPackagingItemQuantity
must have a positive value.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit               - The Handling Unit ID (if empty a handling unit
Id will be generated automatically based on handling unit mask).
iHandlingUnitMask (optional)
iSSCCMask                       - SSCC mask (yes/no)
iPackagingItem                       - Packaging item (optional)
iPackagingItemQuantity                       - Packaging Item Quantity
iWarehouse                       - Warehouse (optional)
iBusinessPartner                       - Business Partner (optional)
iOrderOrigin                       - Order Origin (optional)
iOrderNumber                       - Order Number (optional)
iOrderLine   = Order Line (optional)
iOrderLineSequence                       - Order Line Sequence (optional)
Output: oHandlingUnit               - Generated handling unit
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - Handling Unit has been generated successfully
<> 0                          - Error
```
