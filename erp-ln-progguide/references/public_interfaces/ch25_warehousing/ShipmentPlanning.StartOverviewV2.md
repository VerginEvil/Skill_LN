# ShipmentPlanning.StartOverviewV2

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1315-1317

```baan
DLL:   whextinhapi
This function is available from     2026.09 (KB3691656  ).
Syntax: long ShipmentPlanning.StartOverviewV2(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  whinh.oorg       oOrderOrigin,
ref     domain  tcorno           oOrder,
ref     domain  tcpono           oOrderLine,
ref     domain  tcpono           oOrderSequence,
ref     domain  tcmcs.long       oDistributionSequence,
ref     domain  tcdate           oCreationDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts session Outbound Line - Shipment Planning
Requirements (whinh4183m000) This session can be started in
multi occ only.
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not in use
iSessionIndex
Not in use
iQueryExtend
A specific query to be used when zooming to this session.
Using the query extend may lead to a "data not found,
session not started" situation. (Optional)
iOrderOrigin
The Order Origin to be started (Mandatory).
iOrderNumber
The Order Number to be started (Mandatory).
iOrderLine
The Order Line to be started. (Mandatory)
iOrderSequence
The Order Sequence to be started. (Mandatory)
Output: for iStartMode MODAL:
oOrderOrigin                                  - Selected Order Origin
oOrder                                        - Selected Order
oOrderLine                                    - Selected Order Line
oOrderSequence                                - Selected Order Line Sequence
oDistributionSequence                         - Selected Distribution Sequence
oCreationDate                                 - Selected Creation Date
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Chapter 26 Public Interfaces for Freight

## Public Interfaces for FreightOrderCluster

The following functions are available: FreightOrderCluster.ConfirmDelivery
