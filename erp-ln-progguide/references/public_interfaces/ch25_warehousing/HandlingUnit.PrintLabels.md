# HandlingUnit.PrintLabels

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1054-1057

```baan
DLL:   whextwmdapi
This function is available from 2025.06 (KB3560682).
Syntax: long HandlingUnit.PrintLabels(
domain  whhuid           iHandlingUnit,
domain  whwmd.lbpb       iLabelPrintedBy,
domain  tclabl           iLabelLayout,
domain  tcmcs.str15      iLabelDevice,
domain  tcmcs.long       iNumberOfCopies,
domain  whwmd.lbpr       iPrintOption,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface prints handling unit labels.
The ranges can be based upon order activities or can be related
to handling units.
The ranges can be defined in the iProcessingOptionSet.
The layouts of these labels are defined in session
"Label Layouts" (whwmd5520m000).
Within the label layout the user can define several label fields
which are process dependent, a certain label field can contain
a different value within multiple processes.
The table fields in the layout are defined with the aid
of variables preceded by hashes (#).
The table fields/variables are replaced by the value of the
table fields.
See LN Documentation, topic Label Fields and Expressions
for the possible fields.
Opening/Closing of the report is handled by this function.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iHandlingUnit - Handling Unit Id (Optional).
If iHandlingUnit is filled then iProcessingOptionSet will
be ignored.
iLabelPrintedBy - Label printed By Infor LN or External
application. (Mandatory)
iLabelLayout - Label Layout (Mandatory if iLabelPrintedBy =
Infor LN)
iLabelDevice - Label Device (Mandatory)
iNumberOfCopies - Number of Copies (Mandatory)
iPrintOption - Print option indicator for Handling Unit Labels
only. Range or Structure. (Mandatory)
iProcessingOptionSet Optional, if 0, the default options
are applied.
Processing Options have a direct relationship with the form fields
on session Print Labels (whwmd5430m100) and are not explained in
further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                    TYPE                    DEFAULT
HandlingUnitFrom        domain whhuid           Minimum Value
HandlingUnitTo          domain whhuid           Maximum Value
ShipFromTypeFrom        domain tctyps           Minimum Value
ShipFromCodeFrom        domain tccshp           Minimum Value
ShipFromTypeTo          domain tctyps           Maximum Value
ShipFromCodeTo          domain tccshp           Maximum Value
ShipToTypeFrom          domain tctyps           Minimum Value
ShipToCodeFrom          domain tccshp           Minimum Value
ShipToTypeTo            domain tctyps           Maximum Value
ShipToCodeTo            domain tccshp           Maximum Value
OwnerFrom               domain tccom.bpid       Minimum Value
OwnerTo                 domain tccom.bpid       Maximum Value
InboundOrder            domain tcyesno          tcyesno.no
InboundOrderOriginFrom  domain whinh.oorg       Minimum Value
InboundOrderOriginTo    domain whinh.oorg       Maximum Value
InboundOrderOriginFrom  domain whinh.oorg       Minimum Value
InboundOrderOriginTo    domain whinh.oorg       Maximum Value
InboundOrderLineFrom    domain tcpono           Minimum Value
InboundOrderLineTo      domain tcpono           Maximum Value
OutboundOrder           domain tcyesno          tcyesno.no
OutboundOrderOriginFrom domain whinh.oorg       Minimum Value
OutboundOrderOriginTo   domain whinh.oorg       Maximum Value
OutboundOrderOriginFrom domain whinh.oorg       Minimum Value
OutboundOrderOriginTo   domain whinh.oorg       Maximum Value
OutboundOrderLineFrom   domain tcpono           Minimum Value
OutboundOrderLineTo     domain tcpono           Maximum Value
AdjustmentOrder         domain tcyesno          tcyesno.no
AdjustmentOrderFrom     domain tcorno           Minimum Value
AdjustmentOrderTo       domain tcorno           Maximum Value
CycleCountOrder         domain tcyesno          tcyesno.no
CycleCountOrderFrom     domain tcorno           Minimum Value
CycleCountOrderTo       domain tcorno           Maximum Value
Inspection              domain tcyesno          tcyesno.no
InspectionFrom          domain tcorno           Minimum Value
InspectionTo            domain tcorno           Maximum Value
InspectionSequenceFrom  domain tcpono           Minimum Value
InspectionSequenceTo    domain tcpono           Maximum Value
ShipmentNotice          domain tcyesno          tcyesno.no
ShipFromBPFrom          domain tccom.bpid       Minimum Value
ShipFromBPTo            domain tccom.bpid       Maximum Value
ShipmentNoticeFrom      domain whinh.shpm       Minimum Value
ShipmentNoticeTo        domain whinh.shpm       Maximum Value
ShipmentNoticeLineFrom  domain tcpono           Minimum Value
ShipmentNoticeLineTo    domain tcpono           Maximum Value
Receipt                 domain tcyesno          tcyesno.no
ReceiptFrom             domain whinh.shpm       Minimum Value
ReceiptTo               domain whinh.shpm       Maximum Value
ReceiptLineFrom         domain tcpono           Minimum Value
ReceiptLineTo           domain tcpono           Maximum Value
InboundAdvice           domain tcyesno          tcyesno.no
InboundAdviceFrom       domain tcorno           Minimum Value
InboundAdviceTo         domain tcorno           Maximum Value
InboundAdviceLineFrom   domain tcpono           Minimum Value
InboundAdviceLineTo     domain tcpono           Maximum Value
InboundInspection       domain tcyesno          tcyesno.no
InboundInspectionFrom   domain tcorno           Minimum Value
InboundInspectionTo     domain tcorno           Maximum Value
OutboundAdvice          domain tcyesno          tcyesno.no
OutboundAdviceOrderOriginFrom   domain whinh.oorg       Minimum Value
OutboundAdviceOrderOriginTo     domain whinh.oorg       Maximum Value
OutboundAdviceOrderFrom         domain tcorno           Minimum Value
OutboundAdviceOrderTo           domain tcorno           Maximum Value
OutboundAdviceOrderSetFrom      domain tcsern           Minimum Value
OutboundAdviceOrderSetTo        domain tcsern           Maximum Value
OutboundAdviceOrderLineFrom     domain tcpono           Minimum Value
OutboundAdviceOrderLineTo       domain tcpono           Maximum Value
OutboundAdviceOrderSequenceFrom domain tcpono           Minimum Value
OutboundAdviceOrderSequenceTo   domain tcpono           Maximum Value
OutboundAdviceFrom      domain tcpono           Minimum Value
OutboundAdviceTo        domain tcpono           Maximum Value
OutboundInspection      domain tcyesno          tcyesno.no
OutboundInspectionFrom  domain tcorno           Minimum Value
OutboundInspectionTo    domain tcorno           Maximum Value
Shipment                domain tcyesno          tcyesno.no
ShipmentFrom            domain whinh.shpm       Minimum Value
ShipmentTo              domain whinh.shpm       Maximum Value
ShipmentLineFrom        domain tcpono           Minimum Value
ShipmentLineTo          domain tcpono           Maximum Value
LoadFrom                domain whinh.load       Minimum Value
LoadTo                  domain whinh.load       Maximum Value
ContainerFrom           domain whinh.cntr       Minimum Value
ContainerTo             domain whinh.cntr       Maximum Value
HandlingUnitArray       domain ttjson           0
Possible values of ReportNumber is 1.
JSON Object HandlingUnitArray has the following structure:
"HandlingUnitArray": [
{
"HandlingUnit": "HU100"
},
{
"HandlingUnit": "HU200"
}
]
This structure can be created with the following code:
HandlingUnitArray = Json.newArray()
HandlingUnit = Json.newObject()
Json.setString(HandlingUnit, "HandlingUnit", "HU100")
Json.add(HandlingUnittArray, HandlingUnit)
HandlingUnit = Json.newObject()
Json.setString(HandlingUnit, "HandlingUnit", "HU200")
Json.add(HandlingUnitArray, HandlingUnit)
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
