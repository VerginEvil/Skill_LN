# OutboundOrderLineActivity.ModifyAutomaticProcessing

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLineActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1224-1226

```baan
DLL:   whextinhapi
This function is available from     2020.05 (KB2117931  ).
Syntax: long OutboundOrderLineActivity.ModifyAutomaticProcessing(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  whinh.prty       iProcedureType,
domain  tcmcs.st20m      iActivity mb,
domain  tcyesno          iAutomatic,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will update the automatic attribute of the
outbound order line activity that is provided. The automatic
field will only be updated if the activity is applicable and the
value of the automatic attribute is different than the value
passed in variable iAutomatic.
Depending on the order type certain activities can be set to
not applicable, and as a result the automatic flag cannot be
updated.
Pre:    db.retry.point should be set
Post:   commit or abort transaction depending on the return value.
Input:  iOrderOrigin                          - Mandatory
iOrderNumber                                  - Mandatory
iOrderLine                                    - Optional (inbound line can be 0)
iOrderSequence                                - Optional (inbound sequence can be 0)
iProcedureType                                - Mandatory
Allowed Values:
Outbound Procedure
(whinh.prty.issue.advice)
Shipment Procedure
(whinh.prty.issue.shipment)
iActivity                                     - Mandatory
Allowed Values:
The values are depending on the
procedure type.
Outbound Procedure:
"whinh4201m000"                                                       -
Generate Outbound Advice
"whinh4202m000"                                                       -
Release Outbound Advice
"whinh4415m000"                                                       -
Print Picking List
"whinh4525m100"                                                       -
Confirm Picking List
Shipment Procedure:
"whinh4275m001"                                                       -
Freeze Shipment
"whinh4275m000"                                                       -
Confirm Shipment
"whinh4470m000"                                                       -
Print Bills of Lading
"whinh4475m000"                                                       -
Print Packing Slip
"whinh4476m000"                                                       -
Print Packing List
"whinh4477m000"                                                       -
Print Delivery Notes
"whinh4478m000"                                                       -
Print Shipping Manifest
"whinh4279m000"                                                       -
Print Pro Forma Invoice
iAutomatic                                    - Mandatory
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```

## Public Interfaces for OutboundOrderLine

The following functions are available: OutboundOrderLine.Cancel OutboundOrderLine.CreateAdvice OutboundOrderLine.CreateAdviceV2 OutboundOrderLine.StartAutomaticOutboundProcessing OutboundOrderLine.StatusOverviewStartDetail OutboundOrderLine.StatusOverviewStartOverview OutboundOrderLine.UndoAdvice OutboundOrderLine.UndoCancel OutboundOrderLine.UndoRelease
