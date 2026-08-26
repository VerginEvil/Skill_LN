# DeliveryNote.StartMultiMain

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for DeliveryNote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1139-1141

```baan
DLL:   whextinhapi
This function is available from     2024.01 (KB2317691  ).
Syntax: long DeliveryNote.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  whinh.shpm       iPreliminaryDeliveryNote,
domain  tcdeln           iDeliveryNote,
domain  whinh.load       iLoad,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the multi main table session
Delivery Notes (whinh4635m000).
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
Not Used.
iSessionIndex
Specifies the table index that is to be used.
iQueryExtend
A specific query to be used when zooming to this session.
iPreliminaryDeliveryNote
Preliminary Delivery Note
(mandatory if iSessionIndex=1)
iDeliveryNote
Delivery Note
(mandatory if iSessionIndex=2)
iLoad   Load
(mandatory if iSessionIndex=3)
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

## Public Interfaces for Shipment

The following functions are available: Shipment.Confirm Shipment.ConfirmASN Shipment.Freeze Shipment.GenerateHandlingUnit Shipment.MoveToLoad Shipment.NotifyAutomaticOutboundProcess Shipment.PrintLabelsByPackageLabelBOD Shipment.PrintPackingList Shipment.PrintPackingSlip Shipment.PrintPickAndLoadSheet Shipment.ProcessInvoice Shipment.RecalculateWeight Shipment.Reopen Shipment.StartAutomaticOutboundProcessing Shipment.StartDetail Shipment.StartMultiMain Shipment.StartOverview Shipment.StartPrintPickAndLoadSheet
