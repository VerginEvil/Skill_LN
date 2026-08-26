# LotItem.Convert

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for LotItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1127-1129

```baan
DLL:   whextltcapi
This function is available from     2024.01 (KB2318156  ).
Syntax: long LotItem.Convert(
domain  tcitem           iItem,
domain  tccom.bpid       iBusinessPartner,
domain  tcclot           iLot,
domain  whltc.conv       iConversionTo,
domain  tcyesno          iLotTracking,
domain  tcynna           iRegisterLotEntryForDirectDelivery,
domain  tcynna           iRegisterLotEntryDuringReceipt,
domain  tcynna           iRegisterLotEntryDuringTransfer,
domain  tcynna           iRegisterLotIssueDuringAsBuilt,
domain  tcynna           iRegisterLotIssueInService,
domain  whwmd.rgtm       iLotSerialRegistrationTemplate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to convert an item in one of the
following ways:
-                       To convert a non-lot item to a lot item
-                       To convert a lot item to a non-lot item
-                       To convert a lot item of the Lot in Inventory type to a
lot item of the Lot not in Inventory type or vice versa.
The (mandatory) lot registration settings will be updated
in session Item                       - Warehousing (whwmd4500m000).
Optionally, the Lot Tracking and/or Lot Registration
Template can also be updated.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iItem               - Item (mandatory)
iBusinessPartner                       - The Buy-from business partner's code.
This argument is mandatory if the item is a purchased
item and converted to a lot controlled item.
iLot                       - Lot code (optional). This argument is only used if the
item's outbound method is By Location.
All inventory On Hand is put into this single lot.
If a new lot code must be generated during
conversion, this argument must be left empty.
iConversionTo                       - Conversion To (mandatory):
-                              > Not Lot Controlled
-                              > Lot In Inventory (low volume)
-                              > Lot Not In Inventory (high volume)
iLotTracking                       - Lot Tracking (mandatory):
-                              > Yes
-                              > No
If the value of this field is Yes, the item's lot code
is tracked during receipts and issues in warehousing.
iRegisterLotEntryForDirectDelivery (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume lots.
If the value of this field is Yes, and the order line
on the ASN is a direct delivery purchase line,
you must register the lot code in the
Shipment Notice Line Stock Point Details (whinh3105m000)
session.
iRegisterLotEntryDuringReceipt (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume lots.
If the value of this field is Yes, you must register the
lot codes of received serialized items in the
Receipt Line Stock Point Details (whinh3123m000) session.
iRegisterLotEntryDuringTransfer (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume lots.
If the value of this field is Yes, you must register the
lot codes for both the inbound and outbound lines
of transfer orders, but only if registration during
Receipt is also Yes.
iRegisterLotIssueDuringAsBuilt (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume lots.
The value of this field determine at which point you
must register lot codes for component items that
are issued from the warehouse to the job shop to
manufacture end items listed on production orders
in Manufacturing.
If the value of this field is Yes, you must register the
lot codes in Serial End Item                               - As-Built Components
(timfc0111m000), and NOT during issue from warehouse.
iRegisterLotIssueInService (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume lots.
If the value of this field is Yes, you must register the
lot codes in Serials in Service and NOT during issue
from warehouse.
iLotSerialRegistrationTemplate (optional)
Only applicable when converting to high volume lots.
Lot and serial registration templates are used to
specify the order origins and transaction types for
which serial and/or lot registration must take place.
Output:
oExceptionMessage                       - The last message if any message is
found. If more than one message is given, these are
present in the oExceptionID.
oExceptionID                       - An ID that refers to the exception information.
Use the functions in Exception to get all relevant
information.
Return: 0               - Item has been converted successfully
DALHOOKERROR                       - Item has not been converted successfully
```

## Public Interfaces for Load

The following functions are available: Load.Confirm Load.Freeze Load.Reopen Load.StartAutomaticOutboundProcessing Load.StartDetail Load.StartMultiMain Load.StartOverview
