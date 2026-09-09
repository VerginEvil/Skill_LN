# WarehouseOrder.PrintLabelForActivity

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1030-1032

```baan
DLL:   whextinhapi
This function is available from 2022.02 (KB2217792).
Syntax: long WarehouseOrder.PrintLabelForActivity(
domain  whinh.prty       iProcedureType,
domain  tcmcs.st20m      iActivity mb,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  whinh.shpm       iShipmentNotice,
domain  tcpono           iShipmentNoticeLine,
domain  whinh.shpm       iReceipt,
domain  tcpono           iReceiptLine,
domain  tcpono           iBomLine,
domain  tcorno           iInboundAdvice,
domain  tcpono           iAdviceLine,
domain  tcpono           iBomLineSequence,
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrder,
domain  tcwset           iOrderSet,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcpono           iOutboundAdvice,
domain  whinh.shpm       iShipment,
domain  tcpono           iShipmentLine,
domain  whinh.plbs       iLabelPrinting,
domain  tclabl           iLabelLayout,
domain  whwmd.lbpb       iLabelPrintedBy,
domain  tcmcs.long       iNumberOfCopies,
domain  tcyesno          iHandlingUnitOnly,
domain  whinh.prmt       iPrintingMethod,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports printing of Labels for warehouse
order activities.
Pre:    db.retry.point().
Post:   abort/commit transaction.
Input:  iProcedureType  - Procedure Type (Mandatory)
Allowed Values:       Inbound Procedure
(whinh.prty.receipt.line)
Inspection Procedure
(whinh.prty.receipt.isnpect)
Outbound Procedure
(whinh.prty.issue.advice)
Shipment Procedure
(whinh.prty.issue.shipment)
iActivity       - Warehousing Activity (Mandatory)
Allowed Values:
The values are depending on the
procedure type.
Inbound Procedure
"whinh3101m000" - Shipment Notice - Lines
"whinh3512m000" - Receipts
"whinh3201m000" - Generate Inbound Advice
"whinh3203m000" - Put Away Inbound Advice
"whinh3415m000" - Print Storage List
"whinh3525m100" - Confirm Storage List
Inspection Procedure
"whinh3122m000" - Inspection
"whinh3201m000" - Generate Inbound Advice
"whinh3203m000" - Put Away Inbound Advice
"whinh3415m000" - Print Storage List
"whinh3525m100" - Confirm Storage List
Outbound Procedure:
"whinh4200m000" - Process Outbound Advice
"whinh4201m000" - Generate Outbound Advice
"whinh4202m000" - Release Outbound Advice
"whinh4415m000" - Print Picking List
"whinh4525m100" - Confirm Picking List
"whinh3122m000" - Inspection
Shipment Procedure:
"whinh4275m001" - Freeze Shipment
"whinh4275m000" - Confirm Shipment
Fields below are applicable when Activity = "whinh3101m000";
otherwise these fields will be ignored.
iShipFromBusinessPartner- Ship from BP (Mandatory)
iShipmentNotice         - Shipment Notice (Mandatory)
iShipmentNoticeLine     - Shipment Notice Line (Mandatory)
Fields below are applicable when Activity = "whinh3512m000";
otherwise these fields will be ignored.
iReceipt        - Receipt (Mandatory)
iReceiptLine    - Receipt Line (Mandatory)
iBomLine        - BOM Line (Optional)
Fields below are applicable when Activity = "whinh3201m000" or
"whinh3203m000" or "whinh3415m000" or "whinh3525m100";
otherwise these fields will be ignored.
iInboundAdvice  - Inbound Advice (Mandatory)
iAdviceLine     - Inbound Advice Line (Mandatory)
iBomLineSequence- BOM Line Sequence (Optional)
Fields below are applicable when Activity = "whinh3122m000";
otherwise these fields will be ignored.
iInspection     - Inspection (Mandatory)
iInspectionSequence
- Inspection Sequence (Mandatory)
iBomLineSequence- BOM Line Sequence (Optional)
Fields below are applicable when Activity = "whinh4200m000" or
"whinh4201m000" or "whinh4202m000" or "whinh4415m000" or
"whinh4525m100";
otherwise these fields will be ignored.
iOrderOrigin    - Order Origin (Mandatory)
iOrder          - Order (Mandatory)
iOrderSet       - Order Set (Optional)
iOrderLine      - Order Line (Optional)
iOrderSequence  - Order Sequence (Optional)
iOutboundAdvice - Outbound Advice Number (Mandatory)
Fields below are applicable when Activity = "whinh4275m001" or
"whinh4275m000";
otherwise these fields will be ignored.
iShipment       - Shipment (Mandatory)
iShipmentLine   - Shipment Line (Mandatory)
iLabelPrinting  - Print Labels setup (Mandatory)
Allowed Values:
whinh.plbs.overrule     Overrule Order Settings
whinh.plbs.order.settingsAccording Order Settings
The fields below are applicable when Print Labels Setup is on
Overrule Order Settings
iLabelLayout    - Label Layout (Mandatory if applicable)
iLabelPrintedBy - Label print by Infor LN or external
application (Mandatory)
iNumberOfCopies - Number of Copies (Mandatory if applicable)
iHandlingUnitOnly - Print labels only if handing units
are present for the activity.
(Mandatory)
iPrintingMethod - Printing Method
Allowed Values:
whinh.prtm.by.line - one label per line
whinh.prtm.by.unit - one label per unit
(Mandatory if applicable)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
