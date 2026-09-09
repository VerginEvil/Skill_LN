# HandlingUnit.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1064-1065

```baan
DLL:   whextwmdapi
This function is available from 2025.07 (KB3572724).
Syntax: long HandlingUnit.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcitem           iItem,
domain  whhuid           iHandlingUnit,
domain  tccwar           iWarehouse,
domain  whloca           iLocation,
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
ref             long             oNumberHandlingUnits,
ref     domain  whhuid           oHandlingUnitsArray() fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Handling Units
(whwmd5130m000).
Handling units can be selected in this session and returned
to the calling function.
Maximum length of output array is 30.
Pre:    oHandlingUnitArray must be declared as based array.
Post:   NA
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not used
iSessionIndex
Specifies the session index that is to be used.
0 - No index specified
1 - By Handling Unit
3 - By Item
4 - By Parent Handling Unit
5 - By Warehouse
6 - By Receipt
7 - By Inspection
8 - By Shipment
iQueryExtend
A specific query to be used when zooming to this session.
iItem           - Mandatory if iSessionIndex = 3
iHandlingUnit   - Mandatory if iSessionIndex = 1 or 4
iWarehouse      - Mandatory if iSessionIndex = 5
iLocation       - Optional
iReceipt        - Mandatory if iSessionIndex = 6
iReceipt.line   - Optional
iInspection     - Mandatory if iSessionIndex = 7
iInspectionSequence
- Optional
iShipment       - Mandatory if iSessionIndex = 8
iShipment.line  - Optional
Output: oNumberHandling.units   - Number of handling units in array.
(maximum value is 30)
oHandlingUnitsArray     - Array with handling units.
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0     Session started
<> 0: Error
```
