# WarehouseOrderLine.ActivityIsMandatory

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1286-1287

```baan
DLL:   whextinhapi
This function is available from     2023.09 (KB2304607  ).
Syntax: long WarehouseOrderLine.ActivityIsMandatory(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  whinh.prty       iProcedureType,
domain  tcmcs.str20m     iActivity mb,
ref             boolean          oActivityMandatory,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface checks if an activity is mandatory for
a warehouse order line.
Pre:    N.a.
Post:   N.a.
Input:  iOrderOrigin               - Order Origin (Mandatory)
iOrder                       - Order (Mandatory)
iOrderLine                       - Order Line
iOrderSequence                       - Order Sequence
iProcedureType                       - Procedure Type (Mandatory)
Allowed Values:
Inbound Procedure (whinh.prty.receipt.line)
Inspection Procedure (whinh.prty.receipt.isnpect)
Outbound Procedure (whinh.prty.issue.advice)
Shipment Procedure (whinh.prty.issue.shipment)
iActivity                       - Activity (Mandatory)
Allowed Values:
The values are depending on the procedure type.
Receipt Procedure:
"whinh3412m100"                                       - Print Goods Received Note
"whinh3512m000"                                       - Warehouse Receipts
"whinh3201m000"                                       - Generate Inbound Advice
"whinh3415m000"                                       - Generate Storage List
"whinh3525m100"                                       - Confirm Storage List
"whinh3203m000"                                       - Putaway Inbound Advice
Inspection Procedure:
"whinh3201m000"                                       - Generate Inbound Advice
"whinh3415m000"                                       - Generate Storage List
"whinh3525m100"                                       - Confirm Storage List
"whinh3203m000"                                       - Putaway Inbound Advice
Outbound Procedure:
"whinh4201m000"                                       - Generate Outbound Advice
"whinh4202m000"                                       - Release Outbound Advice
"whinh4415m000"                                       - Print Picking List
"whinh4525m100"                                       - Confirm Picking List
Shipment Procedure:
"whinh4275m001"                                       - Freeze Shipment
"whinh4275m000"                                       - Confirm Shipment
"whinh4470m000"                                       - Print Bills of Lading
"whinh4475m000"                                       - Print Packing Slip
"whinh4476m000"                                       - Print Packing List
"whinh4477m000"                                       - Print Delivery Notes
"whinh4478m000"                                       - Print Shipping Manifest
"whinh4279m000"                                       - Print Pro Forma Invoice
Output: oActivityMandatory               - Activity Mandatory Indicator
oExceptionMessage                       - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID                       - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0                     - No Error
<> 0                          - Error
```
