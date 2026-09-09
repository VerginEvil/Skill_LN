# ShipmentNotice.ReceiveDirectDelivery

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ShipmentNotice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1013-1013

```baan
DLL:   whextinhapi
This function is available from 2021.11 (KB2210894).
Syntax: long ShipmentNotice.ReceiveDirectDelivery(
domain  tccom.bpid       iShipFromBusinessPartner,
domain  whinh.shpm       iShipment,
ref             long             oNumberOfLinesReceived,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function executes option Receive Direct Delivery
for the given Shipment Notice (ASN).
This is allowed if:
- The ASN header exists with status Scheduled or
Scheduled (Manually), and
- If Header status is Scheduled, at least one ASN Line(s) exist
with approval status unequal to Approved
- The security settings by Warehouse allows usage, and
- ASN Line(s) having Direct Delivery Line(s) exist
Be aware that transaction management is handled within this
function.
This function informs Order Management Purchase of any
receipts that are made in Warehousing. As soon as this
notification is given, Purchase can continue with any
automatic processing of the order/schedule line that is required.
Pre:    n.a.
Post:   n.a.
Input:  iShipFromBusinessPartner- Ship-from Business Partner (Mandatory)
iShipment               - Shipment (Mandatory)
Output: oNumberOfLinesReceived  - Number of received Shipment Notice
Lines, having a direct delivery line.
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
