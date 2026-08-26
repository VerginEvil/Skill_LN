# ShipmentNotice.StartMultiMain

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentNotice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1005-1006

```baan
DLL:   whextinhapi
This function is available from     2020.04 (KB2115522  ).
Syntax: long ShipmentNotice.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tccom.bpid       iShipFromBusinessPartner,
domain  whinh.shpm       iShipment,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the multi main table session
Shipment Notices (whinh3600m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, in case of a
multi                                              -occurrence the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Not Used.
iSessionIndex
Specifies the session index that is to be used.
iQueryExtend
iShipFromBusinessPartner
iShipment
Output: oExceptionMessage                     - The last message if any message is
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
