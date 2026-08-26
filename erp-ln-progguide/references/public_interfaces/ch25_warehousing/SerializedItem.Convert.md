# SerializedItem.Convert

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1125-1127

```baan
DLL:   whextltcapi
This function is available from     2024.01 (KB2318156  ).
Syntax: long SerializedItem.Convert(
domain  tcitem           iItem,
domain  whltc.conv.ser   iConversionTo,
domain  tcyesno          iSerialTracking,
domain  tcynna           iRegisterSerialEntryForDirectDelivery,
domain  tcynna           iRegisterSerialEntryDuringReceipt,
domain  tcynna           iRegisterSerialEntryDuringTransfer,
domain  tcynna           iRegisterSerialIssueDuringAsBuilt,
domain  tcynna           iRegisterSerialIssueInService,
domain  whwmd.rgtm       iLotSerialRegistrationTemplate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function converts a non-serialized item or low volume
serialized item to a high volume serialized item.
In other words, an item which is non                      -serialized or Serialized
(in inventory) is converted to 'Serial not in inventory'.
Other conversion options are not (yet) supported.
The (mandatory) serial registration settings will be updated
in session Item                       - Warehousing (whwmd4500m000).
Optionally, the Serial Tracking and/or Serial Registration
Template can also be updated.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iItem               - Item (mandatory)
iConversionTo                       - Conversion To (mandatory):
-                              > Serial Not In Inventory (high volume)
iSerialTracking                       - Serial Tracking (mandatory):
-                              > Yes
-                              > No
If the value of this field is Yes, the item's serial
number is tracked during receipts and issues in
warehousing.
iRegisterSerialEntryForDirectDelivery (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume serials.
If the value of this field is Yes, and the order line
on the ASN is a direct delivery purchase line,
you must register the serial number in the
Shipment Notice Line Stock Point Details (whinh3105m000)
session.
iRegisterSerialEntryDuringReceipt (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume serials.
If the value of this field is Yes, you must register the
serial numbers of received serialized items in the
Receipt Line Stock Point Details (whinh3123m000) session.
iRegisterSerialEntryDuringTransfer (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume serials.
If the value of this field is Yes, you must register the
serial numbers for both the inbound and outbound lines
of transfer orders, but only if registration during
Receipt is also Yes.
iRegisterSerialIssueDuringAsBuilt (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume serials.
The value of this field determine at which point you
must register serial numbers for component items that
are issued from the warehouse to the job shop to
manufacture end items listed on production orders
in Manufacturing.
If the value of this field is Yes, you must register the
serials in Serial End Item                               - As-Built Components
(timfc0111m000), and NOT during issue from warehouse.
iRegisterSerialIssueInService (mandatory)
-                              > Yes
-                              > No
Only applicable when converting to high volume serials.
If the value of this field is Yes, you must register the
serials in Serials in Service and NOT during issue
from warehouse.
iLotSerialRegistrationTemplate (optional)
Only applicable when converting to high volume serials.
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

## Public Interfaces for LotItem

The following functions are available: LotItem.Convert
