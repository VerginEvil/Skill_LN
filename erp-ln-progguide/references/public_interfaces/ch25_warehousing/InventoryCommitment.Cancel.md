# InventoryCommitment.Cancel

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 964-966

```baan
DLL:   whextinpapi
This function is available from 2026.07 (KB3676144).
Syntax: long InventoryCommitment.Cancel(
domain  whinp.corg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcmcs.str15      iDevice,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function cancels inventory commitments for the
iOrderOrigin, iOrderNumber and iOrderLine using the defaults
or options as provided in the iProcessingOptionSet.
Be aware that transaction management is handled within this
function.
Opening/Closing of the report is handled by this function.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iOrderOrigin            Mandatory
iOrderNumber            Optional
iOrderLine              Optional
iDevice                 Mandatory
iProcessingOptionSet    Optional, if 0, the default options
are applied.
A Processing Option Set can be created
via a call to function
ProcessingOptionSet.Create().
In case iOrderNumber is filled then the following options
of the iProcessingOptionSet will be ignored:
- selection range fields (From/To)
- OrderLineArray
The inventory commitments will then be canceled for the given
iOrderOrigin, iOrderNumber (and specific iOrderLine, if filled).
In case option OrderLineArray is set then the selection
range fields (From/To) of the iProcessingOptionSet will be
ignored.
The inventory commitments will then be canceled for the
order lines in the array.
Processing Options have a direct relationship with the form fields
on session Cancel Inventory Commitments (whinp2204m000) and are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Explanation about setting of defaults:
Minimum Value:  Minimum value of domain is taken as default value.
Maximum Value:  Maximum value of domain is taken as default value.
NAME                            TYPE                    DEFAULT
OrderOriginFrom                 domain whinp.corg       Minimum Value
OrderOriginTo                   domain whinp.corg       Maximum Value
SoldToBusinessPartnerFrom       domain tccom.bpid       Minimum Value
SoldToBusinessPartnerTo         domain tccom.bpid       Maximum Value
ShipToBusinessPartnerFrom       domain tccom.bpid       Minimum Value
ShipToBusinessPartnerTo         domain tccom.bpid       Maximum Value
OrderNumberFrom                 domain tcorno           Minimum Value
OrderNumberTo                   domain tcorno           Maximum Value
OrderLineFrom                   domain tcpono           Minimum Value
OrderLineTo                     domain tcpono           Maximum Value
OperationFrom                   domain tcopno           Minimum Value
OperationTo                     domain tcopno           Maximum Value
ProductionDateTo                domain tcutcm           Current Date/Time
PlannedDeliveryDateFrom         domain tcdate           Minimum Value
PlannedDeliveryDateTo           domain tcdate           Current Date/Time
RouteFrom                       domain tccrte           Minimum Value
RouteTo                         domain tccrte           Maximum Value
ProjectFrom                     domain tccprj           Minimum Value
ProjectTo                       domain tccprj           Maximum Value
WarehouseFrom                   domain tccwar           Minimum Value
WarehouseTo                     domain tccwar           Maximum Value
RentalOwnerCompanyFrom          domain tcncmp           Minimum Value
RentalOwnerCompanyTo            domain tcncmp           Maximum Value
RentalOwnerFrom                 domain tccwoc           Minimum Value
RentalOwnerTo                   domain tccwoc           Maximum Value
EffectivityUnitFrom             domain tcuef.effn       Minimum Value
EffectivityUnitTo               domain tcuef.effn       Maximum Value
ItemFrom                        domain tcitem           Minimum Value
ItemTo                          domain tcitem           Maximum Value
OrderLineArray                  domain ttjson           0
ReportName                      domain tcmcs.str16      Empty String
JSON Object OrderLineArray has the following structure:
"OrderLineArray": [
{
"OrderOrigin": 20,
"OrderNumber": "JSC000030",
"OrderLine": 10
},
{
"OrderOrigin": 10,
"OrderNumber": "SLS000012",
"OrderLine": 20
}
]
This structure can be created with the following code:
OrderLineArray = Json.newArray()
OrderLine = Json.newObject()
Json.setNumber(OrderLine, "OrderOrigin", 20)
Json.setString(OrderLine, "OrderNumber", "JSC000030")
Json.setNumber(OrderLine, "OrderLine", 10)
Json.add(OrderLineArray, OrderLine)
OrderLine = Json.newObject()
Json.setNumber(OrderLine, "OrderOrigin", 10)
Json.setString(OrderLine, "OrderNumber", "SLS000012")
Json.setNumber(OrderLine, "OrderLine", 10)
Json.add(OrderLineArray, OrderLine)
ReportName only needs to filled for customized reports, otherwise
the standard report is automatically used.
ReportName must start with an "r", e.g. "rwhinp220411001"
Output: oDataProcessed          - true:  Inventory commitments canceled
false: Nothing canceled.
Return: 0                       - No Error
<> 0                    - Error
```
