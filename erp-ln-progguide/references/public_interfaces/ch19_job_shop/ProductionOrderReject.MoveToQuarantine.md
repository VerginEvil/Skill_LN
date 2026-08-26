# ProductionOrderReject.MoveToQuarantine

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderReject
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 807-808

```baan
DLL:   tiextsfcapi
This function is available from     2020.07 (KB2135601  ).
Syntax: long ProductionOrderReject.MoveToQuarantine(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tiqep2           iQuantity,
ref     domain  tcibd.sern       iSerialArray() fixed,
domain  tccwar           iQuarantineWarehouse,
domain  tiloca           iWarehouseLocation,
domain  tcuef.effn       iEffectivityUnit,
domain  tcclot           iLotCode,
domain  tcorno           iNCMReport,
domain  tctxtn           iTextNumber,
const           string           iTextString(),
domain  tcyesno          iDirectProcessInbound,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function moves a rejected end item quantity of a
production order operation to a quarantine warehouse,
as in session tisfc0209m000.
Retry point and commit / abort transaction are
executed within this Public Interface.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iOperation              Operation (mandatory).
iQuantity               Quantity (mandatory).
iSerialArray            Array of Serial Numbers.
Pass a filled array (static
or dynamic) when the main item is
serialized and serial numbers are required;
the length of the array must equal i.quantity.
Pass an empty array variable when the main
item is not serialized. E.g. pass
the variable dummy.serials, which is
defined as:
domain tcibd.sern dummy.serials(1)
iQuarantineWarehouse    The warehouse to which the quarantined
end item quantity is sent (mandatory).
iWarehouseLocation      Location in iQuarantineWarehouse
(optional).
iEffectivityUnit        Effectivity Unit (optional).
iLotCode                An existing Lot code (mandatory for
lot controlled items)
iNCMReport              The  non                      -conformance material report
to be updated (optional)
iTextNumber             Text number (optional) which will
be copied into a new text and linked
to the Production Warehouse Order.
iTextString             Text string (optional) that will stored
as Text Number and linked
to the Production Warehouse Order.
Must be empty when iText is filled
and vice versa.
iDirectProcessInbound   If Yes, then the inbound procedure
will be executed automatically.
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Reject is moved to quarantine
<> 0                    Reject could not be moved to quarentine.
```
