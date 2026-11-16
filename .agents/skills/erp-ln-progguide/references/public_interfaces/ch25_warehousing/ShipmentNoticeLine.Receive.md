# ShipmentNoticeLine.Receive

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentNoticeLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1018-1019

```baan
DLL:   whextinhapi
This function is available from 2022.01 (KB2217879).
Syntax: long ShipmentNoticeLine.Receive(
domain  tccom.bpid       iShipFromBusinessPartner,
domain  whinh.shpm       iShipmentNotice,
domain  tcpono           iShipmentNoticeLine,
domain  whinh.shpm       iReceipt,
domain  tcqst1           iReceivedQuantity,
domain  tccuni           iReceivedUnit,
domain  tcpksp           iPackingSlip mb,
domain  whinh.load       iLoad,
domain  whinh.shpm       iShipment,
ref     domain  whinh.shpm       oReceipt,
ref             long             oNumberOfReceiptLines,
ref     domain  tcpono           oReceiptLineArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes option Receive for the given
Shipment Notice Line.
Pre:    db.retry.point must be set
oReceiptLineArray must be declared as a based variable, this
function will allocate the memory.
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
After the oReceiptLineArray is used, free the memory.
Input:  iShipFromBusinessPartner- Ship-from Business Partner - Mandatory
iShipmentNotice         - Shipment Notice - Mandatory
iShipmentNoticeLine     - Shipment Notice Line - Mandatory
iReceipt                - Receipt header on which lines must be
added.
Optional, if empty a new receipt
header will be created.
iReceivedQuantity       - Received Quantity - Optional
Value should not be less then zero.
iReceivedUnit           - Received Unit - Mandatory if received
quantity is greater than zero).
iPackingSlip            - Packing Slip - Optional
iLoad                   - Load - Optional
iShipment               - Shipment - Optional
Output: oReceipt                - Receipt that is created (or populated
with the iReceipt when iReceipt is
filled)
oNumberOfReceiptLines   - Number of receipt lines that are
created.
oReceiptLineArray       - Receipt lines that are created.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
