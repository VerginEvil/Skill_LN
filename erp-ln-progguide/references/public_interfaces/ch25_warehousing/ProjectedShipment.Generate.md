# ProjectedShipment.Generate

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for ProjectedShipment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1174-1177

```baan
DLL:   whextinhapi
This function is available from     2025.09 (KB3613618  ).
Syntax: long ProjectedShipment.Generate(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  whinh.gnps       iAction,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will (re-)generate or delete one or
more projected shipments using the defaults or options as
provided in the iProcessingOptionSet.
In case iOrderNumber is filled then the following options
of the iProcessingOptionSet will be ignored:
-                       selection range fields (From/To)
-                       OutboundOrderLineArray
The projected shipments will then be (re                      -)generated or deleted
for the given iOrderOrigin, iOrderNumber, iOrderLine and
iOrderSequence.
In case option OutboundOrderLineArray is set then the
selection range fields (From/To) of the iProcessingOptionSet
will be ignored. The projected shipments will then be
(re                      -)generated or deleted for the outbound order lines in the
array.
Opening/Closing of the report is handled by this function.
Pre:    By default the transaction handling is done within this
function, so there should be no pending logical transaction
before calling this function.
This is not the case when IncludeTransactionHandling
(option of iProcessingOptionSet) is set to False.
Post:   By default the transaction handling is done within this
function, so there is no need to commit or abort the process.
That is handled within the function.
When IncludeTransactionHandling (option of iProcessingOptionSet)
is set to False then the calling process has to handle
abort/commit of the process.
Input:  iOrderOrigin            Mandatory
iOrderNumber            Optional
iOrderLine              Optional
iOrderSequence          Optional
iAction                 Mandatory
iDevice                 Mandatory, unless options PrintShipments
and PrintErrors are set to tcyesno.no.
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Generate Projected Shipments (whinh4230m200) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
OrderOriginFrom                 domain whinh.oorg       Minimum Value
OrderOriginTo                   domain whinh.oorg       Maximum Value
OrderNumberFrom                 domain tcorno           Minimum Value
OrderNumberTo                   domain tcorno           Maximum Value
OrderSetFrom                    domain tcwset           Minimum Value
OrderSetTo                      domain tcwset           Maximum Value
OrderLineFrom                   domain tcpono           Minimum Value
OrderLineTo                     domain tcpono           Maximum Value
OrderSequenceFrom               domain tcpono           Minimum Value
OrderSequenceTo                 domain tcpono           Maximum Value
DistributionSequenceFrom        domain tcmcs.long       Minimum Value
DistributionSequenceTo          domain tcmcs.long       Maximum Value
DeliveryDateFrom                domain tcdate           Minimum Value
DeliveryDateTo                  domain tcdate           Current Date/Time
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
ShipToTypeFrom                  domain tctyps           Minimum Value
ShipToTypeTo                    domain tctyps           Maximum Value
ShipToCodeFrom                  domain tcshpm           Minimum Value
ShipToCodeTo                    domain tcshpm           Maximum Value
ShipToAddressFrom               domain tccom.cadr       Minimum Value
ShipToAddressTo                 domain tccom.cadr       Maximum Value
RouteFrom                       domain tccrte           Minimum Value
RouteTo                         domain tccrte           Maximum Value
CarrierFrom                     domain tccfrw           Minimum Value
CarrierTo                       domain tccfrw           Maximum Value
ShipmentReferenceFrom           domain tcrefs           Minimum Value
ShipmentReferenceTo             domain tcrefs           Maximum Value
ReferenceFrom                   domain tcrefa           Minimum Value
ReferenceTo                     domain tcrefa           Maximum Value
JobSequenceFrom                 domain tcmcs.str30      Minimum Value
JobSequenceTo                   domain tcmcs.str30      Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
PrintShipments                  domain tcyesno          tcyesno.yes
PrintErrors                     domain tcyesno          tcyesno.yes
IncludeTransactionHandling      boolean                 true
OutboundOrderLineArray          domain ttjson           0
ReportName                      domain tcmcs.str16      Empty String
JSON Object OutboundOrderLineArray has the following structure:
"OutboundOrderLineArray": [
{
"OrderOrigin": 1,
"OrderNumber": "SLS000030",
"OrderLine": 10,
"OrderSequence": 0
},
{
"OrderOrigin": 50,
"OrderNumber": "JSC000012",
"OrderLine": 20,
"OrderSequence": 0
}
]
This structure can be created with the following code:
OutboundOrderLineArray = Json.newArray()
OutboundOrderLine = Json.newObject()
Json.setNumber(OutboundOrderLine, "OrderOrigin", 1)
Json.setString(OutboundOrderLine, "OrderNumber", "SLS000030")
Json.setNumber(OutboundOrderLine, "OrderLine", 10)
Json.setNumber(OutboundOrderLine, "OrderSequence", 1)
Json.add(OutboundOrderLineArray, OutboundOrderLine)
OutboundOrderLine = Json.newObject()
Json.setNumber(OutboundOrderLine, "OrderOrigin", 50)
Json.setString(OutboundOrderLine, "OrderNumber", "JSC000012")
Json.setNumber(OutboundOrderLine, "OrderLine", 10)
Json.setNumber(OutboundOrderLine, "OrderSequence", 1)
Json.add(OutboundOrderLineArray, OutboundOrderLine)
ReportName only needs to filled for customized reports, otherwise
the default report is automatically used.
ReportName must start with an "r", e.g. "rwhinh423011001"
Output: oDataProcessed                        - true:  Projected Shipment(s)
(Re                                                       -)Generated/Deleted.
false: Nothing is processed.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error.
```
