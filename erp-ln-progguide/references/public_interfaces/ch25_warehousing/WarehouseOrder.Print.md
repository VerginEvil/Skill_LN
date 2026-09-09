# WarehouseOrder.Print

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1028-1030

```baan
DLL:   whextinhapi
This function is available from 2026.09 (KB3687883).
Syntax: long WarehouseOrder.Print(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataPrinted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will print the Warehouse orders for
the i.order.origin, i.order.number, i.order.line and
i.order.sequence using the defaults or options as provided in
the iProcessingOptionSet.
Opening/Closing of the report is handled by this function.
Input:  iOrderOrigin            Optional, ignored if iOrderNumber is
empty.
iOrderNumber            Optional
iOrderLine              Optional, ignored if iOrderNumber is
empty.
iOrderSequence          Optional, ignored if iOrderNumber is
empty.
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
Processing Options have a direct relationship with the form fields
on session Print Warehousing Orders (whinh2400m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
OrderOrigin                     domain whinh.oorg       empty
OrderNumber                     domain tcorno           Empty String
OrderLine                       domain tcpono           0
OrderSequence                   domain tcpono           0
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
TransactionTypeFrom             domain whinh.ittp       Minimum Value
TransactionTypeTo               domain whinh.ittp       Maximum Value
CarrierFrom                     domain tccfrw           Minimum Value
CarrierTo                       domain tccfrw           Maximum Value
RouteFrom                       domain tccrte           Minimum Value
RouteTo                         domain tccrte           Maximum Value
ShipToAddressFrom               domain tccom.cadr       Minimum Value
ShipToAddressTo                 domain tccom.cadr       Maximum Value
PlannedDeliveryDateFrom         domain tcdate           Minimum Value
PlannedDeliveryDateTo           domain tcdate           Maximum Value
ShipFromTypeFrom                domain tctyps           Minimum Value
ShipFromTypeTo                  domain tctyps           Maximum Value
ShipToTypeFrom                  domain tctyps           Minimum Value
ShipToTypeTo                    domain tctyps           Maximum Value
ShipFromCodeFrom                domain tccshp           Minimum Value
ShipFromCodeTo                  domain tccshp           Maximum Value
ShipToCodeFrom                  domain tccshp           Minimum Value
ShipToCodeTo                    domain tccshp           Maximum Value
ShipFromLocationFrom            domain whloca           Minimum Value
ShipFromLocationTo              domain whloca           Maximum Value
ShipToLocationFrom              domain whloca           Minimum Value
ShipToLocationTo                domain whloca           Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
AttributeSetFrom                domain tcatse           Minimum Value
AttributeSetTo                  domain tcatse           Maximum Value
PrintHeaders                    domain tcyesno          tcyesno.yes
PrintHeaderDetails              domain tcyesno          tcyesno.yes
PrintHeaderWithoutLines         domain tcyesno          tcyesno.yes
PrintHeaderLandedCosts          domain tcyesno          tcyesno.no
PrintHeaderText                 domain tcyesno          tcyesno.yes
PrintLines                      domain tcyesno          tcyesno.yes
PrintLineDetails                domain tcyesno          tcyesno.yes
PrintPegDistribution            domain tcyesno          tcyesno.yes
PrintLineLandedCosts            domain tcyesno          tcyesno.no
PrintLineText                   domain tcyesno          tcyesno.yes
PrintInboundAdvice              domain tcyesno          tcyesno.yes
PrintInboundAdviceDetails       domain tcyesno          tcyesno.yes
PrintOutboundAdvice             domain tcyesno          tcyesno.yes
PrintOutboundAdviceDetails      domain tcyesno          tcyesno.yes
PrintHeaderActivities           domain tcyesno          tcyesno.no
PrintLineActivities             domain tcyesno          tcyesno.no
OrderLineArray                  domain ttjson           0
ReportNumber                    domain tcmcs.long       0
ReportName                      domain tcmcs.str16      Empty String
JSON Object OrderLineArray has the following structure:
"OrderLineArray": [
{
"OrderOrigin": 80,
"OrderNumber": "PUR000030",
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
OrderLineArray = Json.newArray()
OrderLine = Json.newObject()
Json.setNumber(OrderLine, "OrderOrigin", 80)
Json.setString(OrderLine, "OrderNumber", "PUR000030")
Json.setNumber(OrderLine, "OrderLine", 10)
Json.setNumber(OrderLine, "OrderSequence", 1)
Json.add(OrderLineArray, OrderLine)
OrderLine = Json.newObject()
Json.setNumber(OrderLine, "OrderOrigin", 50)
Json.setString(OrderLine, "OrderNumber", "JSC000012")
Json.setNumber(OrderLine, "OrderLine", 10)
Json.setNumber(OrderLine, "OrderSequence", 1)
Json.add(OrderLineArray, OrderLine)
ReportName only needs to filled for customized reports, otherwise
the report related to the SortOption is automatically used.
ReportName must start with an "r", e.g. "rwhinh240011000"
Output: o.data.printed  - true:  Order Printed.
false: Nothing Printed.
Return: 0: OK, <> 0: Error
```
