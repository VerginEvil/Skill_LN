# ProductionOrder.MoveRejectedMaterialToQuarantineV2

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 719-721

```baan
DLL:   tiextsfcapi
This function is available from     2025.09 (KB3546226  ).
Syntax: long ProductionOrder.MoveRejectedMaterialToQuarantineV2(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcpono           iMaterialLine,
domain  tcitem           iItem,
domain  tiqep1           iQuantity,
domain  tcibd.sern       iSerial,
domain  tcuef.effn       iUnit,
domain  tcclot           iLot,
domain  tccwar           iQuarantineWarehouse,
domain  tiloca           iQuarantineLocation,
const           string           iQuarantineText(),
boolean          iDirectProcessInbound,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to move rejected Material to
Quarantine for a given Production Order and Material Line.
Transaction management is handled by this Public Interface. It
Prints the material reject notes. This function makes use of a
Processing Option Set, which can be created via a call to
ProcessingOptionSet.Create(), and cleaned up after use, via a
Call to ProcessingOptionSet.Delete().
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory, must be
in iSite).
iMaterialLine           Material Position Line (Mandatory).
iItem                   Item (Mandatory).
iQuantity               Quantity to be moved to Quarantine. If
iSerialToQuarantine is not empty,
iQuantityToQuarantine must be 1.0.
(Mandatory).
iSerial                 The serial number of the Material to be
moved to Quarantine (Optional).
iUnit                   Effectivity Unit (Optional).
iLot                    Lot Code (Optional).
iQuarantineWarehouse    Warehouse for the Quarantine (Mandatory).
iQuarantineLocation     Quarantine location (Optional).
iQuarantineText         Quarantine text (Optional).
iDirectProcessInbound   Direct process Warehouse Order
(Optional).
iProcessingOptionSet    A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create().
If 0, then user default/session
default values are applied.
NAME                            TYPE                    DEFAULT
PrintReport                     tcyesno                 tcyesno.no
PrintingDevice                  domain tcmcs.str14      ""
PrintingFileoutPathAndName      domain tcmcs.str100     ""
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Material has been moved to Quarantine.
<> 0                    Material has not been moved to
Quarantine.
```
