# ShipmentLineStockPointDetails.StartOverview

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentLineStockPointDetail
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1183-1184

```baan
DLL:   whextinhapi
This function is available from 2023.02 (KB2280145).
Syntax: long ShipmentLineStockPointDetails.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  tcpono           iBomLine,
domain  tcmcs.long       iDistributionSequence,
ref     domain  whinh.shpm       oShipment,
ref     domain  tcpono           oShipmentLine,
ref     domain  tcpono           oBomLine,
ref     domain  tcmcs.long       oDistributionSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl    This function starts the overview session Shipment Line Stock
Point Details (whinh4133m000).
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
Not Used.
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
iShipment
The Shipment to be started
Mandatory if iStartMode = MODELESS
iShipmentLine
The Shipment Line to be started
Mandatory if iStartMode = MODELESS
iBomLine
Optional
iDistributionSequence
Optional
Output: for iStartMode MODAL:
oShipment               - selected shipment
oShipmentLine           - selected shipment line
oBomLine                - selected bom line
oDistributionSequence   - selected distribution sequence
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Session started
<> 0                    - Error.
```
