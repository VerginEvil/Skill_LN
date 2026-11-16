# HandlingUnit.Receive

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1057-1058

```baan
DLL:   whextinhapi
This function is available from 2022.01 (KB2217879).
Syntax: long HandlingUnit.Receive(
domain  whhuid           iHandlingUnit,
domain  whinh.shpm       iReceipt,
domain  tcpksp           iPackingSlip mb,
domain  whinh.load       iLoad,
domain  whinh.shpm       iShipment,
ref     domain  whinh.shpm       oReceipt,
ref             long             oNumberOfReceiptLines,
ref     domain  tcpono           oReceiptLineArray(),
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will receive the given handling unit.
Pre:    db.retry.point must be set
oReceiptLineArray must be declared as a based variable, this
function will allocate the memory.
Post:   Commit the transaction in case of success
Abort the transaction in case of failure
After the oReceiptLineArray is used, free the memory.
Input:  iHandlingUnit           - Mandatory
iReceipt                - Receipt header on which lines must be
added.
Optional, if empty a new receipt
header will be created.
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
