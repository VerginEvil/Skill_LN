# InboundOrderLine.Receive

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1081-1082

```baan
DLL:   whextinhapi
This function is available from     2021.03 (KB2175828  ).
Syntax: long InboundOrderLine.Receive(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  whinh.shpm       iReceipt,
domain  tcqst1           iReceivedQuantity,
domain  tccuni           iReceivedUnit,
domain  tcpksp           iPackingSlip mb,
domain  tcqst1           iPackingSlipQuantity,
domain  tccuni           iPackingSlipUnit,
domain  whinh.load       iLoad,
domain  whinh.shpm       iShipment,
domain  tcclot           iLot,
boolean          iGenerateLot,
boolean          iGenerateSerial,
ref     domain  whinh.shpm       oReceipt,
ref             long             oNumberOfReceiptLines,
ref     domain  tcpono           oReceiptLineArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will allow an inbound line to be received,
making one or multiple new receipt lines.
When the iReceipt is passed as empty, a new Receipt Header will
be created. There can be multiple receipt lines generated based
on the setup related to Receipt Line Consolidation in
combination with the stock points that are to be received.
This function will also have the option to automatically
generate lot and/or serial numbers during the receipt line
creation.
Pre:    db.retry.point must be set
oReceiptLineArray must be declared as a based variable, this
function will allocate the memory.
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
After the oReceiptLineArray is used, free the memory.
Input:  Start Order Line Key Fields
iOrderOrigin                                  - Order Origin - Mandatory
iOrderNumber                                  - Order Number - Mandatory
iOrderLine                                    - Order Line - Optional
iOrderSequence                                - Order Sequence - Optional
End Order Line Key Fiels                       - The order line should exist and will
be validated prior to receiving is
done.
iReceipt                                      - Receipt header on which lines must be
added.
Optional, if empty a new receipt
header will be created.
iReceivedQuantity                             - Received Quantity - Mandatory
iReceivedUnit                                 - Received Unit - Mandatory
iPackingSlip                                  - Packing Slip - Optional
iPackingSlipQuantity                          - Packing Slip Quantity - Optional
iPackingSlipUnit                              - Packing Slip Unit -   Mandatory when
iPackingSlipQuantity
is filled
iLoad                                         - Load - Optional
iShipment                                     - Shipment - Optional
iLot                                          - Received Lot - Optional
iGenerateLot                                  - Generate Lot when item is lot
controlled
-                                                       Mandatory
iGenerateSerial                               - Generate Serial when item is
serialized
-                                                       Mandatory
Output: oReceipt                              - Receipt that is created (or populated
with the iReceipt when iReceipt is
filled)
oNumberOfReceiptLines                         - Number of receipt lines that are
created.
oReceiptLineArray                             - Receipt lines that are created.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
